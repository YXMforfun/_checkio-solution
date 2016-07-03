"""
A blacksmith gave his apprentice a task, ordering them to make a selection of rings. The apprentice is not yet skilled in the craft and
as a result of this, some (to be honest, most) of rings came out connected together. Now he’s asking for your help separating the rings 
and deciding how to break enough rings to free so as to get the maximum number of rings possible.

All of the rings are numbered and you are told which of the rings are connected. This information is given as a sequence of sets.
Each set describes the connected rings. For example: {1, 2} means that the 1st and 2nd rings are connected. You should count how many 
rings we need to break to get the maximum of separate rings. Each of the rings are numbered in a range from 1 to N, where N is total
quantity of rings.

Input: Information about the connected rings as a tuple of sets with integers.

Output: The number of rings to break as an integer.

Example:

break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {4, 6}, {6, 5})) == 3


#https://en.wikipedia.org/wiki/Vertex_cover
This question is about Minimal Vertex_cover
Pseudo Code
 1  APPROXIMATION-VERTEX-COVER(G):
 2 C = ∅
 3 E'= G.E
 4 
 5 while E'≠ ∅:
 6     let (u, v) be an arbitrary edge of E'
 7     C = C ∪ {u, v}
 8     remove from E' every edge incident on either u or v
 9 
10 return C
"""

import itertools

def break_rings(rings):
    link_map = {}
    for link in rings:
        for ring in link:
            link_map.setdefault(ring, link.copy()).update(link)      #G(V, E) like {1 : [1,2,3], 2: [2,3,4]....}
    
    for i in range(1, len(link_map)):                                               # i is the number of vertex_cover
        for remove_rings in itertools.combinations(link_map.keys(), i):              # remove some pairs like (1,2) or (2,3,4,5) ...
            removed = set(remove_rings)
            count = 0
            for links in link_map.items():
                if links[0] not in removed:
                    count += len(links[1] - removed) - 1                                    
            if count == 0:
                return i
    

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
