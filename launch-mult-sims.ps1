param (
    [string]$brain 
)

# Create empty processes array
$Processes = @()

# sim file name - change as needed
$simFileName = "sim.py"

#setup command args
$args = $simFileName + " " + $brain 

# sim loop
For ($count=0; $count -lt 16; $count++) {
  
# PassThru allows us to pass created process info to variable
  $Process = Start-Process python -ArgumentList $args -PassThru

# Add process to array
  $Processes += $Process

}

#Output loop to list all created subprocesses
ForEach ($Process in $Processes)
{
    $id = $Process.Id
    $name = $Process.Name
  
    Write-Host "Subprocess created. Subprocess name is $name, id is $id" 
    
}

Write-Host "*** Type exit and hit enter to kill this window and all sim subprocesses ***"

# Use Register-EngineEvent and PowerShell.Exiting engine event to kill our sim instances ([System.Management.Automation.PsEngineEvent]::Exiting)
# Piped to Out-Null to suppress output
Register-EngineEvent -SourceIdentifier PowerShell.Exiting -Action {
    $RunningProcesses = Get-Process -Name "Python*" 
    
    ForEach ($Process in $RunningProcesses)
    {
        $id = $Process.Id
    
        Stop-Process -Id $id -Force
    }   
} | Out-Null     