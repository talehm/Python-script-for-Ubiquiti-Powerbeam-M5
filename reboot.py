from pexpect import pxssh
from datetime import datetime,timedelta
import logging,logging.handlers,logging.config
import os,os.path 
import io,sys,time,socket

#Get current time
today = datetime.today()

#Calculating date of 4 weeks before now.
d = today - timedelta(days=28)
date="{:%d_%m_%Y}".format(d.date())
today="{:%d_%m_%Y}".format(today.date())

#Creating automatic log file according time current time.
new_logfile="log_"+today+".log"
open(new_logfile,'a').close()

#Checking if the file named according to 4 week before now. It is deleted if exists.
old_logfile="log_"+date+".log"
if os.path.exists(old_logfile):
    os.remove(old_logfile)
else:
    pass
    
# .txt file that contains ip addresses
selected_cmd_file=open('ip_list.txt', 'r')
selected_cmd_file.seek(0)

# Logging configuration shows status of processes in log file after each step.
logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%d, %b %Y %I:%M:%S %p',filename=new_logfile,filemode='w', level=logging.DEBUG)

for hostname in selected_cmd_file.readlines():
    logging.info("Connecting to: "+ hostname)
    # Checking devices via ping before starting the process 
    response=os.system("ping -c 3 "+hostname)
    if response==0:
        logging.info("Status is up")
        try:
            # Creating ssh session
            s=pxssh.pxssh()
            # Logging the devices using current username and password
            s.login(hostname, 'username', 'password')
            s.sendline("\n")
            # Log information of process send to log file.
            logging.info("Connected !")
            logging.info("Rebooting the device...")
            # Rebooting the device.
            s.sendline('reboot')
            s.sendline("\n")
            logging.info(hostname+" is rebooted \n")
            s.close()
        except pxssh.ExceptionPxssh:
            logging.info ("pxssh failed on login.")
            logging.info (str(e))
            logging.info(hostname+" is up but could not rebooted \n")
    else:
        # Log information of process send to log file.
        logging.info("Status is down")
    


        
        
        
        
    
        
        
        
    

    







