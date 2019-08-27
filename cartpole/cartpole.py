"""
Classic cart-pole system implemented by Rich Sutton et al.
Copied from http://incompleteideas.net/sutton/book/code/pole.c
permalink: https://perma.cc/C9ZM-652R
"""

import math
import random
from collections import namedtuple

DEG_PER_RAD = 0.0174533
RAD_PER_DEG = 57.2958

CartPoleState = namedtuple('CartPoleState', 'x x_dot theta theta_dot')

class CartPole:
    """ Model for the dynamics of an inverted pendulum
    """
    def __init__(self):
        self.gravity         = 9.8
        self.masscart        = 1.0
        self.masspole        = 0.1
        self.length          = 0.5  # actually half the pole's length
        self.force_mag       = 10.0
        self.tau             = 0.02  # seconds between state updates

        self.reset()

    def __str__(self):
        str = f"x:{self.state.x: .3f}  "\
              f"ẋ:{self.state.x_dot: .4f}     "\
              f"θ°:{self.state.theta * RAD_PER_DEG: > 8.3f}  "

        return str

    def __repr__(self):
        return self.state

    def reset(self):
        """ Reset the model of a cartpole system to it's initial conditions
        """
        self.x         = 0
        self.x_dot     = 0

        # +/- ~10 degrees off the vertical
        self.theta     = random.uniform(-0.15, 0.15)
        self.theta_dot = 0

    def step(self, action):
        """ Move the state of the cartpole simulation forward one time unit
        """
        total_mass = self.masspole + self.masscart
        polemass_length = (self.masspole * self.length)

        force      = self.force_mag if action else -self.force_mag
        costheta   = math.cos(self.theta)
        sintheta   = math.sin(self.theta)
        temp = (
            (force + polemass_length * self.theta_dot ** 2 * sintheta)
            / total_mass)
        thetaacc = (
            (self.gravity * sintheta - costheta * temp)
            / (self.length *
               (4.0/3.0 - self.masspole * costheta * costheta /
                total_mass)))
        xacc = (
            temp - polemass_length * thetaacc * costheta / total_mass
        )
        self.x         += self.tau * self.x_dot
        self.x_dot     += self.tau * xacc
        self.theta     += self.tau * self.theta_dot
        self.theta_dot += self.tau * thetaacc

        return self.state

    @property
    def state(self):
        return CartPoleState(self.x, self.x_dot, self.theta, self.theta_dot)

