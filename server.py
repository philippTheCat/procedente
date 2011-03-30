#!/usr/bin/env python

__author__="pharno"
__date__ ="$26.03.2011 23:12:45$"


#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir
import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from helpers import *
from threading import Thread

baseFolder = os.path.join(os.getcwd(),"site/")

print baseFolder

#exit(0)
class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith(".psp"):
                fi = os.path.normpath(baseFolder+self.path)
                if os.path.isfile(fi):
                    fiout = check_output(["python", fi])
                    self.send_response(200)
                    self.send_header('Content-type',	'text/html')
                    self.end_headers()
                    self.wfile.write(fiout)
                return
            if self.path.endswith(".png"):
                try:
                    pid = self.path[1:-4]
                    #global processes
                    global processes
                    proc = processes[int(pid)]
                    proc.plot("pics" + self.path)
                    plotimg = open("pics"+self.path)
                    self.send_response(200)
                    self.send_header('Content-type',	'image/jpeg')
                    self.end_headers()
                    self.wfile.write(plotimg.read())
                    print self.path
                except Exception as exp:
                    print repr(exp)
                return
            return
                
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
     

    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            
            self.end_headers()
            upfilecontent = query.get('upfile')
            print "filecontent", upfilecontent[0]
            self.wfile.write("<HTML>POST OK.<BR><BR>");
            self.wfile.write(upfilecontent[0]);
            
        except :
            pass

class procedenteServer(Thread):
    def __init__(self,port,handler):
        Thread.__init__(self)
        self.server = HTTPServer(('', port),handler)
    def run(self):
        try:
            self.server.serve_forever()
        except Exception as exp:
            print exp
    def close(self):
        self.server.socket.close()
        Thread.interrupt_main()

def main():
    try:
#        server = HTTPServer(('', 1337), MyHandler)
        server = procedenteServer(1337,MyHandler)
        server.start()
        print 'started httpserver...'
#        server.serve_forever()
        while True:
            inp = raw_input("quit? [Y/n]:")
            if inp == "Y" or inp == "y" or inp == "\n":
                #pass
                server.close()
    except Exception as exp:
        print exp
        print 'shutting down server'
        print "exiting"

if __name__ == '__main__':
    main()


