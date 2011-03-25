#!/usr/bin/env python3
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="pharno"
__date__ ="$23.03.2011 21:03:58$"
import subprocess
import re
class Process:

    def __init__(self,pid,ram,cpu):
        self.pid = int(pid)
        self.ram = [ram]
        self.cpu = [cpu]

#        print (self.cpu[-1],self.ram[-1])
    def getProcess(self):
        return self.pid,self

    def getRamArray(self):
        return self.ram

    def addStat(self,ram="",cpu=""):
        self.ram.append(ram)
        self.cpu.append(cpu)

    def getCpu(self):
        return self.cpu

    def __str__(self):
        return "process {0} is using {1} CPU and {2} ram".format(self.pid, self.cpu[-1], self.ram[-1])

    def __repr__(self):
        return self.__str__();

if __name__ == "__main__":
    print("got call to process.py ,call ftue.py instead")
