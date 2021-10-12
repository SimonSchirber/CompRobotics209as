
import copy
import numpy as np

class Solver():

	def __init__(self, mdp):
		self.mdp = mdp

	def valueIteration(self, H, Gamma):
		Nstates = self.mdp.Nstates
		Nactions = self.mdp.Nactions

		policy = [0 for i in range(Nstates)]

		step = 0
		ValueFxn = np.zeros(Nstates)
		ValueFxnNext = np.zeros(Nstates)
		
		while step < H:
			for state in range(Nstates):
				maxValue = float('-inf')
				maxAction = -1
				for action in range(Nactions):
					curr_sum = 0.0
					for nxt_state in range(Nstates):
						T_p = self.mdp.getTransitionProbability(state, action, nxt_state)
						R = self.mdp.getReward(state, action, nxt_state)
						# if R!=0:
						# 	print(R, T_p)
						curr_sum = curr_sum + (T_p * (R+Gamma*ValueFxn[nxt_state]))
					if curr_sum > maxValue:
						# print(maxValue)
						maxValue = curr_sum
						maxAction = action

				ValueFxnNext[state] = max(maxValue, 0.0)
				policy[state] = int(maxAction)

			ValueFxn = copy.deepcopy(ValueFxnNext)
			step = step+1
			self.mdp.visualiseValue(ValueFxn, step)
		
		return policy

