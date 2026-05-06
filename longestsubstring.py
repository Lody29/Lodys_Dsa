def longestsubstring(s):
      
        
        start = 0 #initialization
        max_length = 0
        char_map = {}

        for j,character in enumerate(s): #breaking down string to elements
            if character in char_map and char_map[character] >= start: #for each character that we have seen 
             start =  char_map[character] + 1
            char_map[character] = j

            max_length = max(max_length ,j - start +1)
        return max_length

