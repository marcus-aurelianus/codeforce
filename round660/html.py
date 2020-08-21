from collections import defaultdict 
def HTMLElements(str):
  n=len(str)
  dic=defaultdict(int)

  ans=True
  for i,ele in enumerate(str):
    if ele=="<":
      for j in range(i,n):
        if str[j]==">":
          break
      string=str[i:j+1]

      dic[string]+=1
  print(dic)
  for i,ele in enumerate(str):
    if ele=="<":
      for j in range(i,n):
        if str[j]==">":
          break
      string=str[i:j+1] 

      if "/" in string:
        revstring=string[:]
        revstring.replace("/","")
      else:
        revstring=string[:]
        revstring=revstring[0]+"/"+revstring[1:]
      
      counter0=dic[string]
      counter1=dic[revstring]
      print(string,revstring,counter0,counter1)
      if counter0!=counter1:
        copstring=string[:]
        if "/" in copstring:
          copstring.replace("/","")
        ans=copstring[1:-1]
  return ans
print(HTMLElements("<div><div><b></b></div></p>"))
