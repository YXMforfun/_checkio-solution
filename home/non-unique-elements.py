"""You are given a non-empty list of integers (X). 
For this task, you should return a list consisting of only the non-unique elements in this list. 
To do so you will need to remove all unique elements (elements which are contained in a given list only once). 
When solving this task, do not change the order of the list. 
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
"""


def non_unique(data):
    result = []
    for i in range(0, len(data)):
        if data.count(data[i]) >= 2:
	    result.append(data[i])
    return result


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
     assert isinstance(non_unique([1]), list), "The result must be a list"
     assert non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
     assert non_unique([1, 2, 3, 4, 5]) == [], "2nd example"
     assert non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
     assert non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
