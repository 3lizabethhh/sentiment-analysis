# This program analyzes key words in twitter posts around the world by calculating a sentiment score based on searching for keywords.
def compute_tweets(tweet, keyword):
    region_results_lst = []  # list of tuples for each timezone to be returned

    try:  # try block includes all the calculations and catches if the file being read does not exist

        # opens keyword file and tweet file
        tweet_file = open(tweet, "r", encoding="utf‐8")
        keyword_file = open(keyword, "r", encoding="utf‐8")

        # lists of happiness scores from tweets from each timezone (only tweets with keywords are added to lists)
        eastern = []
        central = []
        mountain = []
        pacific = []

        PUNC = "[]'.,;:!?#$@\""  # punctuations to be removed from tweets

        # collection of points that define timezones
        p1 = [49.189787, -67.444574]
        p2 = [24.660845, -67.444574]
        p3 = [49.189787, -87.518395]
        p4 = [24.660845, -87.518395]
        p5 = [49.189787, -101.998892]
        p6 = [24.660845, -101.99889]
        p7 = [49.189787, -115.236428]
        p8 = [24.660845, -115.236428]
        p9 = [49.189787, -125.242264]
        p10 = [24.660845, -125.242264]

        # Create dictionary of keywords
        keywordDict = {}
        for line in keyword_file:
            part = line.split(",")  # splits into [word]:[happiness value]
            keywordDict[part[0]] = int(
                part[1].strip("\n"))  # adds [word] as a key and sets [happiness value] as happiness value

        # Run through each tweet and classify/add the "happiness" of each tweet to the correct timezone list
        for line in tweet_file:  # reads a single tweet

            part = line.split(" ", 5)  # splits single tweet into list with [lat],[long],[value],[date],[time],[text]
            words = part[5].split()  # splits each tweet into words ( part[5] refers to [text in list of parts])

            lat = float(part[0].strip("[,]"))  # assigns latitude to variable for particular tweet
            long = float(part[1].strip("[,]"))  # assigns latitude to variable for particular tweet

            # pacific timezone
            if lat <= p9[0] and lat >= p10[0] and long >= p9[1] and long <= p7[1]:
                tweet_score = find_tweet_score(words, PUNC, keywordDict)
                if tweet_score != 0:  # if no keyword matches then disregard tweet
                    pacific.append(tweet_score)
            # mountain timezone
            elif lat <= p7[0] and lat >= p8[0] and long >= p7[1] and long <= p5[1]:
                tweet_score = find_tweet_score(words, PUNC, keywordDict)
                if tweet_score != 0:  # if no keyword matches then disregard
                    mountain.append(tweet_score)
            # central timezone
            elif lat <= p5[0] and lat >= p6[0] and long >= p5[1] and long <= p3[1]:
                tweet_score = find_tweet_score(words, PUNC, keywordDict)
                if tweet_score != 0:  # if no keyword matches then disregard
                    central.append(tweet_score)
            # eastern timezone
            elif lat <= p3[0] and lat >= p4[0] and long >= p3[1] and long <= p1[1]:
                tweet_score = find_tweet_score(words, PUNC, keywordDict)
                if tweet_score != 0:  # if no keyword matches then disregard
                    eastern.append(tweet_score)

            # ignores tweets that are not in specified timezones

        # creates tuples of [average,count] for each timezone
        east_tuple = (round(find_timezone_score(eastern), 2), len(eastern))
        cent_tuple = (round(find_timezone_score(central), 2), len(central))
        mount_tuple = (round(find_timezone_score(mountain), 2), len(mountain))
        pac_tuple = (round(find_timezone_score(pacific), 2), len(pacific))

        region_results_lst = [east_tuple, cent_tuple, mount_tuple, pac_tuple]

    except IOError:
        print("ERROR: Could Not Open File")

    finally:
        return (region_results_lst)  # returns list of tuples of resulting scores in order [Eastern,Central,Mountain,Pacific]


# finds the average "happiness value" for the given timezone and returns it
def find_timezone_score(timezone):
    hapscore = 0  # sets total count to zero

    # finds total happiness score of timezone
    for score in timezone:
        hapscore = hapscore + score

    try:  # catches Zero division error
        hapscore = hapscore / len(timezone)

    except ZeroDivisionError:
        hapscore = 0

    finally:
        return hapscore


# finds the "happiness score" of a particular tweet and returns the score
def find_tweet_score(words, PUNC, keywordDict):
    total_hap_score = 0  # counts total happiness score of tweet
    key_count = 0  # counts keywords found
    tweet_score = 0

    # check all words and add happiness score to find total happiness score
    for word in words:
        word = word.strip(PUNC).lower()  # takes off punctuation from ends
        if word in keywordDict:  # if the word in tweet is a keyword, add its value to this tweets happiness score
            key_count = key_count + 1
            total_hap_score = total_hap_score + keywordDict[word]

    if key_count != 0:  # if no keywords found, don't divide by zero and leave tweet score as 0
        tweet_score = total_hap_score / key_count

    return tweet_score
