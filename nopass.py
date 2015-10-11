#!/usr/bin/env python
#_*_coding:utf-8_*_

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

    def ssh_connect(self, remote_hostname, remote_port=22, remote_username, remote_passwd):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(remote_hostname, remote_port, remote_username, remote_passwd)
        return ssh

    def exec_cmd(self, ssh, cmd):
        stdin,stdout,stderr = ssh.exec_command(cmd)

    def sftp_connect(self, ssh):
        sftp = ssh.open_sftp()
        return sftp

    def sftp_put(self, sftp, localpath, remotepath):
        return sftp.put(localpath, remotepath)

    def sftp_close(self, sftp):
        sftp.close()

    def ssh_close(self, ssh):
        ssh.close()

    def generate_hash_code(self, checkfile):
        m = hashlib.md5()
        m.update(checkfile)
        return m.hexdigest()
