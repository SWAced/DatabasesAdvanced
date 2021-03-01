from bs4 import BeautifulSoup
import requests
import pandas as pd
import math
import time
import pymongo as mongo
import redis

client = mongo.MongoClient("mongodb://127.0.0.1:27017")

r = redis.Redis()

db = client["Cryptocurrency"]
col_crypto = db["Crypto"]

def eval_func(r, col):
    hashes = map(str, r.lrange("Hash", 0, -1))
    times = map(str, r.lrange("Time", 0, -1))
    btc = map(float, r.lrange("Bitcoin value", 0, -1))
    dollar = map(float, r.lrange("Dollar value", 0, -1))
    maxd = max(dollar)
    index = dollar.index(maxd)
    maxh = hashes[index]
    maxt = time[index]
    maxb = btc[index]
    crypto = {"Hash": maxh, "Time": maxt, "Bitcoin value": maxb, "Dollar value": maxd}
    col.insert_one(crypto)

    #print(hashes)

while True:
    eval_func(r, col_crypto)
    time.sleep(60)