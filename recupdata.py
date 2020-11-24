#coding:utf-8 
import datetime
import os
import json
#----------Api part
from flask_cors import CORS, cross_origin
from flask import Flask
from flask_restful import Api, Resource , reqparse
app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
now = datetime.datetime.now() 
class recupdata(Resource):
    #Methode post : pour utiliser chemin=/Target
    def post( self,result):
        parser = reqparse.RequestParser()
        parser.add_argument("grsrp")
        parser.add_argument("grsrq")
        parser.add_argument("gsinr")
        args = parser.parse_args()
        with open("log.txt","a+")as temp:
            json.dump(args,temp) 
            print ("La date courante est : ")
            print (now.strftime("%H:%M:%S %d/%m/%Y "))
        if (result=="pr"):
            print("donnees recu://///")
            print("grsrp==>", args["grsrp"])
            print("grsrq==>", args["grsrq"])
            print("gsinr==>", args["gsinr"] )
            
            return "it's good !!!",200
        return "syntax error",404


    def get (self,result):
        return "le get est okay, "

            

api.add_resource(recupdata,"/<string:result>")
#---------------------End API REsT
#-----------------------------------------###MaIn###---------------------------#
print("Server start")
app.run( host='0.0.0.0',port=1246 ,debug=True)


