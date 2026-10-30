
# Nested List Sports Performance Analysis

n = int(input("Enter number of players: "))
m = int(input("Enter number of matches: "))

players = []
scores = []

# Input player details and scores
for i in range(n):
    name = input("\nEnter player name: ")
    players.append(name)

    match_scores = []
    print("Enter scores for", name)

    for j in range(m):
        score = int(input("Match " + str(j + 1) + ": "))
        match_scores.append(score)

    scores.append(match_scores)

# Analyse player performance
results = []

for i in range(n):
    total = sum(scores[i])
    average = total / m

    highest = max(scores[i])
    lowest = min(scores[i])

    consistency = highest - lowest

    # Identify performance trend
    if all(scores[i][j] < scores[i][j + 1]
           for j in range(m - 1)):
        trend = "Improving"

    elif all(scores[i][j] > scores[i][j + 1]
             for j in range(m - 1)):
        trend = "Declining"

    elif all(x == scores[i][0] for x in scores[i]):
        trend = "Stable"

    else:
        trend = "Inconsistent"

    results.append([
        players[i], total, average,
        consistency, highest, trend
    ])

# Ranking: Average score, then highest score
results.sort(key=lambda x: (x[2], x[4]), reverse=True)

# Display results
print("\n----- SPORTS PERFORMANCE REPORT -----")

print("Player\tTotal\tAverage\tConsistency\tTrend")

for r in results:
    print(r[0], "\t", r[1], "\t",
          round(r[2], 2), "\t",
          r[3], "\t\t", r[5])

print("\n----- FINAL PLAYER RANKING -----")

for i, r in enumerate(results):
    print(i + 1, ".", r[0],
          "- Average:", round(r[2], 2),
          "- Highest Score:", r[4])

print("\nAnalysis Completed!")

