import json
import urllib.request
from datetime import datetime
from pytz import timezone
from termcolor import colored

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
with urllib.request.urlopen(url) as response:
    content = json.loads(response.read().decode())

quotesTZ = content['Meta Data']['6. Time Zone']
nowDateTime = datetime.now(timezone(quotesTZ))

print("Current " + quotesTZ + " time:" + nowDateTime.strftime("%Y-%m-%d %H:%M:%S"))
for k in content["Time Series (5min)"].keys():
    currDateTime = datetime.strptime(k, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone(quotesTZ))
    
    datetimeDelta = nowDateTime - currDateTime
    datetimeDeltaInHrs = datetimeDelta.days * 24 + int(round(datetimeDelta.seconds / 3600))
    itemsShown = 0
    delta = 1 
    if datetimeDeltaInHrs <= delta:
        content["Time Series (5min)"][k]["4. close"]
        itemsShown += 1

if itemsShown == 0:
    print(colored("No quotes from last hour found.", 'red'))

