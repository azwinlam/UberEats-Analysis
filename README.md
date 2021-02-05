# UberEats-Analysis

## Objective
* To scrape UberEats food delivery platform and compare the results with foodpanda

## Project Overview
* Scraped over 500 restaurants from the Tin Hua area in Hong Kong.
* Clean the data for analysis
* Provide findings
* Project Conclusion

## Code and Resources Used
**Python Version:** 3.9.1
**Packages:** pandas, numpy, matplotlib, seaborn, selenium, bs4, requests, requests-futures, regex

## Web Scraping
Copied and pasted some code from previous Job scraping projects. The following information was extracted from each restaurant:
* Name
* Delivery Fee
* Food Type
* Rating
* Reviews
* Menu Items
* Menu Prices

## Data Cleaning
Due to chinese characters from the restaurants, the file had to be opened with UTF-8 encoding. There was quite a bit of data cleaning before the data was usable.

* For Name, I had to strip the Chinese characters and remove (AREA) from the string
* Delivery Fee - extracted integer from string
* Food Type - used regex to extract the cuisine into a list, then picked the first one as the dominant cuisine
* Rating - extracted float from string
* Reviews - extracted int from string
* Menu Items - not used in analysis, counted number of items to divide total price to get average price per menu item
* Menu Prices - summed all the prices and divded by number of menu items to get average price per menu item
* Dollar Sign Rating - extracted from Food Type column

## EDA
