#!/usr/bin/env python

import random
from cartpole import CartPole
cp = CartPole()

for i in range(int(1e3)):
    print(cp)
    cp.step(random.choice([True, False]))

print(cp)
