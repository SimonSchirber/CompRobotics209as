# CompRobotics209as
Computational Robotics

## Week 1:
The grid dimensions, obstacles, icecream stops, road stops, and intial position are defined.
The script lists/defines:
- All states, which is equivalent to every spot on the grid
- All transitions, which are mathematically defined as [State, transistion, State] and include transitions that have non-zero probability
- Number of transitions: 3125
- Number of non-zero probabilty transitions: 73 (around 2.3% of transitions non-zero probability)

With no direction from sensors, or probablistic movements give, a "move" function is built to take the initial square and amount of desired moves, and move the piece randomly according to the calculated non-zero probabilty transitions in that state for the amount of listed moves. Each time a move happens, the possible transitions for that state are listed.

