
function execSqlDirFiles() {
	$sqlDir = $PSScriptRoot +"/pisql/assets/sql/";
	$dataDir = $PSScriptRoot +"/pisql/assets/data/";

	$sqlFiles = ls $sqlDir;

	echo $sqlFiles ;


	$i = 0
	foreach($sqlFn in $sqlFiles) {
		$sqlFilePath = $sqlDir + $sqlFn.Name ;
		pisql x $sqlFilePath
		$i++
    	$p = ($i/$sqlFiles.Length)*100

		$Host.PrivateData.ProgressForegroundColor = 'DarkMagenta' ;
		If ($p -gt 25) { $Host.PrivateData.ProgressForegroundColor = "Magenta" }
		If ($p -gt 50) { $Host.PrivateData.ProgressForegroundColor = "DarkCyan" }
		If ($p -gt 75) { $Host.PrivateData.ProgressForegroundColor = "Cyan" }
		If ($p -gt 90) { $Host.PrivateData.ProgressForegroundColor = "Green" }

		$Style = @{
			Activity = 'Processing iSQL queries'
			CurrentOperation = 'Querying $sqlFn'
			PercentComplete = $p
		}
		
    	Write-progress -Activity $Style.Activity -CurrentOperation $Style.CurrentOperation -PercentComplete $Style.PercentComplete
	}
}

execSqlDirFiles

