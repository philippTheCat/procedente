#!/usr/bin/env python3
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="pharno"
__date__ ="$23.03.2011 20:55:45$"

import process
import subprocess,re,time


if __name__ == "__main__":
    processes = []

    output = subprocess.check_output(["ps", "auxww"]).decode("utf-8")
    outarr = output.split("\n")[1:-1]

    for i in outarr:
#        print(i)
        out = re.search(r"([a-z,A-Z,0-9]+)\s+(\d*)\s+(\d*.\d*)\s+(\d*.\d*)(.*)",i)

        proc = process.Process(out.group(2),out.group(3),out.group(4)).getProcess()
        print (proc[0],proc[1])
        processes.insert(proc[0],proc[1])


    for i in range(0,40):
        utput = subprocess.check_output(["ps", "auxww"]).decode("utf-8")
        outarr = output.split("\n")[1:-1]

        for j in outarr:
    #        print(i)
            try:
                out = re.search(r"([a-z,A-Z,0-9]+)\s+(\d*)\s+(\d*.\d*)\s+(\d*.\d*)([a-zA-Z0-9\<\>\[\]?\s]*)",j)

                proc = processes[int(out.group(2))]
                proc.addStat(out.group(3),out.group(4))

#                processes(int(out.group(2)),proc)
                #processes.insert(int(out.group(2)),proc)
            except Exception as exp:
#                print (int(out.group(2)))
#                print (proc)
                print(exp)
                print(repr(j))
                print(out.group(2))
#                print(out.group(3))
#                print(out.group(4))
#                exit(1)



        time.sleep(1)
#        proc = process.Process(out.group(2),out.group(3),out.group(4)).getProcess()

    for i in processes:
#        pass
        print(i.getCpu())

    print("finished")
