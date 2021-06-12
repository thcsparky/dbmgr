import os
import json

class dbmgr:

    def saveAll(self):
        try:
            stringOut = json.dumps(self.dictContainer)
            a = open(self.filepath, 'w')
            a.write(stringOut)
            a.close()
            return('saved')
        except Exception as e:
            return(e)

    def reload(self):
        ##reloads, reparse, and return nothing if success
        try:
            a = open(self.filepath)
            b = a.read()
            a.close()

            self.dictContainer = json.loads(b)
            return('loaded: '  + self.filepath)
        except Exception as e:
            return(e)

    def __init__(self, filepath, dictContainer):
        self.filepath = filepath ##pass plaintext filename
        self.dictContainer = dictContainer ## pass an empty dictionary to this
        ##attempt load
        try:
            a = open(self.filepath)
            b = a.read()
            a.close()

            self.dictContainer = json.loads(b)
            return
        except Exception as e:
            return
