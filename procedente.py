#!/usr/bin/env python

__author__="pharno"
__date__ ="$23.03.2011 20:55:45$"

import process
import re,time,os

from helpers import *


if __name__ == "__main__":
    processes = {}

    output = check_output(["ps", "auxww"]).decode("utf-8")
    outarr = output.split("\n")[1:-1]

    for i in outarr:
#        print(i)
        out = re.search(r"([a-z,A-Z,0-9]+)\s+(\d*)\s+(\d*.\d*)\s+(\d*.\d*)(.*)",i)

        proc = process.Process(out.group(2),out.group(3),out.group(4)).getProcess()
        processes[proc[0]] = proc[1]


    for i in range(0,100):
        output = check_output(["ps", "auxww"]).decode("utf-8")
        outarr = output.split("\n")[1:-1]

        print(len(outarr))
        for j in outarr:
            try:
                out = re.search(r"([a-z,A-Z,0-9]+)\s+(\d*)\s+(\d*.\d*)\s+(\d*.\d*)\s+([a-zA-Z0-9\<\>\[\]?\s]*)",j)

                try:
                    proc = processes[int(out.group(2))]
                    proc.addStat(out.group(3),out.group(4))
                except:
                    proc = process.Process(out.group(2),out.group(3),out.group(4)).getProcess()
                    processes[proc[0]] = proc[1]

            except Exception as exp:
                print("exception")
                print(repr(exp))
                print(repr(j))
                print(out.group(2))
                print(out.group(3))
                print(out.group(4))




        time.sleep(1)
    for i in processes:
        print(i, processes[i].getCpu())
        #pass

    plotPID = int(raw_input("plot pid:"))

    #plotPID = 10
    if plotPID > 0:
        try:
            processes[plotPID].plot(str(plotPID) + ".png")
        except Exception as exp:
            print(exp)
    print(os.getcwd())


