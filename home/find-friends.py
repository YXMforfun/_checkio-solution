"""
We have an array of straight connections between drones. Each connection is represented as a string with two names of friends separated
by hyphen. For example: "dr101-mr99" means what the dr101 and mr99 are friends. Your should write a function that allow determine more
complex connection between drones. You are given two names also. Try to determine if they are related through common bonds by any depth.
For example: if two drones have a common friends or friends who have common friends and so on.
 Network:  dr101-mr99
           mr99 -out00
           dr101-out00
           scout1-scout2
           scout3-scout1
           scout1-scout4
           scout4-sscout
           sscout-super
Let's look at examples:
scout2 and scout3 have the common friend scout1 so they are related. super and scout2 are related through sscout, scout4 and scout1.
But dr101 and sscout are not related.

Input: Three arguments: Information about friends as a tuple of strings; first name as a string; second name as a string.

Output: Are these drones related or not as a boolean.

"""

def check_connection(network, first, second):
    d = dict()
    for i in network:
        tmp1, tmp2 = i.split('-')
        d.setdefault(tmp1, []).append(tmp2)
        d.setdefault(tmp2, []).append(tmp1)
    future = [first]
    visited = []
    while len(future):
        top = future.pop()
        visited.append(top)
        if top == second:
            return True
        for next in d.setdefault(top, []):
            if next not in visited and next not in future:
                future.append(next)
    return False
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
