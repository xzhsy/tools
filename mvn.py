#!/usr/bin/python
import paramiko
import os
import time
import configparser
import urllib.request
import urllib


from paramiko import SSHClient


class Deploy(object):
    def __init__(self,config_file):
        self.__configfile = config_file

    
    def deploy(self):
        # start = int(round(time.time) * 1000) 

        CONFIG_SETIONS_REMOTE = 'remote'

        NOW = time.strftime('%Y%m%d_%H%M%S')
        config = configparser.ConfigParser()
        config.read(self.__configfile)

        PROJECT_DIR = config.get(CONFIG_SETIONS_REMOTE,'project_dir')
        ENV = config.get(CONFIG_SETIONS_REMOTE,'env')

        REMOTE_HOST = config.get(CONFIG_SETIONS_REMOTE,'hostname')
        REMOTE_PORT = config.get(CONFIG_SETIONS_REMOTE,'port')
        REMOTE_USERNAME = config.get(CONFIG_SETIONS_REMOTE,'username')
        REMOTE_PASSWORD = config.get(CONFIG_SETIONS_REMOTE,'password')


        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(REMOTE_HOST,REMOTE_PORT,REMOTE_USERNAME,REMOTE_PASSWORD)
        cargs='source ~/.bash_profile && echo $MAVEN_HOME'
        try:
            stdin,stdout,stderr = ssh.exec_command(cargs)
            MAVEN_HOME = str(stdout.readlines()[0]).strip('\n')
        except Exception as e:
            print(e)    
        
        print(MAVEN_HOME)
        # cmd='pwd'
        cmd = MAVEN_HOME + '/bin/mvn -f ' + PROJECT_DIR + '/pom.xml clean package -Dmaven.test.skip=true ' 
        print("Running remote cmd:%s" % cmd)
        try:
            stdin,stdout,stderr = ssh.exec_command(cmd,bufsize=1)
            # print(stdout.read())
            for l in stdout:
                print(l.strip('\n')) 
        except Exception as e:
            print(e)
        ssh.close()



       
if __name__ == "__main__":
    a=Deploy('config.ini')
    a.deploy()

