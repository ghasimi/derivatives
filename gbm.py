#!/usr/bin/python

""" Geometric Brownian Motion
"""

import numpy as np

t = 1
mu = .15
sigma = .1
X0 = 100.

n_paths = 10000
np.random.seed(1)
e = np.random.randn(n_paths)

Xt = X0 * np.exp((mu - .5 * sigma ** 2) * t + sigma * np.sqrt(t) * e)

realized_return = np.log(Xt.mean() / X0) / t

print ('Expected Xt    :', X0 * np.exp(mu * t))     # 116.1834242728283
print ('Realized Xt    :', Xt.mean())               # 116.29610672585129
print ('Expected return:', mu)                      # 0.15
print ('Realized return:', realized_return)         # 0.150969396844214
