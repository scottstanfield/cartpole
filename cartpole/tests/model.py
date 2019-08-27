#!/usr/bin/env python

import random
from cartpole import CartPole
cp = CartPole()
print(cp)

for i in range(20):
    cp.step(random.choice([True, False]))
    print(cp)
