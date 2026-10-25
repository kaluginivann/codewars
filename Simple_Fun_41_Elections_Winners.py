# Task
# Elections are in progress!

# Given an array of numbers representing votes given to each of the candidates, and an integer which is equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

# The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.

# Note: big arrays will be tested.

# Examples
# votes = [2, 3, 5, 2]
# voters = 3

# result = 2
# Candidate #3 may win, because he's already leading.
# Candidate #2 may win, because with 3 additional votes he may become the new leader.
# Candidates #1 and #4 have no chance, because in the best case scenario each of them can only tie with the candidate #3.
# votes = [3, 1, 1, 3, 1]
# voters = 2

# result = 2
# Candidate #1 and #4 can become leaders if any of them gets the votes.
# If any other candidate gets the votes, they will get tied with candidates #1 and #4.
# votes = [1, 3, 3, 1, 1]
# voters = 0

# result = 0
# There're no additional votes to cast, and there's already a tie.

def elections_winners(votes, k):
    max_votes = max(votes)
    count_max = votes.count(max_votes)
    winners = 0
    for v in votes:
        if v == max_votes:
            if count_max == 1 or k > 0:
                winners += 1
        else:
            if v + k > max_votes:
                winners += 1
    return winners