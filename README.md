# Twitch Tweets Data
## A repo to provide open source data analytics of Twitch Tweets.


`scores.json` - a JSON mapping of `scores` to `# of times` score was attained; contains data from scores 0 to 64

`scoresSmall.json` - similar to `scores.json`, but for scores 0 to 10

`tweetIds.json` - a JSON mapping of `tweetId` to key-value pairs of `streamerName` to `# of times` name was guessed

`TweetsBank.py` - the bank of tweets used for Twitch Tweets (note: datetimes follow Pacifc Time; some datetimes are also still bugged)

`scoresData.py` - run `python scoresData.py` to print:
* total games played
* average score

`tweetsData.py` - run `python tweetsData.py` to print:
* total tweets seen
* least predictable tweets
* most predictable tweets
* least predictable streamers
* most predictable streamers
* streamers to correct rate (%)