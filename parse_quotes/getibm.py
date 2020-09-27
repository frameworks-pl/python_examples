import json
import urllib.request
from datetime import datetime
from pytz import timezone

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
with urllib.request.urlopen(url) as response:
    content = json.loads(response.read().decode())

nowDateTime = datetime.now(timezone('US/Pacific'))
print(nowDateTime)
for k in content["Time Series (5min)"].keys():
    #we need timezone for the math to work, but this will also move the date by seven hours
    #to compensate for this, we will add those 7 hours back
    currDateTime = datetime.strptime(k, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone('US/Pacific')) + timedelta(hours=7)

    print(currDateTime)
    #print(nowDateTime + " " + currDateTime + " " + (nowDateTime - currDateTime).seconds/60)
    #print(content["Time Series (5min)"][k]["4. close"])





