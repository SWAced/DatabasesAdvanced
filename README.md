# Bitcoin data scraper

**In this assignment we will be scraping data off the Blockchain website (https://www.blockchain.com/btc/unconfirmed-transactions) and using this data to find the best USD value hash. This assignment is part of the Databases Advanced course, and will gradually evolve as I will be working on it every week, improving the project as intended. Since the programme will get heavier every week, I recommend you run this on a Virtual Machine. The one I will be using is Linux Ubuntu on Virtual Box.**

To use this scraper, you will need to have the following libraries:
- BeautifulSoup (bs4)
- Requests
- Pandas
- Math
- Time

**To install these libraries, you will need python3 (as you might have guessed, considering this is written in python) and you will use the following command to install the libraries:**

*pip3 install (library)*

*E.g. pip3 install bs4*

**You need to make sure you have Python installed.**

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
