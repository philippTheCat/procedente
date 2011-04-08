import urllib
import random
import json
from hashlib import sha1,sha256
class procedenteAPI:
    def __init__(self,host="http://localhost",port=1337):
        self.hostName = host
        self.port = port
        self.host = "{0}:{1}/".format(self.hostName,self.port)
    def authenticate(self,token,user):
        tokenHash,salt = self.__hash__(token)
        #print tokenHash,salt
        Vars = {    "token" : tokenHash,
                    "salt"  : salt,
                    "user"  : user}
        ServerReply = self.__get("authenticate",Vars)
        return ServerReply

    def __hash__(self,toHash,salt=str(random.randint(0,1231235243123))):

            toHash = str(toHash)
            FirstPart = toHash[0:10] + salt
            SecondPart = toHash[10:] + salt
            
            firstPartHashed = sha1(FirstPart).hexdigest()
            secondPartHashed = sha1(SecondPart).hexdigest()

            Hashed = sha256(firstPartHashed + secondPartHashed).hexdigest()
            return Hashed,salt
    def __joinVars(self,Vars):
        VarsArray = []
        if type(Vars).__name__ == "dict":
            for key in Vars:
                value = Vars[key]
                VarsArray.append("{0}/{1}".format(key,value))
            VarsOutPut = "/".join(VarsArray)
            return VarsOutPut
        else:
            print type(Vars).__name__

    def __get(self,function,Vars):
        Vars = self.__joinVars(Vars)
        out =  "{0}api/{1}/{2}".format(self.host,function,Vars)
        ServerReply = urllib.urlopen(out).read()
        reply = json.loads(ServerReply)

        return reply
