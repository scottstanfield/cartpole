""" The state transform, action transform, terminal function and reward
    function. The functions in this file are called from hub.py.
"""

import math
from scipy.stats import norm

my_norm = norm(0, 0.5)

from bonsai_ai.logger import Logger

log = Logger()

THETA_MAX = 45 * 2 * math.pi / 360
X_MAX = 2.4

def state(model_state):
    """ Convert the state as represented in CartPole to a format expected.
        by the AI Engine.
    """
    return {
        'position': model_state[0],
        'velocity': model_state[1],
        'angle':    model_state[2],
        'rotation': model_state[3],
    }


def terminal(model_state):
    """ Return true if the state should end the episode. This includes both
        failure terminals (such as when the model isout-of-bounds) and success
        terminals (when the model is in a successful state)
    """
    # position, velocity, angle, rotation
    x, x_dot, theta, theta_dot = model_state

    # Terminal occurs when the cart's position is too far to the left or right
    # or the cart's pole has tipped too far.
    out_of_bounds = not (-X_MAX     <= x     <= X_MAX)
    falling_over  = not (-THETA_MAX <= theta <= THETA_MAX)

    return (out_of_bounds or falling_over)

def action(brain_action):
    """ Convert the action from the AI Engine to a format expected by the CartPole model.
    """
    return 1 if brain_action['command'] > 0 else 0

def reward(model_state, done):
    """ Return greater values to reward the AI for correct behavior.
    """
    return 1

    # If the AI has not hit a terminal situation reward it with a score of 1.0

    x, x_dot, theta, theta_dot = model_state

    #bonus = my_norm.pdf(x)
    penalty = x / 2

    return 0 if done else 1 -penalty

