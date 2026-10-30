# Nested List Sports Performance Analysis – Python Program

## 1. Problem Statement

Develop a Python program using nested lists to analyse the performance of players across multiple sports matches. The program should store players' scores in a nested list, calculate total and average scores, measure consistency using score differences, identify performance trends, and rank players based on their average scores. If two players have the same average score, use the highest individual score as the tiebreaking rule.

## 2. Algorithm

1. Start the program.
2. Read the number of players and matches.
3. Store player names and their match-wise scores using nested lists.
4. Calculate the total score of each player.
5. Calculate the average score of each player.
6. Calculate the consistency measure using the difference between maximum and minimum scores.
7. Identify performance trends:
   - Improving: scores are continuously increasing.
   - Declining: scores are continuously decreasing.
   - Inconsistent: scores fluctuate.
   - Stable: scores remain the same.
8. Rank players based on average scores in descending order.
9. If averages are equal, compare their highest individual scores.
10. Display player statistics and final rankings.
11. Stop the program.

## 3. Flowchart

[PPT - QBASIC PowerPoint Presentation, free download - ID:6640494](https://images.openai.com/static-rsc-4/0tPzhi44G8jmOdhxzal8_7bzCuFv_IhS7moZhX8xBfUg4yY2sAUjH-7y0R0gK89gAjEfeQKSEeBZuRiy93h24FQlV0YZxQA48sCJUgodQkhFLKEt1Ey3VRBLyoo4etsDpifqtZQdkf2gwoIH3MBjOEUhKh28zB6woavTmc3hK5A?purpose=inline)

## 4. Python Source Code

```
# Nested List Sports Performance Analysisn = int(input("Enter number of players: "))m = int(input("Enter number of matches: "))players = []scores = []# Input player details and scoresfor i in range(n):    name = input("\nEnter player name: ")    players.append(name)    match_scores = []    print("Enter scores for", name)    for j in range(m):        score = int(input("Match " + str(j + 1) + ": "))        match_scores.append(score)    scores.append(match_scores)# Analyse player performanceresults = []for i in range(n):    total = sum(scores[i])    average = total / m    highest = max(scores[i])    lowest = min(scores[i])    consistency = highest - lowest    # Identify performance trend
```

## 5. Sample Input

```
Enter number of players: 3
Enter number of matches: 4

Enter player name: Ravi
Match 1: 40
Match 2: 50
Match 3: 60
Match 4: 70

Enter player name: Kumar
Match 1: 80
Match 2: 70
Match 3: 60
Match 4: 50

Enter player name: Arun
Match 1: 60
Match 2: 60
Match 3: 60
Match 4: 60
```

## 6. Sample Output

```
----- SPORTS PERFORMANCE REPORT -----

Player  Total  Average  Consistency  Trend
Ravi     220    55.0       30        Improving
Kumar    260    65.0       30        Declining
Arun     240    60.0        0        Stable

----- FINAL PLAYER RANKING -----

1. Kumar - Average: 65.0 - Highest Score: 80
2. Arun - Average: 60.0 - Highest Score: 60
3. Ravi - Average: 55.0 - Highest Score: 70

Analysis Completed!
```

## 7. Result

Thus, the Python program successfully analyses players' sports performance using nested lists, calculates total scores, averages and consistency, identifies performance trends, and ranks players according to the given tiebreaking rules.
