# CompRobotics209as
Computational Robotics

## To Run
python3 driver.py

## Week 1:
The grid dimensions, obstacles, icecream stops, road stops, and intial position are defined.
The script lists/defines:
- All states, which is equivalent to every spot on the grid
- All transitions, which are mathematically defined as [State, action, State] and include transitions that have non-zero probability
- Number of transitions: 3125
- Number of non-zero probabilty transitions: 73 (around 2.3% of transitions non-zero probability)

With no direction from sensors, or probablistic movements give, a "move" function is built to take the initial square and amount of desired moves, and move the piece randomly according to the calculated non-zero probabilty transitions in that state for the amount of listed moves. Each time a move happens, the possible transitions for that state are listed.

## Week 2:
This week the script was redesigned to take in an action, and generate probabilites for transtions while playing the game. The game also prints the observation after a transition, but it should note that this cannot be computed when it reaches an ice cream store as the distance = 0 and 1/0 is not possible, so when this happens it simply prints "at ice cream store". There is also now a GUI that displays the grid and where the robot, ice cream store, barriers, and road is. Movement are made by typing in input like u,d,l,r,s for up, down , left, right, stay.

We need to come up with a more general function/script that can take in any list of States, Actions, Probabilities, and Observations as this can only handle specific scenarios.

