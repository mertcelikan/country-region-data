import schedule
import time
from worker import *

# Can add more countries
countries = ["TR", "US"]

while True:
    for x in countries:
        print("!!! Started !!!")
        getCountryInfo(x)
        time.sleep(2)
        getRegionsInfo(x)
        time.sleep(2)

    # time.sleep(3600) Can work every hour / We can also use schedule library to schedule works.
