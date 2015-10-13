#!/usr/bin/env python
#_*_coding:utf-8_*_

import os
import paramiko
import hashlib

class HostInfo:
    number = 0
    def addhost(self, ip, port=None):
        self.host = ip
        self.number += 1
        if port is None:
            self.port = 22
        else:
            self.port = port
        print "ip:%s,total host number is %d" % (self.host, self.number)

    def delhost(self):
        self.number -= 1
        print "ip:%s, deteleted,total host number is %d" % (self.host, self.number)

    def generate_hash_code(self, checkfile):
        m = hashlib.md5()
        m.update(checkfile)
        return m.hexdigest()
    
    def ssh_connect(self, remote_hostname, remote_port=22, remote_username, remote_passwd=None):
        private_key_file = os.path.expanduser('~/.ssh/id_rsa')
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if remote_passwd is None:
            ssh.connect(remote_hostname, remote_port, remote_username, pkey=private_key_file, timeout=5)
            return ssh
        else:
            ssh.connect(remote_hostname, remote_port, remote_username, remote_passwd, timeout=5)
            return ssh

    def exec_cmd(self, ssh, cmd):
        stdin,stdout,stderr = ssh.exec_command(cmd)

    def transfer_file(self, ssh, local_path, remote_path):
        sftp = ssh.open_sftp()

        if os.path.exists(local_path):
            if os.path.isfile(local_path):
                filename = os.path.basename(local_path)
            else:
                return

        if remote_path.endswith('/'):
            remote_file_path = '%s%s' %(remote_path, filename)
        else:
            remote_file_path = '%s/%s' %(remote_path, filename)


       sftp.put(local_path, remote_file_path)
       sftp.close()
       ssh.close()

