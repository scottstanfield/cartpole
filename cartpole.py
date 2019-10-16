"""
Classic cart-pole system implemented by Rich Sutton et al.
Copied from http://incompleteideas.net/sutton/book/code/pole.c
permalink: https://perma.cc/C9ZM-652R
"""

import math
import random
from collections import namedtuple

RAD_PER_DEG = 0.0174533
DEG_PER_RAD = 57.2958

State = namedtuple('State', 'x x_dot theta theta_dot')

class CartPole:
    """ Model for the dynamics of an inverted pendulum
    """
    def __init__(self):
        self.gravity   = 9.8
        self.masscart  = 1.0
        self.masspole  = 0.1
        self.length    = 0.5   # actually half the pole's length
        self.force_mag = 10.0
        self.tau       = 0.02  # seconds between state updates

        self.x         = 0
        self.x_dot     = 0
        self.theta     = 0
        self.theta_dot = 0

    @property
    def state(self):
        return State(self.x, self.x_dot, self.theta, self.theta_dot)

    def __str__(self):
        s = f"{self.state.x:.2f},{self.state.x_dot:.2f},{self.state.theta:.2f},{self.state.theta_dot:.2f}"
        # s = f"x:{self.state.x: .3f}  "\
        #       f"ẋ:{self.state.x_dot: .4f}     "\
        #       f"θ°:{self.state.theta * DEG_PER_RAD: > 8.3f}  "\
        #       f"θv°:{self.state.theta_dot * DEG_PER_RAD: > 8.3f}  "
        return s

    def __repr__(self):
        return self.state

    def reset(self, x=0, x_dot=0, theta=0, theta_dot=0):
        """ Reset the model of a cartpole system to it's initial conditions
        "   theta is in radians
        """
        self.x         = x
        self.x_dot     = x_dot
        self.theta     = theta
        self.theta_dot = theta_dot

    def step(self, action):
        """ Move the state of the cartpole simulation forward one time unit
        """
        total_mass      = self.masspole + self.masscart
        pole_masslength = self.masspole * self.length

        force           = self.force_mag if action else -self.force_mag
        costheta        = math.cos(self.theta)
        sintheta        = math.sin(self.theta)

        temp = (force + pole_masslength * self.theta_dot ** 2 * sintheta) / total_mass

        # theta acceleration
        theta_dotdot = (
            (self.gravity * sintheta - costheta * temp)
            / (self.length *
               (4.0/3.0 - self.masspole * costheta * costheta /
                total_mass)))

        # x acceleration
        x_dotdot = temp - pole_masslength * theta_dotdot * costheta / total_mass

        self.x         += self.tau * self.x_dot
        self.x_dot     += self.tau * x_dotdot
        self.theta     += self.tau * self.theta_dot
        self.theta_dot += self.tau * theta_dotdot

        return self.state

