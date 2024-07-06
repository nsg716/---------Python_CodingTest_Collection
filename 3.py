import math
x1,y1,y2,x2,y3,y4,x3 = map(int,input().split())

s1 = 9.23076 * pow ( (26.7-x1), 1.835)

s2 = 1.84523 * pow ( (y1-75), 1.348)
s3 = 56.0211 * pow ( (y2-1.5), 1.05)


s4 = 4.99087 * pow ( (42.5-x2), 1.81)

s5 = 0.188807 * pow ( (y3-210), 1.41)
s6 = 15.9803 * pow ( (y4-3.8), 1.04)

s7 = 0.11193 * pow ( (254-x3), 1.88)

sum  = int(s1)+int(s2)+int(s3)+int(s4)+int(s5)+int(s6)+int(s7)

print(sum)