#!/usr/bin/env python
#_*_coding:utf-8_*_

import os
import platform

class Facts():

    def get_file_lines(self, path):
        datafile = open(path)
        try:
            return datafile.readlines()
        finally:
            datafile.close()

    def get_memory(self):
        ORIGINAL_MEMORY_FACTS = ('MemTotal')

        if not os.access("/proc/meminfo", os.R_OK):
            return

        for line in self.get_file_lines("/proc/meminfo"):
            data = line.split(":")
            if data[0] in ORIGINAL_MEMORY_FACTS:
                val = long(data[1].strip().split()[0]) / 1024
                print val

    def get_cpu_processor(self):
        ORIGINAL_CPU_FACTS = ('processor')
        processor = 0
        if not os.access("/proc/cpuinfo", os.R_OK):
            return

        for line in self.get_file_lines("/proc/cpuinfo"):
            data = line.split(":")
            key = data[0].strip()
            if key in ORIGINAL_CPU_FACTS:
               processor += 1

        return processor

