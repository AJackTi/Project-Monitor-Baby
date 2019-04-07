from flask import Flask, request, jsonify
import logging
import os
import time
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_restful import Resource, Api
from bottle import post, request
import ast
import db

db_connect = create_engine('sqlite:///test.db')
app = Flask(__name__)
api = Api(app)

# http://localhost:5002/cameras
class Cameras(Resource):
    # get all data
    def get(self):
        lstResult = db.Camera().getDataCamera()
        lstReturn = []
        subResult = {}
        for i in lstResult:
            subResult['ID'] = i[0]
            subResult['TimeStart'] = i[1]
            subResult['TimeEnd'] = i[2]
            subResult['VideoLink'] = i[3]
            subResult['Parameter'] = i[4]
            lstReturn.append(subResult)
            subResult = {}
        return [i for i in lstReturn]

# http://localhost:5002/camera/6/20190303/20190404/5500
class Camera(Resource):
    def get(self, id, timestart, timeend, parameter):
        lstResult = db.Camera().getSpecificDataCamera(id, timestart, timeend, parameter)
        lstReturn = []
        subResult = {}
        for i in lstResult:
            subResult['ID'] = i[0]
            subResult['TimeStart'] = i[1]
            subResult['TimeEnd'] = i[2]
            subResult['Parameter'] = i[3]
            lstReturn.append(subResult)
            subResult = {}
        return [i for i in lstReturn]

# http://localhost:5002/postcamera/10/20190303/20190404/0000/5500
# http://localhost:5002/postcamera/None/20190303_3030/20190404_3030/0000/5500
# http://localhost:5002/postcamera/10/20190303_3030/20190404_3030/0000/5500
class postCamera(Resource):
    def post(self, id, timestart, timeend, videolink, parameter):
        if ast.literal_eval(id) is None:
            if db.Camera().insertSpecificDataCamera(None, timestart, timeend, videolink, parameter):
                return {'status': 'success'}
            else:
                return {'status': 'fail'}
        else:
            if db.Camera().insertSpecificDataCamera(None, timestart, timeend, videolink, parameter):
                return {'status': 'success'}
            else:
                return {'status': 'fail'}

# http://localhost:5002/deleteCamera/10
class deleteCamera(Resource):
    def delete(self, id):
        if db.Camera().deleteSpecificDataCamera(int(id)):
            return {'status': 'success'}
        else:
            return {'status': 'fail'}

class DeviceRas(Resource):
    # get all data
    def get(self):
        lstResult = db.DeviceRas().getDataDeviceRas()
        lstReturn = []
        subResult = {}
        for i in lstResult:
            subResult['ID'] = i[0]
            subResult['Name'] = i[1]
            lstReturn.append(subResult)
            subResult = {}
        return [i for i in lstReturn]

class DeviceRass(Resource):
    def get(self, id, name):
        lstResult = db.DeviceRas().getSpecificDataDeviceRas(id, name)
        lstReturn = []
        subResult = {}
        for i in lstResult:
            subResult['ID'] = i[0]
            subResult['Name'] = i[1]
            lstReturn.append(subResult)
            subResult = {}
        return [i for i in lstReturn]

class postDeviceRas(Resource):
    def post(self, id, name):
        if ast.literal_eval(id) is None:
            if db.DeviceRas().insertSpecificDataDeviceRas(None, name):
                return {'status': 'success'}
            else:
                return {'status': 'fail'}
        else:
            if db.DeviceRas().insertSpecificDataDeviceRas(id, name):
                return {'status': 'success'}
            else:
                return {'status': 'fail'}

class deleteDeviceRas(Resource):
    def delete(self, id):
        if db.DeviceRas().deleteSpecificDataDeviceRas(id):
            return {'status': 'success'}
        else:
            return {'status': 'fail'}

# http://localhost:5002/informations
class Informations(Resource):
    # get all data
    def get(self):
        lstResult = db.Information().getDataInformation()
        lstReturn = []
        subResult = {}
        for i in lstResult:
            subResult['ID'] = i[0]
            subResult['Username'] = i[1]
            subResult['Password'] = i[2]
            lstReturn.append(subResult)
            subResult = {}
        return [i for i in lstReturn]

# http://localhost:5002/information/admin/123
class Information(Resource):
    def get(self, username, password):
        lstResult = db.Information().getSpecificInformation(username, password)
        lstReturn = []
        subResult = {}
        for i in lstResult:
            subResult['Username'] = i[0]
            subResult['Password'] = i[1]
            lstReturn.append(subResult)
            subResult = {}
        if len(lstReturn) == 0:
            return {'status': 'fail'}
        else:
            return {'status': 'success'}

