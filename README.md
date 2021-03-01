# Bitcoin data scraper

**In this assignment we will be scraping data off the Blockchain website (https://www.blockchain.com/btc/unconfirmed-transactions) and using this data to find the best USD value hash. This assignment is part of the Databases Advanced course, and will gradually evolve as I will be working on it every week, improving the project as intended. Since the programme will get heavier every week, I recommend you run this on a Virtual Machine. The one I will be using is Linux Ubuntu on Virtual Box.**

To use this scraper, you will need to have the following libraries:
- BeautifulSoup (bs4)
- requests
- pandas
- math
- time
- pymongo
- redis

**To install these libraries, you will need python3 (as you might have guessed, considering this is written in python) and you will use the following command to install the libraries:**

*pip3 install (library)*

*E.g. pip3 install bs4*

**You need to make sure you have Python installed.**

**Before we run the script, we need to make sure that MongoDB and Redis are properly set up on our Linux machine. On Windows, it is quite simple since you can just download MongoDB from the site and then use MongoDB Compass to have a visualiser. However, on Linux things are different. Here are steps to install MongoDB and Redis on Linux.**

**Step 1:**

First, download the .sh files.

**Step 2:**

Then, open the command line and type the following commands:

<code>chmod +x mongodbinst.sh</code>
<code>chmod +x redis.sh</code>

**Step 3:**

To run the scripts, you use the following command:

<code>bash mongodbinst.sh</code>
<code>bash redis.sh</code>

Now the script will automatically install mongodb and redis and make it active, so you can run the scraper & extraction without issues.

<br>
<br>

# To run the python files, follow the steps below.

**Step 1:**

You can clone my repository using the following command:
<br>
<code>git clone https://github.com/SWAced/DatabasesAdvanced.git</code>
<br>

**Step 2:**
On Linux, you have to make the scripts executable in order for them to execute. To do this, use the following command:
<br>
<code>chmod +x scraper.py</code>
<code>chmod +x extract.py</code>
<br>

**Step 3:**
Assuming you already have Python installed, you can use the following command to run the script:
<br>
<code>python3 scraper.py</code>
<code>python3 extract.py</code>
