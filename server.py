#!/usr/bin/env python

__author__="pharno"
__date__ ="$26.03.2011 23:12:45$"


#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir
import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from helpers import *


baseFolder = os.path.join(os.getcwd(),"site/")

print baseFolder

#exit(0)
class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith(".psp"):
                fi = os.path.normpath(baseFolder+self.path)
                if os.path.isfile(fi):
                    print "python "+fi
                    fiout = check_output("python "+ fi)
                    print fiout
                    self.send_response(200)
                    self.send_header('Content-type',	'text/html')
                    self.end_headers()
                    self.wfile.write(fiout)
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

def main():
    try:
        server = HTTPServer(('', 1337), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
        print "asdf"
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()