# http://localhost:5002/postinformation/admin/321321/dtrong97vn@gmail.com
class postInformation(Resource):
    def post(self, username, password, email):
        if db.Information().insertSpecificInformation(username, password, email):
            return {'status': 'success'}
        else:
            return {'status': 'fail'}

class deleteInformation(Resource):
    def delete(self, id):
        if db.Information().deleteSpecificInformation(id, username):
            return {'status': 'success'}
        else:
            return {'status': 'fail'}

class Music(Resource):
    # get all data
    def get(self):
        lstResult = db.Music().getDataMusic()
        lstReturn = []
        subResult = {}
        for i in lstResult:
            subResult['ID'] = i[0]
            subResult['Name'] = i[1]
            subResult['Duration'] = i[2]
            subResult['IsDelete'] = i[3]
            lstReturn.append(subResult)
            subResult = {}
        return [i for i in lstReturn]

class Musics(Resource):
    def get(self, Username, Password):
        lstResult = db.Information().getSpecificInformation(Username, Password)
        lstReturn = []
        subResult = {}
        for i in lstResult:
            subResult['Username'] = i[0]
            subResult['Password'] = i[1]
            lstReturn.append(subResult)
            subResult = {}
        return [i for i in lstReturn]

class postMusic(Resource):
    def post(self, id, name, duration, isdelete):
        if ast.literal_eval(id) is None:
            if db.Music().insertSpecificMusic(None, name, duration, isdelete):
                return {'status': 'success'}
            else:
                return {'status': 'fail'}
        else:
            if db.Music().insertSpecificMusic(id, name, duration, isdelete):
                return {'status': 'success'}
            else:
                return {'status': 'fail'}

class deleteMusic(Resource):
    def delete(self, id):
        if db.Music().deleteSpecificMusic(id):
            return {'status': 'success'}
        else:
            return {'status': 'fail'}
            
class Enum:
    SAVEDB = 1
    CONNECTDB = 2
    DELETEDB = 3


api.add_resource(Cameras, '/cameras')  # Route_1
api.add_resource(
    Camera, '/camera/<id>/<timestart>/<timeend>/<parameter>')  # Route_2
api.add_resource(
    postCamera, '/postcamera/<id>/<timestart>/<timeend>/<videolink>/<parameter>')  # Route_3
api.add_resource(
    deleteCamera, '/deleteCamera/<id>')  # Route_4

api.add_resource(postInformation, '/postinformation/<username>/<password>/<email>')
api.add_resource(Informations, '/informations')
api.add_resource(Information, '/information/<username>/<password>')

def getDateTime():
    return time.strftime("%Y/%m/%d")

# region Write Log


def writeLog(enumNumber, content):
    # region Save Database
    if enumNumber == 1:
        if(not os.path.isdir('/log/API/SaveDatabase/')):  # Not Exist
            os.mkdir("/log/API/SaveDatabase")

        if os.path.exists('log/API/SaveDatabase/logSaveDatabase_' + getDateTime() + '.log'):  # Exist
            logging.basicConfig(filename='logSaveDatabase_'+getDateTime() + '.log',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                filemode='a', datefmt='%H:%M:%S', level=logging.ERROR)
            logging.error(getDateTime() + ': ' + content)
        else:  # Not Exist
            logging.basicConfig(filename='logSaveDatabase_'+getDateTime() + '.log',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                filemode='w', datefmt='%H:%M:%S', level=logging.ERROR)
            logging.error(getDateTime() + ': ' + content)
    # endregion

    # region Connect Database
    if enumNumber == 2:
        if(not os.path.isdir('/log/API/ConnectDatabase/')):  # Not Exist
            os.mkdir("/log/API/ConnectDatabase")
        if os.path.exists('log/ConnectDatabase/logConnectDatabase_' + getDateTime() + '.log'):  # Exist
            logging.basicConfig(filename='logConnectDatabase_'+getDateTime() + '.log',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                filemode='a', datefmt='%H:%M:%S', level=logging.ERROR)
            logging.error(getDateTime() + ': ' + content)
        else:  # Not Exist
            logging.basicConfig(filename='logConnectDatabase_'+getDateTime() + '.log',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                filemode='a', datefmt='%H:%M:%S', level=logging.ERROR)
            logging.error(getDateTime() + ': ' + content)

# endregion


if __name__ == '__main__':
    app.run(port='5002')
