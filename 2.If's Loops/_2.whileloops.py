#With the break statement we can stop the loop even if the while condition is true:
i = 1
while (i < 6):
  print(i)
  if i == 3:    
    break # come out of the loop
  i += 1

#With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #skip the current iteration
  #print(i)

#With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6: # and and or statements can also be used
  #print(i)
  i += 1
else:
  #print("i is no longer less than 6")
  pass

