#Automate the creation of a linked clone of kali
Write-Host "This script will create a linked clone of the kali vm"

#Shut down and snapshot the vm
Write-Host "Stopping and snapshotting the target vm"
Stop-VM -Name Kali
#Start-Sleep -Seconds 5
Write-Host "VM-Stopped"

Get-VM -Name Kali | Checkpoint-VM -SnapshotName "Pre-parent Snapshot"
Write-Host "Snapshot Created, Beginning clone operations"

#Set the parent VHD to read only

Set-ItemProperty -Path "C:\Users\Public\Documents\Hyper-V\Virtual Hard Disks\Kali.vhdx" `
-Name IsReadOnly -Value $true

Write-Host "Parent vhd set to read only"

#Create a new virtual hard disk that points to the parent's VHD

New-VHD -Path "C:\Users\Public\Documents\Hyper-V\Virtual Hard Disks\SonofKali.vhdx" `
-ParentPath "C:\Users\Public\Documents\Hyper-V\Virtual Hard Disks\Kali.vhdx" -Differencing

Write-Host "New VHD created"

#Then create a new VM
New-VM -Name "SonofKali" -MemoryStartupBytes 4GB -SwitchName "Hyper-V-Wan" -BootDevice VHD `
-Path "C:\Users\Public\Documents\Hyper-V\Virtual Hard Disks\SonofKali" -Generation 2 

Add-VMHardDiskDrive -VMName SonofKali -Path "C:\Users\Public\Documents\Hyper-V\Virtual Hard Disks\SonofKali.vhdx"
#-NewVHDPath "C:\Users\Public\Documents\Hyper-V\Virtual Hard Disks\SonofKali.vhdx"`
#-NewVHDSizeBytes 127GB

Write-Host "Linked Clone Created!"

$vhd = Get-VMHardDiskDrive -VMName SonofKali

Set-VMFirmware -VMName SonofKali -BootOrder $vhd -EnableSecureBoot Off

Write-Host "boot device set, secure boot off"

Get-VMFirmware SonofKali | Select-Object *
