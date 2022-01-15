import json
import numpy as np

#############################
# python scoresData.py      #
#   - total games played    #
#   - average score         #
#############################

# Opening JSON files
scoresJSON = open('./scores.json')
scores = json.load(scoresJSON)

totalScore = 0
totalCount = 0
for score in scores:
    if score == "> 64":
        continue
    totalScore += int(score) * scores[score]
    totalCount += scores[score]

print("total games played", totalCount)
print("average score:", totalScore/totalCount)