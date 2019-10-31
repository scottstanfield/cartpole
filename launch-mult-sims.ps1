Param(
    [Parameter(Mandatory=$true)][string]$brain,
    [string]$simFileName = "sim.py",
    [int32]$spawnTotal=16
)

# Create empty processes array
$Processes = @()

#setup command args
$args = $simFileName + " " + $brain 


For ($count=0; $count -lt $spawnTotal; $count++) {
  
# PassThru allows us to pass created process info to variable
  $Process = Start-Process python -ArgumentList $args -PassThru

# Add process to array
  $Processes += $Process

}

#Output loop to list all created subprocesses if verbose is used
If ($PSCmdlet.MyInvocation.BoundParameters["Verbose"].IsPresent)
{
    ForEach ($Process in $Processes)
    {
        $id = $Process.Id
        $name = $Process.Name
        Write-Host ""
        Write-Host "Subprocess created. Subprocess name is $name, id is $id" -ForegroundColor DarkGreen
        
    }
}

Write-Host ""
Write-Host "*** Type exit and hit enter to kill this window and all sim subprocesses ***" -ForegroundColor Red
Write-Host ""

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