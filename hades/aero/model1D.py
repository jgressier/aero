"""@package model1D
  representation of 1D flows
"""

import math
import numpy     as np
#import ShockWave as sw
#import IterativeSolve
from ..common import defaultgas as defg

# -- class --

class state():
	"""
	defines a one dimensional state class

	Attributes:
		_gamma
		rho
		u
		p
	"""
	def __init__(self, rho, u, p, gamma=defg._gamma):
	 	self._gamma = gamma
	 	self.rho    = rho
	 	self.u      = u
	 	self.p      = p

	def __repr__(self):
		return "state (rho, u, p) : (%s, %s, %s)" % (self.rho, self.u, self.p)

	def copy(self):
		return state(self.rho, self.u, self.p, self._gamma)

	def asound(self):
		"""returns speed of sound"""
		return math.sqrt(self._gamma*self.p/self.rho)

	def mach(self):
		"""returns speed of sound"""
		return self.u/self.asound()

	def massflow(self):
		"""returns massflow"""
		return self.rho * self.u