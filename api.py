from helpers import *
from config import *
from hashlib import sha1 ,sha256
import json
import random
global DebugFlag

class APIRequest:
    def __init__(self,ClientHandler,ClientFile,request):
        self.ClientHandler = ClientHandler
        self.ClientFile = ClientFile
        self.__Codes__()
        self.__functions__()
        self.__splitVars__(request)
        self.__callFunction__(self._FUNCTION,self._GET)
        return
        
    def authenticate(self,args):
        token = args["token"]
        salt = args["salt"]
        user = args["user"]
        
        #print typeof(token),typeof(salt),typeof(user)
        global APIUsers
        if user in APIUsers:
            # Split the Userpassword in 2 parts, salt them both, Sha1 them, and make a sha256 of both parts added together
            userpw = APIUsers[user]

            passwordHashed = self.__hash__(userpw,salt)
            print passwordHashed
            if passwordHashed == token:
                print "authenticated {0}".format(user)

                global securityTokens
                if user in securityTokens:
                    token = securityTokens[user]
                else:
                    token = self.__hash__(random.randint(0,52348304503428102339450354829424)*random.random())
                    securityTokens[user] = token
                self.send({"authenticated":True,"token":token})
            return
        self.sendError(403,"not authenticated")
    
    def send(self,Message,MessageType = "json",code=200,):
        
        if MessageType == "json":
            indent = 4 if DebugFlag == True else 0
            #(DebugFlag)? indent = 4 : indent = 0
            Message["status"] = 200
            MessageString = json.dumps(Message,indent = indent)
            print MessageString
        else:
            MessageString = Message

        self.ClientHandler.send_response(code)
        MessageInternalType = self.ApplicationCodes[MessageType]
        self.ClientHandler.send_header("Content-type", MessageInternalType)
        self.ClientHandler.end_headers()
        self.ClientFile.write(MessageString)
        return

    def sendError(self,errorCode,errorMessage = ""):
        self.ClientHandler.send_response(errorCode)
        self.ClientHandler.send_header('Content-type',	'text/html')
        self.ClientHandler.end_headers()
        Message = """
<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1><b>{0}</b></h1>
        <br />
        <br />
        {1}
        <hr>
    </body>
</html>""".format(self.errorCodes[errorCode],errorMessage)
        self.ClientFile.write(Message)
        #return

    def __hash__(self,toHash,salt=str(random.randint(0,1231235243123))):

            toHash = str(toHash)
            FirstPart = toHash[0:10] + salt
            SecondPart = toHash[10:] + salt
            
            firstPartHashed = sha1(FirstPart).hexdigest()
            secondPartHashed = sha1(SecondPart).hexdigest()

            Hashed = sha256(firstPartHashed + secondPartHashed).hexdigest()
            return Hashed

    def __Codes__(self):
        self.errorCodes = { 403: "Forbidden",
                            404: "Not Found"}

        self.ApplicationCodes = {   "json" : "application/json",
                                    "html" : "text/html" }
                            
    def __splitVars__(self,request):
        Vars = request.split("/")
        if len(Vars)> 1:
            self._FUNCTION = Vars[1]

            _GET = {}
            for i in range(2,len(Vars)-1,2):
                j = i+1
                _GET[Vars[i]] = Vars[j]
                i += 1

        self._GET = _GET

    def __functions__(self):
        self.functions = {"authenticate": self.authenticate}

    def __callFunction__(self,function,args):
        func = self.functions[function]
        func(args)
#testString = "/function/variablename1/variablevalue1/variablename2/variablevalue2"

#request = APIRequest(None,None,testString)
