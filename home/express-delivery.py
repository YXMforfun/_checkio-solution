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
import heapq
MOVE = {"L":(-1,0),"R":(1,0),"U":(0,-1),"D":(0,1)}
def checkio(field_map):
  def get_next(n, c):
      for act in 'LRUD':
          d = MOVE[act]
          pt = d[0]+n[0],d[1]+n[1]
          if pt not in map_data or map_data[pt] == 'W' :
              continue
          m = 2 if c else 1
          if map_data[pt] == 'B' :
             yield act+'B', m+1, pt, not c
          yield act, m, pt, c
          
  map_data = {(x,y) : c for y, line in enumerate(field_map) for x, c in enumerate(line)}
  start = [ k for k,v in map_data.items() if v == 'S'][0]
  visited = set()
  heap = [(0, start, True, '')]
  while heap :
      time, nicola, cargo , route = heapq.heappop(heap)
      visited.add((nicola, cargo))
      if cargo and map_data[nicola] == 'E':
          return route
      for action, minutes, new_nicola, new_cargo in get_next(nicola, cargo):
          if (new_nicola, new_cargo) in visited:
              continue
          new_time = time + minutes
          new_route = route + action
          heapq.heappush(heap, (new_time, new_nicola, new_cargo, new_route)) 
          
          
          
  if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    ACTIONS = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
        "B": (0, 0)
    }

    def check_solution(func, max_time, field):
        max_row, max_col = len(field), len(field[0])
        s_row, s_col = 0, 0
        total_time = 0
        hold_box = True
        route = func(field[:])
        for step in route:
            if step not in ACTIONS:
                print("Unknown action {0}".format(step))
                return False
            if step == "B":
                if hold_box:
                    if field[s_row][s_col] == "B":
                        hold_box = False
                        total_time += 1
                        continue
                    else:
                        print("Stephan broke the cargo")
                        return False
                else:
                    if field[s_row][s_col] == "B":
                        hold_box = True
                    total_time += 1
                    continue
            n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1],
            total_time += 2 if hold_box else 1
            if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
                print("We've lost Stephan.")
                return False
            if field[n_row][n_col] == "W":
                print("Stephan fell in water.")
                return False
            s_row, s_col = n_row, n_col
            if field[s_row][s_col] == "E" and hold_box:
                if total_time <= max_time:
                    return True
                else:
                    print("You can deliver the cargo faster.")
                    return False
        print("The cargo is not delivered")
        return False

    assert check_solution(checkio, 12, ["S...", "....", "B.WB", "..WE"]), "1st Example"
    assert check_solution(checkio, 11, ["S...", "....", "B..B", "..WE"]), "2nd example"
