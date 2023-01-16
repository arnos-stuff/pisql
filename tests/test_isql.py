import os
import re
import rich
import uuid
import subprocess

from pathlib import Path
from typing import List, Tuple, Dict, Union, Optional, Any

def iSqlColumnParser(raw: str) -> List[str]:
    output = re.sub(r" [ ]+", " ", raw)
    output = re.sub(r"\n\t", ";", output)
    column_delimiter = re.findall(r"([ \;\'\-]+')", output).pop()
    # rich.print(column_delimiter)
    rawcols, _ = output.split(column_delimiter)
    columns = [ col.strip() for col in rawcols.replace("'", ";").split(";") if col.strip() != ""]
    return columns

def iSqlRowFormat(columns: List[str]):
    base = r"' "
    for col in columns:
        if col == columns[-1]:
            base += r"(.+)"    
        else:
            base += r"(.+?)[\;\']{1}"
    return base

def iSqlDataParser(raw: str) -> List[str]:
    output = re.sub(r" [ ]+", " ", raw)
    output = re.sub(r"\n\t", ";", output)
    column_delimiter = re.findall(r"([ \;\'\-]+')", output).pop()
    # rich.print(column_delimiter)
    rawcols, rawrows = output.split(column_delimiter)
    columns = [ col.strip() for col in rawcols.replace("'", ";").split(";") if col.strip() != ""]
    
    rowpattern = iSqlRowFormat(columns)
    
    rows = []
    for _row in rawrows.split("'\n'"):
        row = re.findall(rowpattern, _row)
        rich.print(_row)
        rich.print(row)
        rows.append(row)
        
    return columns, rows
        
# basic sybase server configs

config = {
    "sipwmftvasedmf1": {
        "user": "oscardmf_adm",
        "password": "oskdmf1*!",
        "server": "sipwmftvasedmf1",
    }
}

query = "SELECT TOP 500 * FROM WonV16_RUN"

tmpdir = Path.home() / ".isql" / "tmp"
tmpdir.mkdir(exist_ok=True, parents=True)
filename = tmpdir / f"tmp{uuid.uuid4()}.sql"
# add GO statement to end of script
with open(filename, "w+", encoding='utf-8') as fp:
    fp.writelines([query, "\n", "GO"])    

server = config["sipwmftvasedmf1"]["server"]
user = config["sipwmftvasedmf1"]["user"]
password = config["sipwmftvasedmf1"]["password"]
db = "oscar_tma"

command = [
    'isql',
    "-S", server,
    "-U", user,
    "-P", password,
    "-s", "';'",
    "-D", db,
    "-J", "utf8",
    "-X", # encrypt pwd
    "-i", filename
]

result = subprocess.run(
    command,
    stdin=subprocess.DEVNULL,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    creationflags=subprocess.CREATE_NO_WINDOW,
    text=True,
    shell=True,
)
# rich.print(output)
cols, rows = iSqlDataParser(result.stdout)
filename.unlink()

print(cols)
print(rows[:5])