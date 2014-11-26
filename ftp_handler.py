import ftplib
import os
import directories
import shutil
import time

class MCEdit_FTP_Client:

    def read_properties(self):
        levelname = "world"
        with open(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+'server.properties', 'r') as props_f:
            old_content = props_f.readlines()
            for prop in old_content[0].split('\r'):
                if prop.startswith("level-name"):
                    levelname = prop.split("=")[1:][0]
        print levelname
        return levelname
    
    def download_folder(self, folder, level):
        try:
            os.mkdir(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+level+os.path.sep+folder)
        except OSError:
            pass
        self._ftp.cwd(folder)
        if self._ftp.nlst()[2:] != []:
            for item in self._ftp.nlst()[2:]:
                self._ftp.retrbinary("RETR "+item, open(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+level+os.path.sep+folder+os.path.sep+item, 'wb').write)
        self._ftp.cwd("..")
        #time.sleep(10)
        pass


    def getWorld(self, level):
        try:
            os.mkdir(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+level)
        except OSError:
            pass
        self._ftp.cwd(level)
        found = self._ftp.nlst()
        for obj in found[2:]:
            if "." in obj:
                print obj
                self._ftp.retrbinary("RETR "+obj, open(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+level+os.path.sep+obj, 'wb').write)
            else:
                print obj+" is a folder"
                self.download_folder(obj, level)
    
    
    def __init__(self, address, username, password):
        try:
            os.mkdir(directories.getDataDir()+os.path.sep+'ftp-data')
        except OSError:
            pass

        # Removed FTP class init due to containing my password, it will be re-added once everything is implemented
        self._ftp = ftplib.FTP(address, username, password)
        for f in self._ftp.nlst():
            if f == "server.properties":
                self._ftp.retrlines("RETR server.properties", open(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+'server.properties', 'wb').write)
                level = self.read_properties()
                self.getWorld(level)
        
    def stop(self):
        shutil.rmtree(directories.getDataDir()+os.path.sep+'ftp-data')
        self._ftp.quit()
        

yn = raw_input("CMD: ")
if yn == "stop":
    client.stop()  # @UndefinedVariable