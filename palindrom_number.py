def ispalindrome(self,x):
    x = str(x)
    y = x[::-1]

    if x<0:
      return False



    if x == y: 
      return True
    else:
      return False