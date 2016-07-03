"""
Stephan and Sophia forget about security and use simple passwords for everything. 
Help Nikola develop a password security check module. 
The password will be considered strong enough if its length is greater than or equal to 10 symbols, 
it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. 
The password contains only ASCII latin letters or digits.

Input : A password as a string.
Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean.
In the results you will see the converted results.
"""

import re

def house_password(data):
    low = up = num = False
    length = len(data)
    if length <= 0 or length > 64 :
    	return False
    elif length >= 10:
        for i in range(0, length):
	    m = re.match("[a-z]",data[i])
	    if m is not None:
	    	low = True
	    m = re.match("[A-Z]", data[i])
	    if m is not None:
	    	up = True
	    m = re.match("[0-9]", data[i])
	    if m is not None:
	    	num = True
	return (low and up and num)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house_password('A1213pokl') == False, "1st example"
    assert house_password('bAse730onE4') == True, "2nd example"
    assert house_password('asasasasasasasaas') == False, "3rd example"
    assert house_password('QWERTYqwerty') == False, "4th example"
    assert house_password('123456123456') == False, "5th example"
    assert house_password('QwErTy911poqqqq') == True, "6th example"
