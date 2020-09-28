import json
import urllib.request
from datetime import datetime
from pytz import timezone
from termcolor import colored

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
with urllib.request.urlopen(url) as response:
    content = json.loads(response.read().decode())

nowDateTime = datetime.now(timezone('US/Pacific'))
print("Current PST time:" + nowDateTime.strftime("'%Y-%m-%d %H:%M:%S'"))
for k in content["Time Series (5min)"].keys():
    #we need timezone for the math to work, but this will also move the date by seven hours
    #to compensate for this, we will add those 7 hours back
    currDateTime = datetime.strptime(k, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone('US/Pacific')) # + timedelta(hours=7)
    
    datetimeDelta = nowDateTime - currDateTime
    datetimeDeltaInHrs = datetimeDelta.days * 24 + int(round(datetimeDelta.seconds / 3600))
    itemsShown = 0
    #print(currDateTime.strftime("%Y-%m-%d %H:%M:%S") + " " + str(datetimeDeltaInHrs))
    delta = 1 #just for test as it's over weekend so last quote was more than 48 hours ago
    if datetimeDeltaInHrs <= delta:
        content["Time Series (5min)"][k]["4. close"]
        itemsShown += 1

if itemsShown == 0:
    print(colored("No quotes from last hour found.", 'red'))

