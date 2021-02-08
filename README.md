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

**Teammates**: [Ryan's GitHub](https://github.com/ryan9411 "Ryan's GitHub") & [Abrahams's GitHub](https://github.com/yatfungleung "Abrahams's GitHub")

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

![alt text](https://github.com/azwinlam/UberEats-Analysis/blob/main/figures/head.png "Head")


* For Name, I had to strip the Chinese characters and remove (AREA) from the string
* Delivery Fee - extracted integer from string
* Food Type - used regex to extract the cuisine into a list, then picked the first one as the dominant cuisine
* Rating - extracted float from string
* Reviews - extracted int from string
* Menu Items - not used in analysis, counted number of items to divide total price to get average price per menu item
* Menu Prices - summed all the prices and divded by number of menu items to get average price per menu item
* Dollar Sign Rating - extracted from Food Type column

## EDA (Exploratory Data Analysis)

Below are the highlights from the EDA:

### These are the dollar sign ratings from UberEats
![alt text](https://github.com/azwinlam/UberEats-Analysis/blob/main/figures/dollarsignrating.png "Dollar Sign Ratings")


### Dollar Sign Ratings versus Average Price
* Excluding outliers, the Dollar Sign suggestions on UberEats do not definitively separate price ranges. With the exception of $$$$ being significantly pricier than the other 3.![alt text](https://github.com/azwinlam/UberEats-Analysis/blob/main/figures/Dollarsign_vs_AveragePrice.png "Dollar Sign Ratings vs Average Price")

### Reviews vs Ratings
* Ratings were fairly consistent across No of Reviews. No conclusions can be made on validity of Ratings. The IQR narrows with more reviews as expected

![alt text](https://github.com/azwinlam/UberEats-Analysis/blob/main/figures/ReviewCounts_Vs_Ratings.png "Reviews vs Ratings")

### Cuisine Counts
* Asian cuisines dominate the area as expected for the demographics.
![alt text](https://github.com/azwinlam/UberEats-Analysis/blob/main/figures/cuisineCounts.png "Cuisine Counts")

### Delivery Costs
* 2 Outliers with 29 dollars for delivery. They are located in Wanchai (Further away from Tin Hau area) so distance is probably a factor.
![alt text](https://github.com/azwinlam/UberEats-Analysis/blob/main/figures/DeliveryCostCounts.png "Delivery Costs")

#### My parters compared Deliveroo and foodpanda. Unfortunately, Deliveroo had very few restaurant over lap with UberEats and foodpanda. I will focus on UberEats X foodpanda.

### UberEats vs foodpand Price Differences
* Aside from the extreme outliers caused by missing data. UberEats costs more than foodpanda in the Tin Hau area for most restaurants.
![alt text](https://github.com/azwinlam/UberEats-Analysis/blob/main/figures/UberEatXPanda%20Price%20Difference.png "Price Differences")

### UberEats vs foodpand Delivery Fee Differences
* Aside from the extreme outliers caused by missing data. UberEats costs more than foodpanda in the Tin Hau area for most restaurants.
![alt text](https://github.com/azwinlam/UberEats-Analysis/blob/main/figures/UberEatXPanda%20Delivery%20Difference.png "Delivery Fee Differences")

## EDA Conclusion
* Order from foodpanda if restaurants are on both platforms (UberEats). 
* You will save $25 per à la carte on average with food panda.
* You will save $3 on delivery fees on average with food panda.
* Buy from food panda in Tin Hau Area. (Feb 2021)

## Business Applications
* Food scanner app can help consumers find the best price across three food delivery platform
