from MDP import MDP
import numpy as np
import matplotlib.pyplot as plt

class GridWorldMDP(MDP):

	def __init__(self, M, N, agent_state):
		super().__init__(M*N, 5) # M*N states and 5 Actions for now
		self.M = M #rows
		self.N = N #columns
		self.Maze = np.zeros((M, N))
		self.agent_state = agent_state
		self.state_rewards = {
								(7,5) : 5,
								(7,2) : 10,
								(9, 9): -10,
								(9, 8): -10,
								(9, 7): -10,
								(9, 6): -10,
								(9, 5): -10,
								(9, 4): -10,
								(9, 3): -10,
								(9, 2): -10,
								(9, 1): -10,
								(9, 0): -10,
							}
		self.blocks = [
						(7,3),
						(6,3),
						(7,4),
						(6,4),
						(7,6),
						(6,6)
					  ]
		self.Pe = 0.3

	def getState(self, i):
		row = int(i/self.N)
		col = i%self.N
		return row, col

	def getAction(self, i):
		# only 5 actions permitted for now
		# [L, R, U, D, S]
		actions=['L', 'R', 'U', 'D', 'S']
		return actions[i]

	def getTransitionProbability(self, i, j, k):
		rowN, colN = self.getState(k)
		if (rowN, colN) in self.blocks:
			return 0

		next_state = self.getNextState(i, j)
		if k == next_state:
			return 1-self.Pe

		rowC, colC = self.getState(i)
		rowN, colN = self.getState(k)

		if(rowN==rowC+1 and colN==colC):
			return self.Pe/4
		if(rowN==rowC-1 and colN==colC):
			return self.Pe/4
		if(rowN==rowC and colN==colC+1):
			return self.Pe/4
		if(rowN==rowC and colN==colC-1):
			return self.Pe/4
		if(rowN==rowC and colN==colC):
			return self.Pe/4

		return 0
		
	# Next state when you take action j from state i
	def getNextState(self, i , j):
		row, col = self.getState(i)
		a = self.getAction(j)
		row_nxt = None
		col_nxt = None
		if a == 'L':
			row_nxt = row
			col_nxt = col-1
		elif a == 'R':
			row_nxt = row
			col_nxt = col+1
		elif a == 'U':
			row_nxt = row-1
			col_nxt = col
		elif a == 'D':
			row_nxt = row+1
			col_nxt = col
		elif a == 'S':
			row_nxt = row
			col_nxt = col

		if row_nxt<0 or row_nxt>=self.M:
			row_nxt = row
		if col_nxt<0 or col_nxt>=self.N:
			col_nxt = col

		return (row_nxt)*self.N+col_nxt

	def markState(self, state):
		row, col = self.getState(state)
		self.Maze[row][col] = -1

	# Agent takes an action i
	def takeAction(self, i):
		self.clearAgent()
		next_state = self.getNextState(self.agent_state, i)
		self.markState(self.agent_state)
		self.agent_state = next_state

	def startAgent(self, policy, steps):
		self.visualise()
		for step in range(steps):
			# print("Taking action ", self.agent_state, policy[self.agent_state])
			self.takeAction(policy[self.agent_state])
			self.visualise()

	def clearAgent(self):
		row, col = self.getState(self.agent_state)
		self.Maze[row][col] = 0

	def getReward(self, i , j, k):
		row, col = self.getState(k)
		for key, value in self.state_rewards.items():
			if(row==key[0] and col==key[1]):
				return value
		return 0

	def visualise(self):
		row, col = self.getState(self.agent_state)
		self.drawmaze(self.Maze)

	def visualiseValue(self, valueFxn, iteration):
		valueMaze = np.zeros((self.M, self.N))
		maxVal = 0.0
		for i, value in enumerate(valueFxn):
			row, col = self.getState(i)
			valueMaze[col][row] = value
			maxVal = max(maxVal, value)

		for txt in plt.gca().texts:
			txt.set_visible(False)
		for x in range(len(valueMaze)):
			for y in range(len(valueMaze)):
				colVal = 0.0
				if maxVal > 0:
					colVal = valueMaze[x][y]/maxVal
				rectangle = plt.Rectangle((x, y), 1, 1, fc=(colVal, 0.0, 0.0), ec="black")
				plt.gca().add_patch(rectangle)
				plt.gca().text(x+0.25, y+0.25, str(round(valueMaze[x][y])), fontsize=6)
				

		plt.title("Iteration "+str(iteration))
		plt.axis('scaled')
		plt.draw()
		plt.pause(1.5)

	def drawmaze(self, maze):
		for place, value in self.state_rewards.items():
			if value > -1:
				maze[place[0]][place[1]] = 2  # a Green state
			else:
				maze[place[0]][place[1]] = -3 # a Red state

		row, col = self.getState(self.agent_state)
		maze[row][col] = 1

		for place in self.blocks:
			maze[place[0]][place[1]] = 3 # a Gray Block

		plt.axes()
		for x in range(len(maze)):
		    for y in range(len(maze)):
		        if maze[x][y] == 0:
		            rectangle = plt.Rectangle((x, y), 1, 1, fc='white', ec="black")
		            plt.gca().add_patch(rectangle)
		        if maze[x][y] == 1:
		            rectangle = plt.Rectangle((x, y), 1, 1, fc='blue', ec="black")
		            plt.gca().add_patch(rectangle)
		        if maze[x][y] == -1:
		            rectangle = plt.Rectangle((x, y), 1, 1, fc='purple', ec="black")
		            plt.gca().add_patch(rectangle)
		        if maze[x][y] == 2:
		            rectangle = plt.Rectangle((x, y), 1, 1, fc='green', ec="black")
		            plt.gca().add_patch(rectangle)
		        if maze[x][y] == -3:
		            rectangle = plt.Rectangle((x, y), 1, 1, fc='red', ec="black")
		            plt.gca().add_patch(rectangle)
		        if maze[x][y] == 3:
		            rectangle = plt.Rectangle((x, y), 1, 1, fc='gray', ec="black")
		            plt.gca().add_patch(rectangle)

		plt.axis('scaled')
		plt.draw()
		plt.pause(0.5)
			


		