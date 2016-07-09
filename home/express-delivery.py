"""
Our three robots found a few mysterious boxes on the island. After some examination Nicola discovered that these boxes have an an 
interesting feature. If you place something in one of them, you can retrieve it again from any other box. Stephan figures this makes
for quick delivery of cargo across the island, moving loads twice as fast. Stephan can place the cargo in one box and pick it up later
at the delivery point. On the map there are water cells which Stephan can't pass, but else these boxes will make his task a whole lot 
easier.

The map for delivery is presented as an array of strings, where:

"W" is a water (closed cell)
"B" is a box
"E" is a goal point.
"S" is a start point.
"." is an empty cell.
Stephan moves between neighbouring cells in two minutes if he carries a load. Without any carry-on luggage, he only needs one minute.
Loading and unloading of cargo in (and out of) the box takes one minute. You should find the fastest way for the cargo delivery 
(minimum time).

The route is a string, where each letter is an action.

"U" -- Up (north)
"D" -- Down (south)
"L" -- Left (west)
"R" -- Right (east)
"B" -- Load or unload in (out) a box.

Input: A map for delivery as a list of strings.

Output: The fastest route as a string.

Example:

checkio(["S...","....","B.WB","..WE"]) #RRRDDD
checkio(["S...","....","B..B","..WE"]) #DDBRRRBD

How it is used: This problem is similar to the "Open labyrinth", but here we have various cost of moves. Using this task,
you will learn algorithms used in pathfinding and graph traversal. For example: in some strategy or role playing games, a unit
can move with different speed on various terrains.
"""


