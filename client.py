"""Grover's Search Algorithm Engine.
100% Python Standard Library.
"""

import math

class GroverSearch:
    """Grover's amplitude amplification search simulator."""
    def __init__(self, num_items=8, target_idx=3):
        self.n = num_items
        self.target = target_idx
        self.state = [1.0 / math.sqrt(num_items)] * num_items

    def step(self):
        self.state[self.target] = -self.state[self.target]
        mean = sum(self.state) / self.n
        self.state = [2.0 * mean - s for s in self.state]

    def get_target_probability(self):
        return self.state[self.target]**2
