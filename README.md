# Bitcoin data scraper

**In this assignment we will be scraping data off the Blockchain website (https://www.blockchain.com/btc/unconfirmed-transactions) and using this data to find the best USD value hash. This assignment is part of the Databases Advanced course, and will gradually evolve as I will be working on it every week, improving the project as intended. Since the programme will get heavier every week, I recommend you run this on a Virtual Machine. The one I will be using is Linux Ubuntu on Virtual Box.**

To use this scraper, you will need to have the following libraries:
- BeautifulSoup (bs4)
- requests
- pandas
- math
- time
- pymongo

**To install these libraries, you will need python3 (as you might have guessed, considering this is written in python) and you will use the following command to install the libraries:**

*pip3 install (library)*

*E.g. pip3 install bs4*

**You need to make sure you have Python installed.**

**Before we run the script, we need to make sure that MongoDB is properly set up on our Linux machine. On Windows, it is quite simple since you can just download MongoDB from the site and then use MongoDB Compass to have a visualiser. However, on Linux things are different. Here are steps to install MongoDB on Linux:**

**Step 1:**

wget -q0 - https://www.mongodb.org/static/pgp/server -4.2.asc | sudo apt-key add -

**Step 2:**

echo "deb [ arch=amd64, arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org -4.2.list

**Step 3:**

sudo apt-get update

sudo apt-get install -y mongodb-org

**Step 4:**

sudo systemctl start mongod

sudo systemctl status mongod

*You can run the status command above to check if your mongod is running.*

**Step 5:**

cd <mongodb installation dir>/bin

mongo

mongodb://127.0.0.1:27017

**Optional Step 6:**

*You can use this step if you wish to create a user with root privileges in your database. Note that the "superuser" and "pass" are just examples for username and password respectively. The password "pass" should never be used as password.*

mongo --host HOST --port PORT

use admin

db.createUser(
  {
  user: "superuser",
  pws: "pass",
  roles: ["root"]
  }
)

show users
db.shutdownServer()
exit

mongod --auth

<br>
<br>

<h1>Now you can run the script using the following steps below.</h1>

**Step 1:**

You can clone my repository using the following command:
<br>
<code>git clone https://github.com/SWAced/DatabasesAdvanced.git</code>
<br>

**Step 2:**
On Linux, you have to make the script executable in order for it to execute. To do this, using the following command:
<br>
<code>chmod +x scraper.py</code>
<br>

**Step 3:**
Assuming you already have Python installed, you can use the following command to run the script:
<br>
<code>python3 scraper.py</code>
