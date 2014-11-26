from ftplib import FTP

def read_properties():
    levelname = "world"
    with open('server.properties') as props_f:
        content = []
        old_content = props_f.readlines()
        for line in old_content:
            content.append(line.strip('\n'))
        for prop in content:
            if prop.startswith("level-name"):
                levelname = prop.split("=")[1:][0]
    print levelname
    return levelname

read_properties()

# Removed FTP class init due to containing my password, it will be re-added once everything is implemented

for f in ftp.nlst():
    if f == "server.properties":
        print "Founds Server Properties"
        
ftp.quit()