import shelve
import uuid
import socket
import os
import base64

class File:
    def __init__(self):
        if not os.path.exists("files"):
            os.makedirs("files")

    def upload_file(self,namafile=None,isifile=None):
        data_file = isifile
        f = open("files/"+namafile,"wb")
        f.write(base64.decodestring(data_file))
        return True

    def download_file(self,namafile=None):
        temp = []
        f = open("files/" + namafile, "rb")
        l = f.read()
        f.close()
        hasil = base64.encodestring(l)
        temp.append(hasil.decode())
        return hasil

    def list_files(self):
        file_list = os.listdir("files")
        f = []
        for filename in file_list:
            f.append(filename)
        return f

if __name__=='__main__':
    f = File()