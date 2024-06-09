
import re
def is_palindrome(teststr):
    # use the slice trick to reverse the string
    teststr = teststr.lower()
    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x
    if teststr == teststr[::-1]:
        return True
    return False

run = True
while (run):
    teststr = input("Enter string to test for palindrome or 'exit':")

    # If the user types "exit" then quit the program
    if teststr == "exit":
        run = False
        break

    # convert the string to all lower case
    teststr = teststr.lower()
    newstr = ''.join(e for e in teststr if e.isalnum())
    
  #one liner to remote special chars and leave only alphabeth and numbers
    #''.join(e for e in teststr if e.isalnum())

  #     one lines using Regex to remove special char and leave only alphabet and numbers
    #re.sub('[A-Za-z0-9]+','', teststr)

    
    #strip all the spaces and punctuation from the string
    
    print("Palindrome test:", is_palindrome(newstr))

