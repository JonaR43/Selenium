"""from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.the-sun.com/sport/soccer/"
path ="D:/coding/freecodecamp/Selenium/chromedriver.exe"
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

#//div[@class='teaser__copy-container']
containers = driver.find_elements(by="xpath", value="//div[@class='teaser__copy-container']")

titles = []
subtitles = []
links=[]


for container in containers:
    title = container.find_element(by="xpath", value="./a/span").text #title
    subtitle = container.find_element(by="xpath", value="./a/h3").text #subtitle
    link = container.find_element(by="xpath", value="./a").get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline-headless.csv')

driver.quit()


#//div[@class='teaser__copy-container']/a/h3
#//div[@class='teaser__copy-container']/a/p"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os
from datetime import datetime
import sys


app_path = os.path.dirname(sys.executable)
now = datetime.now() #get date and time from OS
exec_date = now.strftime("%m%d%y")  #get time data into string mmddyy

# Define the website and path to the chromedriver
website = "https://www.the-sun.com/sport/soccer/"
path = "D:/coding/freecodecamp/Selenium/chromedriver.exe"

# Setup Chrome options for headless mode
options = Options()
options.add_argument("--headless=new") # for Chrome >= 109
#options.headless = True

# Initialize the WebDriver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

# Open the website
driver.get(website)

# Locate the containers for the articles
containers = driver.find_elements(by="xpath", value="//div[@class='teaser__copy-container']")

titles = []
subtitles = []
links = []

# Extract data from each container
for container in containers:
    try:
        title = container.find_element(by="xpath", value="./a/span").text  # Title
    except:
        title = "N/A"

    try:
        subtitle = container.find_element(by="xpath", value="./a/h3").text  # Subtitle
    except:
        subtitle = "N/A"

    try:
        link = container.find_element(by="xpath", value="./a").get_attribute('href')  # Link
    except:
        link = "N/A"

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Create a DataFrame and save to CSV
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)

file_name = f'headline-{exec_date}.csv'
final_path = os.path.join(app_path,file_name)
df_headlines.to_csv(final_path)

# Quit the WebDriver
driver.quit()



