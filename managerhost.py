#!/usr/bin/env python
#_*_coding:utf-8_*_

import MySQLdb
import time
from getfacts import Facts


class ManagerHosts():
    number = 0
    group = 0
    idc = 0
    def __init__(self):
        self.conn = MySQLdb.connect(host='192.168.1.100', user='root', passwd='tom.com', db='test', charset='utf8')
        self.cursor = self.conn.cursor()

    def addhosts(self, host_name, ip, port=None, system_type=None):
        self.host = ip
        self.number += 1

        if port is None:
            self.port = 22
        else:
            self.port = port
        self.hostname = host_name

        if system_type is None:
            self.systemtype = 'Linux/Unix'
        else:
            self.systemtype = 'system_type'

        total_mem = get_memory()
        total_cpunum = get_cpu_processor()

        sql = 'insert into host(hostname,ip,port,memory,cpu,type) values(self.hostname,self.host,self.port,total_mem,total_cpunum,self.systemtype)'
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()

    def delhosts(self, ip):
        self.host = ip
        self.number -= 1
        sql = 'delete from host where ip=self.host'
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()

    def addhostgroups(self, group_name):
        self.group = group_name
        self.group += 1

    def delhostgroups(self):
        self.group -= 1

    def addidc(self, idc_name):
        self.idc = idc_name
        self.idc +=1

    def delidc(self):
        self.idc -= 1

    def printhost(self):
        self.cursor.execute('select * from host')
        all = self.cursor.fetcall()
        for line in all:
            print line
        self.conn.close()
