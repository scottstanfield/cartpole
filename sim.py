#!/usr/bin/env python

"""
This file contains the simulator that controls the cartpole model
using actions from the Bonsai Platform
"""

import sys, os

from bonsai_ai import Simulator, Brain, Config, logger
import star
from cartpole import CartPole
from render import Viewer

log = logger.Logger()

class CartpoleSimulator(Simulator):

    def __init__(self, brain, model):
        super().__init__(brain, "the_simulator")      # string must match cartpole.ink
        self.model = model

    def episode_start(self, parameters=None):
        self.model.reset()
        return star.state(self.model.state)

    def simulate(self, brain_action):
        action = star.action(brain_action)

        self.model.step(action)

        terminal    = star.terminal(self.model.state)
        reward      = star.reward(self.model.state, terminal)
        brain_state = star.state(self.model.state)

        if terminal:
            log.info(f'Episode {self.episode_count}: '
                     f'iterations={self.iteration_count:-3.0f} reward={self.episode_reward:-3.1f}')

        return (brain_state, reward, terminal)


if __name__ == "__main__":
    log.info(f'Process ID {os.getpid()}')

    config    = Config(sys.argv)        # Parses ~/.bonsai and .brains
    brain     = Brain(config)

    model     = CartPole()

    sim       = CartpoleSimulator(brain, model)

    should_render = False

    if '--render' in sys.argv:
        should_render = True
        log.info('Rendering to screen')
        viewer = Viewer()
        viewer.model = model

    log.info(f'Training {brain.name}...')
    while sim.run():
        if should_render:
            viewer.update()
            if viewer.has_exit:
                viewer.close()
                sys.exit(0)

