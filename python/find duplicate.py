n=input("enter any string :")
count=0
duplicate={}
for ch in n:
    if ch in duplicate:
        duplicate[ch] = duplicate[ch] + 1
    else:
        duplicate[ch] = 1    
for ch in duplicate:
    if duplicate[ch] > 1:
        print(f"the character {ch} is duplicate {duplicate[ch]} times ")        
   