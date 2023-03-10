[![License](https://img.shields.io/badge/Licence-MIT-blue.svg)](/LICENSE) [![PyPI](https://img.shields.io/badge/PyPI-latest-green.svg)](https://pypi.org/project/pisql) [![License](https://img.shields.io/badge/Archives-targz-purple.svg)](https://pypi.org/project/pisql/#files)

# What is pisql ?

pisql is a mix of a command line tool and a small python library to interact with a [Sybase ASE][1] database.  
It so happens, that I have to work with a Sybase ASE database and I wanted to have a tool to interact with it.  

## But why ?

The reason I built this is fairly simple although frustrating:

* My company has tight control over what gets installed on the workstations
* My company hasn't bought the SQL Anywhere drivers for ASE on top of ASE itself as of today
* The only way I have to interact with the database is through a [very old and ugly piece of software called "sqlDbx"][2].
* I wanted to have scripting and automation capabilities that the interface couldn't provide, but that bash/powershell/python could.

## What is it ?

pisql is, for the CLI part, a [rich CLI wrapper][3] around the barebones [isql][4] command line tool that comes with the ASE installation every time.

For the python part, it's a small library that allows you to interact with the database through python code.
You can turn `.sql` files into dataframes ([pandas](https://pandas.pydata.org/) or [polars](https://pola.rs)), and further manipulate them.
You can use every tool you have in python to interact with the data, vizualize it, etc.

## How do I use it ?

### Installation

You can install pisql through pip:

```bash
    pip install pisql
```

Although I recommend `pipx`:

```bash
    pipx install pisql
```

This works on Windows, Linux and MacOS.

### Usage

#### CLI

The CLI is fairly simple to use.

To execute a single .sql file, you can just use the `exec` command:

```bash
    pisql exec my_file.sql
```

which is also aliased to `pisql e my_file.sql` and `pisql x my_file.sql`.

To execute multiple .sql files, you can use what I call the "query mode" or "run mode", using either  
the symbols `q`, `run` or `::`. Once this more is activated, you can chain multiple executions together  
by using the `++` or `//` commands:

```bash
    pisql q ++ file_one.sql file_two.sql file_three.sql
```

An important feature of this mode, is that you can list both files and directories.


```bash
    pisql :: // file.sql some_dir other_file.sql
```

What happens then is that pisql will execute sequentially:

* `file.sql` first
* then all the `.sql` files in `some_dir` second
* then `other_file.sql` last

One nice feature is the presence of rich progress bars like so (give example)

**NB:** I haven't had the time to implement further recursion, so if you have a directory in `some_dir`, it will be ignored.

#### Python

Will explain in the next few days.

## What's next ?

I'm currently working on a few things:

* [ ] Implementing a config file subcommand to set the default database, user, etc.
* [ ] Give more freedom to users to change the storage of the dataframes and config files
* [ ] Build a semi ORM to interact with the database through python. Comes to mind the SELECT, WHERE, JOIN, etc. clauses.
* [ ] Have a little templating feature, but nothing too fancy. I don't want to reinvent the wheel here.
* [ ] Use Agg-Grid to have a  web interface to interact with the database. I'm not sure how to do this yet, but I'll figure it out.

Here's most of it for now ! I'll update this as I go.

[1]: https://www.sap.com/products/technology-platform/sybase-ase.html
[2]: http://www.sqldbx.com/
[3]:https://github.com/Textualize/rich
[4]:https://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc35456.1570/html/ocspsunx/X33477.htm