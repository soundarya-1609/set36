k=input()
f=0
for i in range(len(k)):
 if(k[i].isdigit() or k[i].isalpha() or k[i]==(" ")):
  continue
 else:
  f+=1
print(f)
