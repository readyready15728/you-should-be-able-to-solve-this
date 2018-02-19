from __future__ import division
import random

total_with_at_least_one_head = 0
total_with_two_heads = 0

for _ in xrange(100000):
    first_coin = random.choice([0, 1])
    second_coin = random.choice([0, 1])

    if first_coin == 0 and second_coin == 0:
        continue
    else:
        total_with_at_least_one_head += 1

        if first_coin == 1 and second_coin == 1:
            total_with_two_heads += 1

print total_with_two_heads / total_with_at_least_one_head
