# SimpleBloomberg.py

A simple wrapper for the Bloomberg Terminal API, it currently can only retrieve historical prices.

Quickstart:

(1) On a computer with Bloomberg Terminal open, install the Bloomberg Python API in a command prompt:

```
pip install blpapi
```

(2) Create a Python script in the same folder as SimpleBloomberg.py and paste the following code:

```
import SimpleBloomberg as sb
# get IBM & AAPL daily closing prices for the period of 4/27/2010 to 5/1/2010
data = sb.getHistoricalPrices(['IBM US Equities','AAPL US Equities'], '20100427', '20100501', 'DAILY', fields='PX_LAST')
```
