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

    def getSpecificDataCamera(self, ID=None, TimeStart=None, TimeEnd=None, Parameter=None):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM camera where Id = ? or TimeStart like ? or TimeEnd like ? or Parameter = ?",
                        (ID, unicode(str(TimeStart), "utf-8") + '%', unicode(str(TimeEnd), "utf-8") + '%', Parameter,))
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

    def getDataMusic():
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM music")
        return cur.fetchall()

    def getSpecificDataMusic(self, ID=None, Name=None, Duration=None, IsDelete=None):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM music where ID = ? or Name = ? or Duration = ? or IsDelete = ?",
                        (ID, Name, Duration, IsDelete,))
        except expression as identifier:
            return False

        return cur.fetchall()

    # Update or Insert
    def insertSpecificDataMusic(self, ID, Name=None, Duration=None, IsDelete=None):
        cur = self.conn.cursor()
        if ID == None:  # Not Exist
            try:
                query = ''' INSERT INTO music(Name, Duration, IsDelete) VALUES(?,?,?) '''
                data = (Name, Duration, IsDelete)
                cur.execute(query, data)
            except:
                return False
        else:  # Exist - Update
            try:
                query = ''' UPDATE MUSIC SET Name = ?, Duration = ?, IsDelete = ? WHERE ID = ? '''
                data = (Name, Duration, IsDelete, ID)
                cur.execute(query, data)
            except:
                return False
        
        self.conn.commit()   
        
        return True

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

    def getDataSensorMotion(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM SensorMotion")

        return cur.fetchall()

    def getSpecificDataSensorMotion(self, ID=None, TimeStart=None, TimeEnd=None, Quantity=None):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM SensorMotion where Id = ? or TimeStart like ? or TimeEnd like ? or Quantity = ?",
                        (ID, unicode(str(TimeStart), "utf-8") + '%', unicode(str(TimeEnd), "utf-8") + '%', Quantity,))
        except:
            return False

        return cur.fetchall()

    def insertSpecificDataSensorMotion(self, ID, TimeStart=None, TimeEnd=None, Quantity=None):
        cur = self.conn.cursor()
        if ID == None:  # Not Exist
            try:
                query = ''' INSERT INTO SensorMotion(Name, TimeStart, TimeEnd, Quantity) VALUES(?,?,?) '''
                data = (Name, TimeStart, TimeEnd, Quantity)
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

    def getSpecificDataDeviceRas(self, ID=None, Name=None):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM DeviceRas where Id = ? or Name = ?",
                        (ID, Name,))
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
            try:
                query = ''' INSERT INTO Information(Username, Password, Email) VALUES(?,?,?) '''
                data = (Username, Password, Email)
                cur.execute(query, data)
            except Exception as e:
                print e
                return False

        self.conn.commit()

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

    def getDataSensorSound(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM SensorSound")

        return cur.fetchall()

    def getSpecificSensorSound(self, ID=None, TimeStart=None, TimeEnd=None, Parameter=None):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM SensorSound where Id = ? or TimeStart like ? or TimeEnd like ? or Parameter = ?",
                        (ID, unicode(str(TimeStart), "utf-8") + '%', unicode(str(TimeEnd), "utf-8") + '%', Parameter,))
        except:
            return False

        return cur.fetchall()

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
    Information().insertSpecificInformation('ductrong','123123','admin@hotmail.com')

if __name__ == '__main__':
    main()
