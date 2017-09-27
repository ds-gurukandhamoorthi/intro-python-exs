import itertools
from bernoulli import count_integers

comb_with_rp = itertools.combinations_with_replacement

NB_SIDE=6

def expected_dist(dice_values1, dice_values2, n):
    sums = (v1 + v2 for v1 in dice_values1  for v2 in dice_values2)
    return count_integers(sums, n)

# def expected_dist(dice_values1, dice_values2, max_sum):
#     expected_dist = [0] * (max_sum + 1)
#     for face_value1 in dice_values1:
#         for face_value2 in dice_values2:
#             print(face_value1, face_value2)
#             expected_dist[face_value1 + face_value2] += 1
#     return expected_dist

def dice_values(nb_sides):
    return range(1,nb_sides+1)

MAX = max(dice_values(NB_SIDE))*2
print(MAX)

EXPECTED=expected_dist(dice_values(NB_SIDE), dice_values(NB_SIDE), NB_SIDE*2+1)
print("EXPECTED", EXPECTED)

count = 0
for dice1 in comb_with_rp(range(1,MAX ),NB_SIDE):
    for dice2 in comb_with_rp(range(1,MAX ),NB_SIDE):
        sum_ = expected_dist(dice1, dice2, NB_SIDE*2+1)
        if sum_ == EXPECTED:
            print(sum_)
            print('SOLUTION')
            print( dice1, dice2)







