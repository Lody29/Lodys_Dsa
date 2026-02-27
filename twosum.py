nums = []
target = input("Your target is ?")
seen = {}

for i ,num in enumerate(nums) :
    complement = int(target) - num
    if complement in seen:
        print(f"[{seen[complement]},{i}]")
    else: 
        seen[num] = i



