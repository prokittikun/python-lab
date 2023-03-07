def extract_string(s):
  ls = []
  str = ""
  num = ""
  for i in range(0,len(s)):
    if s[i] == changeType(s[i]): 
        ls.append(changeType(num))
        num = ""
        str += s[i]
    if s[i] != changeType(s[i]):
        ls.append(str)
        str = ""
        num += s[i]
    if i+1 == len(s) and s[i] == changeType(s[i]): ls.append(changeType(str))
    elif i+1 == len(s) and s[i] != changeType(s[i]): ls.append(changeType(num))
  new = []
  for j in ls:
    if j != "": new.append(j)
  return new

def changeType(s):
  if s.isnumeric(): return int(s)
  else: return s
print( extract_string("G2X3t4") )