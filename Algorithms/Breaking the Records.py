# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

# Example
# scores = [12,24,10,24]

# Scores are in the same order as the games played. She tabulates her results as follows:

#                                      Count
#     Game  Score  Minimum  Maximum   Min Max
#      0      12     12       12       0   0
#      1      24     12       24       0   1
#      2      10     10       24       1   1
#      3      24     10       24       1   1
# Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

# SOLUTION

def breakingRecords(scores):
    high_score= scores[0]
    low_score = scores[0]
    max_count, min_count = 0, 0
    for i in range(len(scores)):
        if scores[i] > high_score:
            high_score = scores[i]
            max_count+=1
        elif scores[i] < low_score:
            low_score = scores[i]
            min_count+=1
    return max_count, min_count

