import os
import json
from pymongo import MongoClient

# 
class MongoCartographer(object):
    @classmethod
    def __init__(cls, link):
        cls.client = MongoClient(f"""{link}""")
    @classmethod
    def push(cls, rootdir):
        for dir, subdirs, files in os.walk(os.path.abspath(rootdir)):
            for file in files:
                if len(dir.split(os.sep)) > 2:
                    with open(os.path.join(dir, file), 'r') as datafile:
                        jsondata = json.load(datafile)
                        database = f"{dir.split(os.sep)[-2]}"
                        collection = f"{dir.split(os.sep)[-1]}"
                        if cls.client[database][collection].find({'_id': f"{file.split('.')[0]}", 'data': jsondata}).count() == 0:
                            cls.client[database][collection].insert({'_id': f"{file.split('.')[0]}", 'data': jsondata})
                            print("OK")
                        else:
                            print("Record Already Exists")
