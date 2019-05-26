#!/usr/bin/python

import sqlite3
from sqlite3 import Error
from numpy import matrix
database = "test.db"
# conn = sqlite3.connect(database)

class Camera:
    def __init__(self):
        self.conn = sqlite3.connect(database)

    def getDataCamera(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM camera")
        return cur.fetchall()

    def getSpecificDataCamera(self, TimeStart=None, TimeEnd=None):
        cur = self.conn.cursor()
        try:
            if TimeEnd != None:
                cur.execute("SELECT * FROM camera where datetime(TimeStart) BETWEEN datetime(?) and datetime(?)", (str(TimeStart), str(TimeEnd),))
            else:
                cur.execute("SELECT * FROM camera where datetime(TimeStart) BETWEEN datetime(?) and datetime('now', 'localtime')", (str(TimeStart),))
        except:
            return False

        return cur.fetchall()

    # Update or Insert
    # + x.insertSpecificDataCamera(8,'0000','0000','_','0000')
    # + x.insertSpecificDataCamera(None,'0000','0000','_','0000')
    def insertSpecificDataCamera(self, ID, TimeStart=None, TimeEnd=None, VideoLink=None, Parameter=None):
        cur = self.conn.cursor()
        if ID == None:  # Not Exist
            try:
                query = ''' INSERT INTO camera(TimeStart, TimeEnd, VideoLink, Parameter) VALUES(?,?,?,?) '''
                data = (TimeStart, TimeEnd, VideoLink, Parameter)
                cur.execute(query, data)
            except:
                return False
        else:  # Exist - Update
            try:
                query = ''' UPDATE CAMERA SET TimeStart = ?, TimeEnd = ?, VideoLink = ?, Parameter = ? WHERE ID = ? '''
                data = (TimeStart, TimeEnd, VideoLink, Parameter, ID)
                cur.execute(query, data)
            except:
                return False

        self.conn.commit()

        return True

    def deleteSpecificDataCamera(self, ID):
        cur = self.conn.cursor()
        try:
            query = '''DELETE FROM camera where ID = ?'''
            data = (ID,)
            cur.execute(query, data)
        except:
            return False

        try:
            self.conn.commit()
        except:
            return False

        return True

    def dispose(self):
        self.conn.close()

class Music:
    def __init__(self):
        self.conn = sqlite3.connect(database)

    # Music().getDataMusic()
    def getDataMusic(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM music ORDER BY IsSelected DESC")
        return cur.fetchall()
        
    # Music().getSpecificDataMusic(1)
    def getSpecificDataMusic(self, ID=None, Name=None, Duration=None, IsDelete=None):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM music where ID = ? or Name = ? or Duration = ? or IsDelete = ?",
                        (ID, Name, Duration, IsDelete,))
        except expression as identifier:
            return False

        return cur.fetchall()

    # Get music with music IsDelete and IsSelected
    def getMusicSelected(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM music where IsDelete is null and IsSelected = 1")
        except:
            return False
        
        return cur.fetchall()

    # Update or Insert
    # Music().insertSpecificDataMusic(1,'xyz','15:00')
    # Music().insertSpecificDataMusic(None,'xyz','15:00')
    def insertSpecificDataMusic(self, Name=None, Duration=None, IsDelete=None, IsSelected=None):
        cur = self.conn.cursor()
        if Name == None:  # Not Exist
            try:
                query = ''' INSERT INTO music(Name, Duration, IsDelete, IsSelected) VALUES(?,?,?,?,) '''
                data = (Name, Duration, IsDelete, IsSelected)
                cur.execute(query, data)
            except:
                return False
        else:  # Exist - Update
            try:
                query = ''' UPDATE MUSIC SET Duration = ?, IsDelete = ?, IsSelected = ? WHERE Name = ? '''
                data = (Duration, IsDelete, IsSelected)
                cur.execute(query, data)
            except:
                return False
        
        self.conn.commit()   
        
        return True
    
    def updateSelectedMusic(self, ID):
        cur = self.conn.cursor()
        try:
            query1 = ''' UPDATE Music SET IsSelected = 1 WHERE ID = ? '''
            data1 = (str(ID))
            cur.execute(query1, data1)

            query2 = ''' UPDATE Music SET IsSelected = 0 WHERE ID != ? '''
            data2 = (str(ID))
            cur.execute(query2, data2)
        except Exception as e:
            print str(e)
            return False

        self.conn.commit()

        return True

    # Music().deleteSpecificDataMusic(2)
    def deleteSpecificDataMusic(self, ID):
        cur = self.conn.cursor()
        try:
            query = '''DELETE FROM Music where ID = ?'''
            data = (ID,)
            cur.execute(query, data)
        except:
            return False

        try:
            self.conn.commit()
        except:
            return False

        return True

    def dispose(self):
        self.conn.close()

class SensorMotion:
    def __init__(self):
        self.conn = sqlite3.connect(database)
    # SensorMotion().getDataSensorMotion()
    def getDataSensorMotion(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM SensorMotion")

        return cur.fetchall()

    # SensorMotion().getSpecificDataSensorMotion(1)
    def getSpecificDataSensorMotion(self, TimeStart=None, TimeEnd=None):
        cur = self.conn.cursor()
        try:
            if TimeEnd != 'None':
                cur.execute("SELECT * FROM SensorMotion where datetime(TimeStart) BETWEEN datetime(?) and datetime(?)",
                        (str(TimeStart), str(TimeEnd),))
            else:
                cur.execute("SELECT * FROM SensorMotion where datetime(TimeStart) BETWEEN datetime(?) and datetime('now', 'localtime')", (str(TimeStart),))
        except:
            return False

        return cur.fetchall()


    # SensorMotion().insertSpecificDataSensorMotion(1,'20190505', '20190606', 255)
    def insertSpecificDataSensorMotion(self, ID, TimeStart=None, TimeEnd=None, Quantity=None):
        cur = self.conn.cursor()
        if ID == None:  # Not Exist
            try:
                query = ''' INSERT INTO SensorMotion(TimeStart, TimeEnd, Quantity) VALUES(?,?,?) '''
                data = (TimeStart, TimeEnd, Quantity)
                cur.execute(query, data)
            except:
                return False
        else:  # Exist - Update
            try:
                query = ''' UPDATE SensorMotion SET TimeStart = ?, TimeEnd = ?, Quantity = ? WHERE ID = ? '''
                data = (TimeStart, TimeEnd, Quantity, ID)
                cur.execute(query, data)
            except:
                return False
        try:
            self.conn.commit()
        except:
            return False

        return True
    # SensorMotion().deleteSpecificDataSensorMotion(1)
    def deleteSpecificDataSensorMotion(self, ID, TimeStart=None, TimeEnd=None, Quantity=None):
        cur = self.conn.cursor()
        try:
            query = '''DELETE FROM SensorMotion where ID = ?'''
            data = (ID,)
            cur.execute(query, data)
        except:
            return False

        self.conn.commit()
        
        return True

    def dispose(self):
        self.conn.close()

class DeviceRas:
    def __init__(self):
        self.conn = sqlite3.connect(database)

    def getDataDeviceRas(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM DeviceRas")

        return cur.fetchall()

    # Only Get IpAddress When Having douple Ip Address => check MAC Address
    def getSpecificDataDeviceRas(self, ipAddress):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM DeviceRas where IPAddress = ?",(ipAddress,))
        except:
            return False

        return cur.fetchall()
    
    # Get Full To Check Correctly Device
    def getFullSpecificDataDeviceRas(self, ipAddress, macAddress):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM DeviceRas where IPAddress = ? and MACAddress = ?",(ipAddress,macAddress,))
        except:
            return False

        return cur.fetchall()

    def insertSpecificDataDeviceRas(self, ID, Name=None):
        cur = self.conn.cursor()
        if ID == None:  # Not Exist
            try:
                query = ''' INSERT INTO DeviceRas(Name) VALUES(?) '''
                data = (Name)
                cur.execute(query, data)
            except:
                return False
        else:  # Exist - Update
            try:
                query = ''' UPDATE DeviceRas SET Name = ? WHERE ID = ? '''
                data = (Name, ID)
                cur.execute(query, data)
            except:
                return False

        self.conn.commit()

        return True

    def deleteSpecificDataDeviceRas(self, ID=None, Name=None):
        cur = self.conn.cursor()
        try:
            query = '''DELETE FROM DeviceRas where ID = ?'''
            data = (ID,)
            cur.execute(query, data)
        except:
            return False

        self.conn.commit()

        return True

    def dispose(self):
        self.conn.close()

class Information:
    def __init__(self):
        self.conn = sqlite3.connect(database)

    def getDataInformation(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Information")

        return cur.fetchall()

    def getSpecificInformation(self, Username, Password):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM Information where Username = ? and Password = ?",
                        (Username, Password,))
        except:
            return False

        return cur.fetchall()

    def getAllUserNameInformation(self):
        cur = self.conn.cursor()
        cur.execute("SELECT Username FROM Information")

        return cur.fetchall()

    def insertSpecificInformation(self, Username, Password, Email):
        print '1'
        cur = self.conn.cursor()
        lstUsername = matrix(Information().getAllUserNameInformation()).A1.tolist()
        if Username in lstUsername: # Update
            try:
                query = ''' UPDATE Information set Password = ?, Email = ? WHERE Username = ? '''
                data = (Password, Email, Username)
                cur.execute(query, data)
            except:
                return False
        else: # Insert
            print '2'
            try:
                query = ''' INSERT INTO Information(Username, Password, Email) VALUES(?,?,?) '''
                data = (Username, Password, Email)
                cur.execute(query, data)
            except Exception as e:
                return False

        print '3'
        self.conn.commit()
        print '4'
        return True

    def deleteSpecificInformation(self, Username):
        cur = self.conn.cursor()
        try:
            query = '''DELETE FROM DeviceRas where Username = ?'''
            data = (Username,)
            cur.execute(query, data)
        except:
            return False

        self.conn.commit()

        return True

    def dispose(self):
        self.conn.close()

class SensorSound:
    def __init__(self):
        self.conn = sqlite3.connect(database)
    # SensorSound().getDataSensorSound()
    def getDataSensorSound(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM SensorSound")

        return cur.fetchall()
    # SensorSound().getSpecificSensorSound(1)
    def getSpecificSensorSound(self, TimeStart=None, TimeEnd=None):
        cur = self.conn.cursor()
        try:
            if TimeEnd != None:
                cur.execute("SELECT * FROM SensorSound where datetime(TimeStart) BETWEEN datetime(?) and datetime(?)", (str(TimeStart), str(TimeEnd),))
            else:
                cur.execute("SELECT * FROM SensorSound where datetime(TimeStart) BETWEEN datetime(?) and datetime('now', 'localtime')", (str(TimeStart),))
        except:
            return False

        return cur.fetchall()

    # SensorSound().insertSpecificSensorSound(1,'20190000', '20190101',500)
    # SensorSound().insertSpecificSensorSound(None,'20190000', '20190101',500)
    def insertSpecificSensorSound(self, ID, TimeStart=None, TimeEnd=None, Parameter=None):
        cur = self.conn.cursor()
        if ID == None:  # Not Exist
            try:
                query = ''' INSERT INTO SensorSound(TimeStart, TimeEnd, Parameter) VALUES(?,?,?) '''
                data = (TimeStart, TimeEnd, Parameter)
                cur.execute(query, data)
            except:
                return False
        else:  # Exist - Update
            try:
                query = ''' UPDATE SensorSound SET TimeStart = ?, TimeEnd = ?, Parameter = ? WHERE ID = ? '''
                data = (TimeStart, TimeEnd, Parameter, ID)
                cur.execute(query, data)
            except:
                return False

        self.conn.commit()
        
        return True
    # SensorSound().deleteSpecificSensorSound(2)
    def deleteSpecificSensorSound(self, ID, TimeStart=None, TimeEnd=None, Parameter=None):
        cur = self.conn.cursor()
        try:
            query = '''DELETE FROM SensorSound where ID = ?'''
            data = (ID,)
            cur.execute(query, data)
        except:
            return False

        self.conn.commit()
        
        return True

    def dispose(self):
        self.conn.close()

def main():
    database = "test.db"
    conn = sqlite3.connect(database)
    # Camera().insertSpecificDataCamera(None, '2019', '2020', '_', '300')
    # Camera().deleteSpecificDataCamera(1)
    # print Information().getSpecificInformation('admin','123')
    # Information().insertSpecificInformation('ductrong123','123123','admin@hotmail.com')
    # print SensorMotion().getSpecificDataSensorMotion('2019-04-10 14:30', None)
    # Information().getSpecificInformation('ductrong', '123123')
    # Music().getDataMusic()
    Music().updateSelectedMusic(2)
if __name__ == '__main__':
    main()
