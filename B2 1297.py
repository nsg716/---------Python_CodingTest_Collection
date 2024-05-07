import math
d, h, w = map(int, input().split())

a =w/h
height = math.sqrt((d**2)/(1+a**2))
width = a*height
print(int(height),int(width) )



