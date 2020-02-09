#Write a python program that analyzes a year's woth of rainfall data...
import math
Rain_data= tuple()
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec',]
for I in range(12):
    x=int(input(f"Enter the rainfall for the month of {months[I]}: "))
    Rain_data = Rain_data + (x,)
High_fall = max(Rain_data)
Low_fall = min(Rain_data)
avg = math.fsum(Rain_data)/len(Rain_data)
L_Rain_data=list(Rain_data)

print(f"The maximum rainfall is {High_fall} inches and happens in the month of {months[L_Rain_data.index(High_fall)]}")
print(f"The minimum rainfall is {Low_fall} inches and happens in the month of {months[L_Rain_data.index(Low_fall)]}")
print(f"The monthly average rainfall is {avg} inches")

