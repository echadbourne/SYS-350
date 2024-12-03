
$Prompt = "Please choose your operation:`n"
$Prompt += "0 - Exit`n"
$Prompt += "1 - Start sonofubuntu`n"
$Prompt += "2 - Stop sonofubuntu`n"
$Prompt += "3 - Take a checkpoint of sonofubuntu`n"
$Prompt += "4 - Switch sonofubuntu to another network`n"

$operation = $true

while ($operation){
        Write-Host $Prompt | Out-String
        $choice = Read-Host
        if($choice -eq 0){
            Write-Host "Goodbye" | Out-string
            $operation = $false
        }
        elseif($choice -eq 1){
            #Start vm
            Write-Host "Starting sonofubuntu"
            Start-VM -Name sonofubuntu
            Write-Host "Done"
        }
        elseif($choice -eq 2){
            #stop vm
            Write-Host "Stopping sonofubuntu"
            Stop-VM -Name sonofubuntu
            Write-Host "Done"
        }
        elseif($choice -eq 3){
            #Create a checkpoint

            Write-Host "Please enter a name for your checkpoint"
            $name = Read-Host
            Get-VM -Name sonofubuntu | Checkpoint-VM -SnapshotName $name
            Write-Host "Snapshot Created"
        }
        elseif($choice -eq 4){
            #change vm network
            Write-Host "Current vm network"
            $network = Get-VM -Name sonofubuntu | Get-VMNetworkAdapter
            Write-Host $network
            Write-Host "Please enter the network you want to change sonofubuntu to"
            $switch = Read-Host
            Get-VM -Name sonofubuntu | Get-VMNetworkAdapter | Connect-VMNetworkAdapter -SwitchName $switch
        }
        else{
            Write-Host "Please enter a valid option"
        }
}
