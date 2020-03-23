from file_control import File
import json
import logging

f = File()

class FileMachine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("upload")
                namafile = cstring[1].strip()
                isifile = cstring[2].strip()
                f.upload_file(namafile,isifile.encode())
                return "OK"
            elif (command=='download'):
                logging.warning("download")
                namafile = cstring[1].strip()
                hasil = f.download_file(namafile)
                return hasil[0]
            elif (command=='list'):
                logging.warning("list")
                namafile = f.list_files()
                hasil = {"filename":namafile}
                return json.dumps(hasil, indent=4)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    fm = FileMachine()
    # hasil = fm.proses("list")
    print(hasil)
