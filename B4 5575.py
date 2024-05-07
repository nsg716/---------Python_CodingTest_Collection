h1, m1, s1, h2, m2, s2 = map(int, input().split())
h3, m3, s3, h4, m4, s4 = map(int, input().split())
h5, m5, s5, h6, m6, s6 = map(int, input().split())

res1 = h1*3600+m1*60+s1
res2 = h2*3600+m2*60+s2
res3 = h3*3600+m3*60+s3
res4 = h4*3600+m4*60+s4
res5 = h5*3600+m5*60+s5
res6 = h6*3600+m6*60+s6

ress1 = res2-res1
ress2 = res4-res3
ress3 = res6-res5

ah1 = ress1//3600
am1 = (ress1%3600)//60
as1 = (ress1%3600%60)

ah2 = ress2//3600
am2 = (ress2%3600)//60
as2 = (ress2%3600%60)

ah3 = ress3//3600
am3 = (ress3%3600)//60
as3 = (ress3%3600%60)


print(ah1, am1, as1)
print(ah2, am2, as2)
print(ah3, am3, as3)

