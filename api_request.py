__author__ = 'SeanSmith'


from pprint import pprint
import requests, json
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#Format
#{"importance": 0-10, "sentiment": positive/negative/neutral, "score":0-1}
#

def get_sentiment(text):
    r = requests.get("https://api.idolondemand.com/1/api/sync/analyzesentiment/v1?apikey=fe6dea49-084f-4cd8-be86-0976baf9a714&text="+str(text))

    if(r.status_code == 200):
        #print(r.text)
        data2 = json.loads(r.text)
        #pprint(data2)

        return data2['aggregate']['score']
    else:
        print("Error return code = "+r.status_code)




def get_text(url):
    dlst = []
    driver = webdriver.Firefox()
    driver.get(url)
    the_table = driver.find_element_by_id("siteTable")
    elements = the_table.find_elements_by_tag_name("div")
    print(elements)
    for element in elements:
        if(len(element.find_elements_by_class_name("title"))>0):
            text = element.find_element_by_class_name("title").text
            print(text)
            dlst += [text]

    driver.quit()
    return dlst



counter= 0

text = get_text("http://www.reddit.com/r/Bitcoin/")
print(text)
for each in text:
    counter += get_sentiment(each)

print(counter)
