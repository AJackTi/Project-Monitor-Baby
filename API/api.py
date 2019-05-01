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
import socket
from flask_cors import CORS
from OpenSSL import SSL
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')

db_connect = create_engine('sqlite:///test.db')
app = Flask(__name__)
api = Api(app)
hostName = socket.gethostbyname(socket.gethostname()) + ":5002"
CORS(app, origins=hostName, allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)

# region Camera
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
        return jsonify(lstReturn)

class Camera(Resource):
    def get(self, timestart, timeend):
        lstResult = db.Camera().getSpecificDataCamera(timestart, timeend)
        lstReturn = []
        subResult = {}
        for i in lstResult:
            subResult['ID'] = i[0]
            subResult['TimeStart'] = i[1]
            subResult['TimeEnd'] = i[2]
            subResult['Parameter'] = i[4]
            lstReturn.append(subResult)
            subResult = {}
        return jsonify(lstReturn)

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
            if db.Camera().insertSpecificDataCamera(id, timestart, timeend, videolink, parameter):
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

# endregion
# region DeviceRas
class DeviceRas(Resource):
    # get all data
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

class DeviceRass(Resource):
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
# endregion
# region Information
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
# endregion
# region Music
class Music(Resource):
    # get all data
    def get(self, id, name, duration, isdelete):
        lstResult = db.Music().getSpecificDataMusic(id, name, duration, isdelete)
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
    def get(self):
        lstResult = db.Music().getDataMusic()()
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
# endregion         
# region SensorMotion
class SensorMotions(Resource):
    # get all data
    def get(self):
        lstResult = db.SensorMotion().getDataSensorMotion()
        lstReturn = []
        subResult = {}
        for i in lstResult:
            subResult['ID'] = i[0]
            subResult['TimeStart'] = i[1]
            subResult['TimeEnd'] = i[2]
            subResult['Quantity'] = i[3]
            lstReturn.append(subResult)
            subResult = {}
        return [i for i in lstReturn]

class SensorMotion(Resource):
    def get(self, timestart, timeend):
        print 'Time: ', timestart, timeend
        lstResult = db.SensorMotion().getSpecificDataSensorMotion(timestart, timeend)
        lstReturn = []
        subResult = {}
        for i in lstResult:
            subResult['ID'] = i[0]
            subResult['TimeStart'] = i[1]
            subResult['TimeEnd'] = i[2]
            subResult['quantity'] = i[3]
            lstReturn.append(subResult)
            subResult = {}
        return jsonify(lstReturn)

class postSensorMotion(Resource):
    def post(self, id, timestart, timeend, quantity):
        if ast.literal_eval(id) is None:
            if db.SensorMotion().insertSpecificDataSensorMotion(None, timestart, timeend, quantity):
                return {'status': 'success'}
            else:
                return {'status': 'fail'}
        else:
            if db.SensorMotion().insertSpecificDataSensorMotion(id, timestart, timeend, quantity):
                return {'status': 'success'}
            else:
                return {'status': 'fail'}

class deleteSensorMotion(Resource):
    def delete(self, id):
        if db.SensorMotion().deleteSpecificDataSensorMotion(int(id)):
            return {'status': 'success'}
        else:
            return {'status': 'fail'}

# endregion
# region SensorSound
class SensorSounds(Resource):
    # get all data
    def get(self):
        lstResult = db.SensorSound().getDataSensorSound()
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

class SensorSound(Resource):
    def get(self, timestart, timeend):
        lstResult = db.SensorSound().getSpecificSensorSound(timestart, timeend)
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

class postSensorSound(Resource):
    def post(self, id, timestart, timeend, parameter):
        if ast.literal_eval(id) is None:
            if db.SensorSound().insertSpecificSensorSound(None, timestart, timeend, parameter):
                return {'status': 'success'}
            else:
                return {'status': 'fail'}
        else:
            if db.SensorSound().insertSpecificSensorSound(id, timestart, timeend, parameter):
                return {'status': 'success'}
            else:
                return {'status': 'fail'}

class deleteSensorSound(Resource):
    def delete(self, id):
        if db.SensorSound().deleteSpecificSensorSound(int(id)):
            return {'status': 'success'}
        else:
            return {'status': 'fail'}
# endregion

class Enum:
    SAVEDB = 1
    CONNECTDB = 2
    DELETEDB = 3

# region API
# region Camera
api.add_resource(Cameras, '/api/cameras')  
api.add_resource(Camera, '/api/camera/<timestart>/<timeend>')  
api.add_resource(postCamera, '/api/postcamera/<id>/<timestart>/<timeend>/<videolink>/<parameter>')  
api.add_resource(deleteCamera, '/api/deleteCamera/<id>')  
# endregion

# region Music
api.add_resource(Musics, '/api/musics')
api.add_resource(Music, '/api/music/<id>/<name>/duration/<isdelete>')
api.add_resource(postMusic, '/api/postMusic/<id>/<name>/duration/<isdelete>')
api.add_resource(deleteMusic, '/api/deleteCamera/<id>')
# endregion

# region SensorMotion
api.add_resource(SensorMotions, '/api/sensormotions')  
api.add_resource(SensorMotion, '/api/sensormotion/<timestart>/<timeend>')  
api.add_resource(postSensorMotion, '/api/postsensormotion/<id>/<timestart>/<timeend>/<quantity>')  
api.add_resource(deleteSensorMotion, '/api/deletesensormotion/<id>')
# endregion

# region DeviceRas
api.add_resource(DeviceRass, '/api/devicerass')  
api.add_resource(DeviceRas, '/api/deviceras/<id>/<name>')  
api.add_resource(postDeviceRas, '/api/postcamera/<id>/<name>')  
api.add_resource(deleteDeviceRas, '/api/deleteCamera/<id>')  
# endregion

# region Information
api.add_resource(postInformation, '/api/postinformation/<username>/<password>/<email>')
api.add_resource(Informations, '/api/informations')
api.add_resource(Information, '/api/information/<username>/<password>')
# endregion

# region SensorSound
api.add_resource(SensorSounds, '/api/sensorsounds')  
api.add_resource(SensorSound, '/api/sensorsound/<timestart>/<timeend>')  
api.add_resource(postSensorSound, '/api/postsensorsound/<id>/<timestart>/<timeend>/<parameter>')  
api.add_resource(deleteSensorSound, '/api/deletesensorsound/<id>')  
# endregion

# endregion


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
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, support_credentials=True)
    context = ('server.crt', 'server.key')
    app.run(host=socket.gethostbyname(socket.gethostname()), port='5002', ssl_context=context, threaded=True, debug=True)
    
