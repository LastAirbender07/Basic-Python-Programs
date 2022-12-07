# Given string s1=’sheep’ s2=’horse’ , output : peersh (last char + middle char +first char of two strings )

s1 = 'sheep'
s2 = 'horse'
s3 = s1[4] + s1[2:4] + s2[2] + s1[0] + s2[0]
print(s3)