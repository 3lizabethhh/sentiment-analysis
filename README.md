# sentiment-analysis
## Description
Analyzes twitter data and determines which timezone is the "happiest" using file input and output, data structures,text processing,loops etc..

## Prerequisites
PyCharm

## Notable Files
tweets.txt etc.. contain tweets from the US
key1.txt etc.. contains the keywords and their happiness score

## How Program Works
The Twitter data contains comments from individuals about how they feel about their
lives and comes from individuals across the continental United States.This program analyzes each individual tweet to determine a score – a “happiness score”. The program stores the happiness score into a group then finds the sum of the scores and compares the sums to find the "happiest" timezone.

## What is a "happiness score"
The “happiness score” for a single tweet is found by looking for certain keywords (which are given) in a tweet and for each keyword found in that tweet totaling their “sentiment values”.  In this program, each value is an integer from 1 to 10.  The happiness score for the tweet is simply the sum of the “sentiment values” for keywords found in the tweet divided by the number of keywords found in the tweet.  If there are none of the given keywords in a tweet, it is just ignored.

## Timezones
Given a latitude and longitude, the task of determining exactly the location that it corresponds
to can be very challenging given the geographical boundaries of the United States.  For this
assignment, we simply approximate the regions corresponding to the timezones by rectangular
areas defined by latitude and longitude points.  Our approximation looks like:
p9________________________p7  ________________________p5________________________p3________________________p1
|\\\\\\\\\\\\\Pacific\\\\\\\\\\\\\\|\\\\\\\\\\\\\\\\\\Mountain\\\\\\\\\|\\\\\\\\\\\\\\Central\\\\\\\\\\\\|\\\\\\\\\\\\Eastern\\\\\\\\\\|
p10________________________p8________________________p6________________________p4________________________p2                          

_p1_   =  (49.189787, ‐67.444574)
_p2_   =  (24.660845, ‐67.444574)
_p3_   =  (49.189787, ‐87.518395)
_p4_   =  (24.660845, ‐87.518395)
_p5_   =  (49.189787, ‐101.998892)
_p6_   =  (24.660845, ‐101.998892)
_p7_   =  (49.189787, ‐115.236428)
_p8_   =  (24.660845, ‐115.236428)
_p9_   =  (49.189787, ‐125.242264)
_p10_ =  (24.660845, ‐125.242264)

