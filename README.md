BitcoinSentiment
================

Abstract
--------

This is a HackMIT 2014 project.

We're trying to predict bitcoin values based on sentiment on online communities. Our initial hypothesis is that based on good or bad news in online forums bitcoin prices rise and fall. So by looking at existing data we are trying to find a correlation.

Methodology
-----------

We Used the Idol On Demand api: http://www.idolondemand.com/developer/apis from HP to determine aggregate sentiment. The sentiment is a value between -1 and 1, 1 being "I LOVE BITCOIN" to -1 being "SELL YOUR BITCOIN NOW". Each post over the historical data was summed to get a daily correct value. 

The historical bitcoin prices were retreived from the coinbase API: https://www.coinbase.com/docs/api/overview



