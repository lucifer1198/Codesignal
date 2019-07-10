"""
A test score is perfect if every answer is correct.

You are asked to implement a grader that checks whether a 3 question test score
is perfect based on the correctness of answers to each of the 3 questions.

Example

For ans1 = true, ans2 = true and ans3 = true, the output should be
isPerfectScore(ans1, ans2, ans3) = true.
"""


def isPerfectScore(ans1, ans2, ans3):
    return ans1 and ans2 and ans3
