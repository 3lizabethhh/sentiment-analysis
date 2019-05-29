# Dongzheng (Elizabeth) Xu
# This program helps us determine which timezone is the "happiest" by calling sentiment_analysis.py to calculate score
#  and displaying the results.


from SentimentAnalysis import sentiment_analysis
# prompts user to enter desired files
keyword_file = input("Please enter a keyword file:")
tweet_file = input("Please enter a tweet file:")

# calculates timezone happiness
region_result_lst = sentiment_analysis.compute_tweets(tweet_file, keyword_file)

if len(region_result_lst) != 0:  # if there are no values in list, do not display results bc error occurred
    print("The happiness score for Eastern is:{} and there are {} tweets.".format(region_result_lst[0][0],region_result_lst[0][1]))
    print("The happiness score for Central is:{} and there are {} tweets.".format(region_result_lst[1][0],region_result_lst[1][1]))
    print("The happiness score for Mountain is:{} and there are {} tweets.".format(region_result_lst[2][0],region_result_lst[2][1]))
    print("The happiness score for Pacific is:{} and there are {} tweets.".format(region_result_lst[3][0],region_result_lst[3][1]))
