# Python script to reboot Ubiquiti Powerbeam M5

Ubiquiti Powerbeam M5 devices on firmware version below than 6.1.2 ,  work inefficiently. Data or management traffic is not passing through wireless connection to remote device. To overcome this issue, remote device has to be rebooted. And also, there might be problem on spesific vlan traffic between Access and Station. Both sides should be rebooted to normalize the traffic.  

This script reboots Ubiquiti powerbeam M5 devices connecting via ssh automatically.

The following steps should be applied before running the script.

Note: Operating system used in this project is Ubuntu 16.04 TLS.


1. install python2.7

 		- sudo apt-get install python2.7
	
2. You need to install pexpect module to use ssh protocol.

	2.1 Fistly, install pip bu typing command:
	
		- sudo apt-get install python-pip
		
	2.2 Then, install pexpect module using pip.
	
		- pip install pexpect
		
3. Create .txt file called "ip_list.txt". This file contains ip addresses of devices that will be rebooted.


You are ready to run script after applying all the steps required above.
