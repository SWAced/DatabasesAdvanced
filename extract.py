from bs4 import BeautifulSoup
import requests
import pandas as pd
import math
import time
import pymongo as mongo
import redis

r = redis.Redis()

hashes = r.lrange("Hash", 0, -1)
times = r.lrange("Time", 0, -1)
btc = r.lrange("Bitcoin value", 0, -1)
dollar = r.lrange("Dollar value", 0, -1)

print(hashes)