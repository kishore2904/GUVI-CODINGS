sand=input()
a=0
for i in sand:
  if i=='0' or i=='1':
    a=a+1
  else:
    break
if a==len(sand):
  print('yes')
else:
  print('no')
