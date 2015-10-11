#!/usr/bin/env python
#_*_coding:utf-8_*_

import logging

format_dict = {
    1:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    2:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    3:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    4:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    5:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
}

class logInfo:

    def __init__(self,logger,filename,loglevel):
        self.onli = logging.getLogger(logger)
        self.onli.setLevel(logging.DEBUG)

        fhandler = logging.FileHandler(filename)
        fhandler.setLevel(logging.DEBUG)

        chandler = logging.StreamHandler()
        chandler.setLevel(logging.DEBUG)

        formatter = format_dict[int(loglevel)]
        fhandler.setFormatter(formatter)
        chandler.setFormatter(formatter)

        self.onli.addHandler(fhandler)
        self.onli.addHandler(chandler)

    def getLog(self):
        return self.onli
