#!/usr/bin/env python

__author__="pharno"
__date__ ="$23.03.2011 21:03:58$"

from helpers import *
import re
import matplotlib.pyplot as plot



class Process:
    """represents a single process, cpu and ram stats can be added, and a plot drawn"""
    def __init__(self,pid,cpu,ram):
        """
        @type   pid:    int
        @param  pid:    the PID of the process
        
        @type   cpu:    string
        @param  cpu:    cpu state on init

        @type   ram:    string
        @param  ram:    cpu state on init
        """
        self.pid = int(pid)
        self.ram = [ram]
        self.cpu = [cpu]

    def getProcess(self):
        return self.pid,self

    def getRamArray(self):
        return self.ram

    def addStat(self,cpu="",ram=""):
        if len(self.ram) > 1000:
		self.ram = self.ram[-1000:]
	if len(self.cpu) > 1000:
		self.cpu = self.cpu[-1000:]

	self.ram.append(ram)
        self.cpu.append(cpu)
		
    def getCpu(self):
        return self.cpu

    def plot(self,toFile):
        if len(self.cpu) > 1000:
            plotCPU = self.cpu[-1000:]        
            plotLenCpu = range(len(self.cpu)-1000,len(self.cpu))
        else:
            plotCPU = self.cpu
            plotLenCpu = range(0,len(self.cpu))

        if len(self.ram) > 1000:
            plotRam = self.ram[-1000:]        
            plotLenRam = range(len(self.ram)-1000,len(self.ram))
        else:
            plotRam = self.ram
            plotLenRam = range(0,len(self.ram))

        print len(plotCPU),len(plotLenCpu),len(plotRam),len(plotLenRam)
        global figureid
        plot.figure(figureid)
        figureid +=1
        plot.plot([0],[0])
        plot.plot([1000],[100])
        plot.plot(plotCPU, label = "cpu")        
        plot.plot(plotRam, label = "ram")
        plot.legend()
        #print(dir(plot))
        #plot.set_title(str(self.pid))
        plot.savefig(toFile)

    def __str__(self):
        return "process {0} is using {1} CPU and {2} ram".format(self.pid, self.cpu[-1], self.ram[-1])

    def __repr__(self):
        return self.__str__();

if __name__ == "__main__":
    print("You've called process.py, please call procedente.py instead")
