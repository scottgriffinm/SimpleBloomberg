# SimpleBloomberg.py

A simple wrapper for the Bloomberg Terminal API, currently can only retrieve historical prices.

Quickstart:

(1) On a computer with Bloomberg Terminal open, install the Bloomberg Python API in a command prompt:

```
python -m pip install --index-url=https://bcms.bloomberg.com/pip/simple blpapi
```

(2) Create a Python script in the same folder as SimpleBloomberg.py and paste the following code:

```
import SimpleBloomberg as sb
# get IBM & AAPL daily closing prices for the period of 4/27/2010 to 5/1/2010 and save to csv
data = sb.getHistoricalPrices(['IBM US Equity','AAPL US Equity'], '20100427', '20100501', 'DAILY', fields='PX_LAST')
sb.saveToCSV(data,'data.csv')
```

(3) Run your Python script.
