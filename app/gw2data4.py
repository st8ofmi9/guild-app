import time
import requests
import datetime
import logging
from pathlib import Path


class gw2data:

    loglocation = "/home/pi/gw2data.log"
    lfmt = "%(asctime)s %(message)s"
    dfmt = "%m/%d/%Y %I:%M:%S %p"
    llvl = logging.DEBUG
    logging.basicConfig(filename=loglocation, format=lfmt, datefmt=dfmt, level=llvl)
    results = []

    def __init__(self, apikey=None):
        self.apikey = apikey
        self.auth = {'Authorization':'Bearer {}'.format(self.apikey)}
        self.url = "https://api.guildwars2.com/v2/"
    
    def apicall(self, call, limit=0, obj_list=None):
        "This Function is to streamline API calls using Python"
        call_type = call
        search_url = "{}{}".format(self.url, call_type)
        obj_id = requests.get(search_url, headers=self.auth).json()
        logging.debug("Object Id is: {}".format(obj_id))
        logging.debug("Object Id length is: {}".format(len(obj_id)))
        obj_list = []
        i = 0
        logging.info("i = {}, and limit = {}".format(i, limit))
        if float(limit) == 1:
            obj_list = obj_id
            #break
        elif float(limit)!= 1:
            logging.debug("Running If Successful Clause")
            logging.debug("{} <= {} is {}".format(i, limit, i <= limit))
            for id in obj_id:
                pop_request = requests.get(str(search_url)+"/"+str(id)).json()
                obj_list.extend([pop_request])
                logging.info("Get Response is {}".format(pop_request))
                try:
                    logging.debug("{}. {}".format(i+1, obj_list[i]["name"]))
                except(KeyError):
                    logging.info("Key: Name does not exist")
                time.sleep(1.5)
                i = i+1
                if i >= limit:
                    break
        elif float(limit) == 0:
            logging.critical("no limit selected, retriving all results")
            for id in obj_id:
                pop_request = requests.get(str(search_url)+"/"+str(id)).json()
                obj_list.extend([pop_request])
                logging.info("Get Response is {}".format(pop_request))
                try:
                    logging.debug("{}. {}".format(i+1, obj_list[i]["name"]))
                except(KeyError):
                    logging.info("Key: Name does not exist")
                time.sleep(1.5)
                i = i+1
        gw2data.results = obj_list
        return obj_list
   
    def guildinfo(self, guild):
        call = "guild/search?name="
        rURL = self.url+call+guild
        r = requests.get(rURL)
        self.gid = r.json()
        

    def unpack_results(*results):
        i = 0
        while(int(i) < len(results)):
            for itm in results[0]:
                logging.info("i = {}".format(i))
                logging.info("itm = {}".format(itm))
                logging.info("results = {}".format(results[i]))
                logging.info("Results have a length of {}".format(len(results)))
                try:
                    print("{}: {}".format(itm, results[i][itm]))
                except(TypeError):
                    logging.critical("TypeError, try using *arg instead of arg")
                    print("TypeError, try using *arg instead of arg")
                    break
                except(KeyError):
                    logging.critical("Key: {} does not exist".format(itm))
                    print("Key: {} does not exist".format(itm))
                    break
            i = i+1