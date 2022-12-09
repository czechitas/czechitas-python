import sys
import platform
import urllib2
import json

# function called by server to return response
# Simple explanation how it works:
# Instead of printing to screen it "prints" back to web browser
def application(environ, start_response):
    # HTTP basic header
    start_response(b'200 OK', [(b'Content-Type', b'text/html')])
    
    API = 'https://api.csas.cz/sandbox/webapi/api/v1/exchangerates'
    # To get key go to https://developers.csas.cz/html/devs/
	KEY = 'xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
    
    req = urllib2.Request(API)
    # HTTP header
    req.add_header('WEB-API-key', KEY)
    resp = urllib2.urlopen(req)
    
    if (resp.getcode() != 200):
        yield "No exchange rates"
        exit()
    
    # get response in JSON format
    content = resp.read()
    
    # convert response from JSON to array of dictionaries
    rates = json.loads(content) 
    # imagine yield as print(very, very simple imagination)
    # https://docs.python.org/2/reference/simple_stmts.html#the-yield-statement
    yield '<h1>CSAS Exchange Rates</h1>'
    yield '<table>\r\n'
    for rate in rates:
        yield f"<tr><td>{rate['shortName']}</td><td align='right'>{rate['currBuy']}</td><td align='right'>{rate['currSell']}</td></tr>\r\n"
    yield '</table>\r\n'
