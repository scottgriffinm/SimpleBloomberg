# SimpleBloomberg.py

A simple wrapper for the Bloomberg Terminal Python API, currently only retrieves historical prices.

Quickstart:

(1) On your computer, open the Bloomberg terminal application and log in. Make sure to keep the application open throughout this process.

(2) Open the command line and install the Bloomberg Python API libraries:
```
python -m pip install --index-url=https://bcms.bloomberg.com/pip/simple blpapi
```

(3) Then clone this Github reposititory (or download it as a .zip and extract it to a folder):
```
git clone https://github.com/scottgriffinm/SimpleBloomberg.git
```

(4) Create a Python script in the same folder as SimpleBloomberg.py and paste the following code:
```
import SimpleBloomberg as sb
# get IBM & AAPL daily closing prices for the period of 4/27/2010 to 5/1/2010 and save to csv
data = sb.getHistoricalPrices(['IBM US Equity','AAPL US Equity'], '20100427', '20100501', 'DAILY', fields='PX_LAST')
sb.saveToCSV(data,'data.csv')
```

(5) Run your Python script.
