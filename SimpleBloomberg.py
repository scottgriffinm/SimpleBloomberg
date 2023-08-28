import blpapi
import csv
'''
SimpleBloomberg: A simple wrapper for the Bloomberg API

Written by Scott Griffin
scottgriffinm@gmail.com
'''

def __startSession():
    d_host = 'localhost'
    d_port = 8194
    sessionOptions = blpapi.SessionOptions()
    sessionOptions.setServerHost(d_host)
    sessionOptions.setServerPort(d_port)
    session = blpapi.Session(sessionOptions)
    session.start()
    return session

def saveToCSV(data, filename):
    '''
    :param data: dictionary of lists, each list is a column of data
    :param filename: string, name of file to save to
    '''
    with open(filename, mode='w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data.keys())
        for row in zip(*data.values()):
            writer.writerow(row)
    
def getHistoricalPrices(securities, start_date, end_date, frequency, fields='PX_LAST'):
    '''
    :param securities: string or list of strings in format TICKER EXCHANGE ex: 'IBM US Equity'
    :param start_date: string in format YYYYMMDD
    :param end_date: string in format YYYYMMDD
    :param frequency: string in 'DAILY', 'WEEKLY', 'MONTHLY', 'QUARTERLY', 'SEMI_ANNUALLY', 'YEARLY'
    :param fields: list of strings, type of price data to get from bloomberg
    '''
    assert frequency in ['DAILY', 'WEEKLY', 'MONTHLY', 'QUARTERLY', 'SEMI_ANNUALLY', 'YEARLY']
    session = __startSession()
    session.openService('//blp/refdata')
    refDataService = session.getService('//blp/refdata')
    request = refDataService.createRequest('HistoricalDataRequest')
    if type(securities) == str:
        securities = [securities]
    for security in securities:
        request.getElement('securities').appendValue(security)
    if type(fields) == str:
        fields = [fields]
    for field in fields:
        request.getElement('fields').appendValue(field)
    request.set('periodicitySelection', frequency)
    request.set('startDate', start_date)
    request.set('endDate', end_date)
    session.sendRequest(request)
    data = {}
    while True:
        event = session.nextEvent()
        for msg in event:
            if msg.messageType() == 'HistoricalDataResponse':
                dates = []
                prices = []
                securityData = msg.getElement('securityData')
                fieldData = securityData.getElement('fieldData')
                for element in fieldData:
                    dates.append(element.getElementAsString('date'))
                    prices.append(element.getElementAsFloat('PX_LAST'))
                if 'dates' not in data.keys():
                    data['Date'] = dates
                data[securityData.getElementAsString('security') + ' Price'] = prices
        if event.eventType() == blpapi.Event.RESPONSE:
            break

    return data
