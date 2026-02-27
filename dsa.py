def numStep(self,s):
    steps=0
    num = int(s,2)

    while num != 1:
         mod = num%2
         if mod != 0:
           num = num+1 
         else:
           num = num//2
         steps += 1
    
    return(steps)

        

    