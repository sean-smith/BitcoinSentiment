BitcoinSentiment
================

Abstract
--------

This is a HackMIT 2014 project.

We're trying to predict bitcoin values based on sentiment on online communities. Our initial hypothesis is that based on good or bad news in online forums bitcoin prices rise and fall. So by looking at existing data we are trying to find a correlation.

We were inspired by the work of Peter Gloor and Jermain Kaminski on how twitter posts effect bitcoin value. You can read their work here: http://humancomputation.com/ci2014/papers/Active%20Papers%5CPaper%2048.pdf

Methodology
-----------

We Used the Idol On Demand api: http://www.idolondemand.com/developer/apis from HP to determine aggregate sentiment. The sentiment is a value between -1 and 1, 1 being "I LOVE BITCOIN" to -1 being "SELL YOUR BITCOIN NOW". Each post over the historical data was summed to get a daily correct value. Our data was taken from the reddit bitcoin community. 

The historical bitcoin prices were retreived from the coinbase API: https://www.coinbase.com/docs/api/overview

Results
-------

The initial data is messy. When compared to the graph of bitcoin value, a clear correlation is not evident.

![Alt text](https://raw.githubusercontent.com/sean-smith/BitcoinSentiment/master/Screen%20Shot%202014-10-08%20at%202.44.59%20PM.png "Graph of Bitcoin Value")
![Alt text](https://raw.githubusercontent.com/sean-smith/BitcoinSentiment/master/Screen%20Shot%202014-10-08%20at%202.40.24%20PM.png "Graph of Bitcoin Sentiment")

So we Cleaned up the data by applying a filter:
![Alt text](https://raw.githubusercontent.com/sean-smith/BitcoinSentiment/master/sentiment_average.png "Averaged Sentiment")


Data
----

Feel free to use our data. There are two text files that have json data dumped straight in them. Or you can use the csv file if you'd like an easier file format. Please attribute your work to this github repo.

