import json
from TweetsBank import tweetsBank;

#####################################
# python tweetsData.py              #
#   - total tweets seen             #
#   - least predictable tweets      #
#   - most predictable tweets       #
#   - least predictable streamers   #
#   - most predictable streamers    #
#   - streamers to correct rate (%) #
#####################################

# Opening JSON files
tweetIdsJSON = open('./tweetIds.json')
tweetIds = json.load(tweetIdsJSON)

# Generate tweetId : name mapping
tweetToName = dict()
for id in tweetsBank:
    tweetToName[id] = tweetsBank[id]["name"]

totalTweetsSeen = 0

tweetToRate = dict() # tweetId : correct % mapping
nameToRate = dict() # name : correct % mapping
for id in tweetIds:
    guessesCorrect = 0
    guessesTotal = 0
    for name in tweetIds[id]:
        guessesTotal += tweetIds[id][name]
        if name == tweetToName[id]:
            guessesCorrect = tweetIds[id][name]
            if name not in nameToRate:
                nameToRate[name] = [0,0]
            nameToRate[name][0] += guessesCorrect
    tweetToRate[id] = guessesCorrect / guessesTotal
    nameToRate[tweetToName[id]][1] += guessesTotal
    totalTweetsSeen += guessesTotal

print("Total tweets seen:", totalTweetsSeen)

sortedTweetToRate = dict(sorted(tweetToRate.items(), key=lambda item: item[1]))
leastPredictableTweets = list(sortedTweetToRate.keys())[:3]
mostPredictableTweets = list(sortedTweetToRate.keys())[-3:][::-1]
print("Least predictable tweets:")
for id in leastPredictableTweets:
    print(tweetToName[id] + ":", tweetsBank[id]["text"], sortedTweetToRate[id])
    bait = ""
    baitCount = 0
    guessesTotal = 0
    for name in tweetIds[id]:
        guessesTotal += tweetIds[id][name]
        if baitCount < tweetIds[id][name]:
            bait = name
            baitCount = tweetIds[id][name]
    print("baited by:", bait, baitCount/guessesTotal)
print("Most predictable tweets:")
for id in mostPredictableTweets:
    print(tweetToName[id] + ":", tweetsBank[id]["text"], sortedTweetToRate[id])

for name in nameToRate:
    nameToRate[name] = nameToRate[name][0] / nameToRate[name][1]
sortedNameToRate = dict(sorted(nameToRate.items(), key=lambda item: item[1]))
leastPredictableStreamers = list(sortedNameToRate.keys())[:4]
mostPredictableStreamers = list(sortedNameToRate.keys())[-4:][::-1]
print("Least predictable streamers:", leastPredictableStreamers)
print("Most predictable streamers:", mostPredictableStreamers)
print("Streamers to correct %", sortedNameToRate)





