# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="pharno"
__date__ ="$23.03.2011 21:03:58$"
import subprocess
import re
class Process:

    

    def __init__(self,id,ram,cpu):
        self.id = int(id)
        self.ram = [ram]
        self.cpu = [cpu]

#        print (self.cpu[-1],self.ram[-1])
    def getProcess(self):
        return self.id,self

    def getRamArray(self):
        return self.ram

    def addStat(self,ram="",cpu=""):
        self.ram.append(ram)
        self.cpu.append(cpu)

    def getCpu(self):
        
        return self.cpu
    def __str__(self):
        return "process %s is using %s CPU and %s ram" % (self.id,self.cpu[-1],self.ram[-1])

    def __repr__(self):
        return self.__str__();

if __name__ == "__main__":
    print("got call to process.py ,call ftue.py instead")
