from sys import exit
from lxml import html
import requests
import re

weather_type = {"today": "2day", "hourbyhour": ["hour", "hourly", "hour by hour"], "5day": "five day", "weekend": "wknd", "tenday": "10 day"}

def start():
    print("Let's look at the weather for Sunnyvale, CA.")
    weather()

def weather():
    print("What weather forecast time period are you interested in?")
    print("Today, hour by hour, 5 day, weekend, or 10 day?")
    choice = input("> ")

    #dictionary for normalizing user input
    rep = {
        " ": "",
        "2day": "today",
        "hour": "hourbyhour",
        "hourly": "hourbyhour",
        "five": "5day",
        "5": "5day",
        "ten": "tenday",
        "10": "tenday",
        "10 day": "tenday",
        "s":"",
        "wknd": "weekend",
    }

    #normalize user input
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], choice.lower())

    link = "https://weather.com/weather/" + text +"/l/USCA1116:1:US"
    page = requests.get(link)
    tree = html.fromstring(page.content)

    if text == "today":
        print("Sunnyvale, CA Today's Weather")
        current = tree.xpath('//div[@class="today_nowcard-temp"]/span/text()')
        feels =  tree.xpath('//span[@classname="deg-feels"]/text()')
        high = tree.xpath('//div[@class="today_nowcard-hilo"]/span[2]/span/text()')
        low = tree.xpath('//div[@class="today_nowcard-hilo"]/span[5]/span/text()')
        print ("The current temperature is " +
            str(current).replace('[\'','').replace('\']','') + "°F with a high of " +
            str(high).replace('[\'','').replace('\']','') + "°F and a low of " +
            str(low).replace('[\'','').replace('\']','') + "°F.",
            "It feels like " + str(feels).replace('[\'','').replace('\']','') + "°F.")
        restart()

    elif text == "tenday":
        location = tree.xpath('//h1[@class="h2"]/text()')
        print (str(location).replace('[\'','').replace('\']',''))
        number = range(1, 11)
        for x in number:
            day_path = '//*[@id="twc-scrollabe"]/table/tbody/tr[' + str(x) + ']/td[2]/div/span/text()'
            high = '//*[@id="twc-scrollabe"]/table/tbody/tr[' + str(x) + ']/td[4]/div/span[1]/text()'
            low = '//*[@id="twc-scrollabe"]/table/tbody/tr[' + str(x) + ']/td[4]/div/span[3]/text()'
            day = tree.xpath(day_path)
            high_temp = tree.xpath(high)
            low_temp = tree.xpath(low)
            print (str(day).replace('[\'','').replace('\']',''),
                "High:", str(high_temp).replace('[\'','').replace('\']','') + "°F",
                "Low:", str(low_temp).replace('[\'','').replace('\']','') + "°F")
        restart()

    elif text == "hourbyhour":
        location = tree.xpath('//h1[@class="h2"]/text()')
        print (str(location).replace('[\'','').replace('\']',''))
        number = range(1, 17) #should go up to 25 but can't figure out how to get the elements hidden under collapsed menu
        for x in number:
            time_path = '//*[@id=\"twc-scrollabe\"]/table/tbody/tr[' + str(x) + ']/td[2]/div/div[1]/span/text()'
            time = tree.xpath(time_path)
            print(str(time).replace('[\'','').replace('\']',''))
        restart()

    elif text == "5day":
        location = tree.xpath('//h1[@class="h2"]/text()')
        print (str(location).replace('[\'','').replace('\']',''))
        number = range(1, 6)
        for x in number:
            day_path = '//*[@id="twc-scrollabe"]/table/tbody/tr[' + str(x) + ']/td[2]/div/span/text()'
            high = '//*[@id="twc-scrollabe"]/table/tbody/tr[' + str(x) + ']/td[4]/div/span[1]/text()'
            low = '//*[@id="twc-scrollabe"]/table/tbody/tr[' + str(x) + ']/td[4]/div/span[3]/text()'
            day = tree.xpath(day_path)
            high_temp = tree.xpath(high)
            low_temp = tree.xpath(low)
            print (str(day).replace('[\'','').replace('\']',''),
                "High:", str(high_temp).replace('[\'','').replace('\']','') + "°F",
                "Low:", str(low_temp).replace('[\'','').replace('\']','') + "°F")
        restart()

    elif text == "weekend":
        location = tree.xpath('//h1[@class="h2"]/text()')
        print (str(location).replace('[\'','').replace('\']',''))
        number = range(1, 4)
        for x in number:
            day_path = '//*[@id="twc-scrollable"]/article/div/div/div[' + str(x) + ']/section/header/h3/text()'
            day = tree.xpath(day_path)
            date_path = '//*[@id="twc-scrollable"]/article/div/div/div[' + str(x) + ']/section/header/span/span/text()'
            date = tree.xpath('' + date_path)
            high_path = '//*[@id="twc-scrollable"]/article/div/div/div[' + str(x) + ']/section/p[1]/span[1]/span/text()'
            high = tree.xpath('//*' + high_path)
            low_path = '//*[@id="twc-scrollable"]/article/div/div/div[' + str(x) + ']/section/p[1]/span[3]/span/text()'
            low = tree.xpath(low_path)
            print(str(day).replace('[\'','').replace('\']',''), str(date).replace('[\'','').replace('\']',''),
                "High: " + str(high).replace('[\'','').replace('\']','') + "°F",
                "Low: " + str(low).replace('[\'','').replace('\']','')  + "°F")
        restart()

    else:
        print("Sorry, that is not a valid time period. Please choose another time period.")
        weather()
    exit(0)

def restart():
    print("Would you like to find out more about Sunnyvale's weather?")
    text = input("> ")
    if text in ("y", "Y", "yes", "Yes"):
        weather()
    elif text in ("n", "N", "no", "No"):
        exit(0)
    else:
        print("Sorry, that is not a valid answer. Would you like to find out more about Sunnyvale's weather?")
        restart()

start()
