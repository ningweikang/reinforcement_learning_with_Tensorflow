#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 18:23
# @Author  : Wang Shuailong

import gym


class Environment(object):
    def __init__(self, name, seed=1):
        self.name = name
        env = gym.make(name)
        env.seed(seed)
        self.env = env.unwrapped
        self.n_states = env.observation_space.shape[0]
        self.n_actions = env.action_space.shape[0]
        self.a_low_bound = env.action_space.low
        self.a_high_bound = env.action_space.high

    def reset(self):
        return self.env.reset()

    def step(self, a):
        return self.env.step(a)

