import requests
import urllib
import urllib2
token = '25D26255F6924F31BD86503A4253BEA0'
start = '9/1/2015'
end = '9/18/2015'
arr = ['GOOG']

def queryStock(stockArray, startDate, endDate):
    result = [];
    for stock in stockArray:
        url='http://ws.nasdaqdod.com/v1/NASDAQAnalytics.asmx/GetEndOfDayData'
        data = {'_Token' : '%s' % token,
        'Symbols' : '%s' % stock,
        'StartDate' : '%s' % startDate,
        'EndDate' : '%s' % endDate,
        'MarketCenters' : '' }
        r = requests.get(url, data = data)
        result += r.text
        return r.text

queryStock(arr, start, end)
