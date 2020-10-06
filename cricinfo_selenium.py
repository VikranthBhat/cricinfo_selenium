import time

import pandas as pd
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

coptions = Options()
coptions.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=coptions)

# print(driver.window_handles[0])
url = "https://www.espncricinfo.com/series/19859/commentary/1223944/australia-women-vs-new-zealand-women-1st-odi-nz-women-in-australia-2020-21"

# print(driver.title)
driver.get(url)
print(driver.title)

y = 0
last_height = 0

SCROLL_PAUSE_TIME = 0.5

# Get scroll height last_height = driver.execute_script("return document.body.scrollHeight")

while True:

    # Scroll down to bottom

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page

    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break
    else:
        last_height = new_height

outdf: DataFrame = pd.DataFrame()

overs, runs, bowler, batsman = list(), list(), list(), list()

for element in driver.find_elements_by_class_name("match-comment-over"):
    overs.append(float(element.text))
for element in driver.find_elements_by_class_name("match-comment-run"):
    runs.append(element.text)
for element in driver.find_elements_by_class_name("match-comment-short-text"):
    comment = element.text.split("to")
    print(comment)
    bowler.append(comment[0])
    batsman.append(comment[1].split(",")[0])

outdf["overs"] = overs
outdf["runs"] = runs
outdf["bowler"] = bowler
outdf["batsman"] = batsman

# driver.page_source
driver.quit()
outdf.replace(to_replace="•", value="0")
outdf.sort_values('overs')

print(outdf)

writer_obj = pd.ExcelWriter("Cricinfo.xlsx", engine='xlsxwriter')

outdf.to_excel(writer_obj, sheet_name='Sheet1')

writer_obj.save()
