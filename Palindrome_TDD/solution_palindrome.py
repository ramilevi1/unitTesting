from unidecode import unidecode

def is_palindrome(teststr):
  teststr = teststr.lower()
  teststr = unidecode(teststr)
  newstr = ""
  for x in teststr:
    if x.isalnum():
      newstr += x
  if newstr ==newstr[::-1]:
    return True
  return False
