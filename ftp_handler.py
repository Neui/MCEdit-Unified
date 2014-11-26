import ftplib
import os
import directories
import shutil

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
            for item in self._ftp.nlst():
                if item != ".." and item != "." and item != "##MCEDIT.TEMP##":
                    self._ftp.retrbinary("RETR "+item, open(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+level+os.path.sep+folder+os.path.sep+item, 'wb').write)
        self._ftp.cwd("..")
        pass


    def getWorld(self, level):
        try:
            os.mkdir(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+level)
        except OSError:
            pass
        self._ftp.cwd(level)
        found = self._ftp.nlst()
        for obj in found:
            if obj != ".." and obj != "." and obj != "##MCEDIT.TEMP##":
                if "." in obj:
                    print obj
                    self._ftp.retrbinary("RETR "+obj, open(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+level+os.path.sep+obj, 'wb').write)
                else:
                    print obj+" is a folder"
                    self.download_folder(obj, level)
        self._ftp.cwd("..")
    
    
    def __init__(self, address, username, password):
        try:
            os.mkdir(directories.getDataDir()+os.path.sep+'ftp-data')
        except OSError:
            pass

        self._ftp = ftplib.FTP(address, username, password)
        for f in self._ftp.nlst():
            if f == "server.properties":
                self._ftp.retrlines("RETR server.properties", open(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+'server.properties', 'wb').write)
                level = self.read_properties()
                self._level = level
                self.getWorld(level)
                
    def delete_folder(self, folder):
        self._ftp.cwd(folder)
        files = self._ftp.nlst()[2:]
        for f in files:
            self._ftp.delete(f)
        self._ftp.cwd("..")
        self._ftp.rmd(folder)

    def upload_changes(self):
        print os.listdir(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+self._level)
        self._ftp.cwd(self._level)
        found = self._ftp.nlst()
        for obj in found:
            if obj != ".." and obj != "." and obj != "##MCEDIT.TEMP##":
                if "." in obj:
                    print obj
                    self._ftp.delete(obj)
                else:
                    print obj+" is a folder"
                    self.delete_folder(obj)
        self._ftp.cwd("..")
        self._ftp.rmd(self._level)
        self._ftp.mkd(self._level)
        self._ftp.cwd(self._level)
        print "Uploading files...."
        for entry in os.listdir(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+self._level):
            if entry != "##MCEDIT.TEMP##":
                if os.path.isfile(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+self._level+os.path.sep+entry):
                    print "Uploading "+entry
                    self._ftp.storbinary("STOR "+entry, open(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+self._level+os.path.sep+entry, 'rb'))
                    print "Uploaded "+entry
                else:
                    files_to_upload = os.listdir(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+self._level+os.path.sep+entry)
                    try:
                        self._ftp.mkd(entry)
                    except ftplib.error_perm:
                        pass
                    self._ftp.cwd(entry)
                    for f in files_to_upload:
                        if f != "##MCEDIT.TEMP##":
                            if os.path.isfile(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+self._level+os.path.sep+entry+os.path.sep+f):
                                print "Uploading "+f+" to folder ("+entry+")"
                                self._ftp.storbinary("STOR "+f, open(directories.getDataDir()+os.path.sep+'ftp-data'+os.path.sep+self._level+os.path.sep+entry+
                                                                     os.path.sep+f, 'rb'))
                                print "Uploaded "+f+" to folder ("+entry+")"
                            else:
                                self._ftp.mkd(f)
                            self._ftp.cwd("..")
                
    @property   
    def level(self):
        return self._level
    
    def stop(self):
        self.upload_changes()
        #shutil.rmtree(directories.getDataDir()+os.path.sep+'ftp-data')
        self._ftp.quit()