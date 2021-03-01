from bs4 import BeautifulSoup
import requests
import pandas as pd
import math
import time
import pymongo as mongo
import redis

r = redis.Redis()

hashes = map(str, r.lrange("Hash", 0, -1))
times = map(str, r.lrange("Time", 0, -1))
btc = map(float, r.lrange("Bitcoin value", 0, -1))
dollar = map(float, r.lrange("Dollar value", 0, -1))

print(hashes)