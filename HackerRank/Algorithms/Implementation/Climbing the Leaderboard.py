def climbingLeaderboard(leaderboard, scores):
    # Player scores that there are not on the leaderboard
    set_diff = set(scores) - set(leaderboard)

    # Make an union of player scores with the leaderboard
    merged = set(leaderboard) | set(scores)

    # Change "merged" variable into a dictionary assigning
    # the position for each score (that's why start by 1),
    # greater to less
    #
    # enumerate(sorted(merged, reverse=True), start=1)  ->  (1, s1) (2, s2) (3, s3)....
    # dict(enumerate(sorted(merged, reverse=True), start=1))  ->  {1: s1, 2: s2, 3: s3...}
    #
    # v: k  ->  {score: position}
    # {s1: 1, s2: 2, s3: 3...}
    merged = {v: k for k, v in dict(enumerate(sorted(merged, reverse=True), start=1)).items()}

    results = []

    # For every score in player scores
    for score in scores:
        # Verify IF "score" exist on "set_diff"
        if score in set_diff:
            # Then, remove "score" from "set_diff"
            set_diff.remove(score)

        # append(position according to score - len(set_diff))
        results.append(merged[score] - len(set_diff))

    return results

if __name__ == '__main__':

    _ = int(input())
    # Leaderboard
    leaderboard = list(map(int, input().split()))

    _ = int(input())
    # Scores gotten by player
    scores = list(map(int, input().split()))

    print(*climbingLeaderboard(leaderboard, scores), sep="\n")