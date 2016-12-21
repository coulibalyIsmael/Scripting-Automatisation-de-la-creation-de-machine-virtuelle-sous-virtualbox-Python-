from subprocess import call
from subprocess import check_output
import os
#VBoxManage createvm --name "nio ___**"
name="Centos4"
typeOs="Linux"
#modifyvm --
version="Debian_64"
formatdisk="VDI"
ram="2000"
hard_disk="15000"
nomVDI=name+".vdi"
nomVDI
IDE="IDE controller"
cheminIso="E:\\gparted-live-0.23.0-1-i586.iso"
cheminVDI="C:\\Python27\\"+nomVDI
controller="PIIX4"
#createhd --size megamybte

#modifyhd --<uuid|filename>,--resize
call("VBoxManage createvm --name "+name+" --register",shell=True)

#modifyvm --memory taille RAM in MB && --ostype type os
call("VBoxManage modifyvm " +name+" --memory "+ram+" --audio dsound"+" --ioapic on ",shell=True)

#parametrage reseau et type du os
call("VBoxManage modifyvm " +name+" --ostype "+version,shell=True)

#createhd --format VDI-VMDK-VHD default:VDI
call("VBoxManage createhd --filename "+nomVDI+" --size "+ hard_disk,shell=True)

call("VBoxManage storagectl " +name+" --name 'IDE_controller' "+" --add ide"+" --controller "+controller,shell=True)
call("VBoxManage storageattach " +name+" --storagectl 'IDE_controller'"+" --port 0 --device 1 --type hdd --medium "+cheminVDI,shell=True)
call("VBoxManage storageattach " +name+" --storagectl 'IDE_controller'"+" --port 0 --device 1 --type dvddrive --medium "+cheminIso,shell=True)
call("VBoxManage guestproperty set " +name+  " /VirtualBox/GuestAdd/VBoxService/--timesync-min-adjust" ,shell=True)
#activer usb 2.0
call("VBoxManage modifyvm "+name+" --usbehci on",shell=True)

#activer le nat sur carte 1
call("VBoxManage modifyvm "+name+" --nic1 nat ",shell=True)

