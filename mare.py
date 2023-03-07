def convertInt(ls):
  res = []
  for i in ls:
    res.append(int(i))
  return res

area = input()
area = area.split("x")
m = []
i = 0
while i < int(area[0]):
  m.append([0]*int(area[1]))
  i += 1

j = 0
round = int(input())
while j < round:
  point = input()
  point = convertInt(point.split(","))#1,2
  lsRow = m[point[0]]
  lsRow[point[1]] = "*"
  j += 1

def increaseVal(data):
  if data == "*":
    return data
  else:
    return data + 1
  
k = 0
while k < len(m):
  j = 0
  while j < len(m[k]):
    if m[k][j] == "*":
      if k == 0: 
        if j == 0: 
          m[k][j+1] = increaseVal(m[k][j+1]) 
          if len(m) > 1:
            m[k+1][j] = increaseVal(m[k+1][j]) 
            m[k+1][j+1] = increaseVal(m[k+1][j+1]) 
        elif j == len(m[k]) - 1: #0, L
          m[k][j-1] = increaseVal(m[k][j-1]) 
          if len(m) > 1:
            m[k+1][j] = increaseVal(m[k+1][j]) 
            m[k+1][j-1] = increaseVal(m[k+1][j-1]) 
        else:
          m[k][j-1] = increaseVal(m[k][j-1])
          m[k][j+1] = increaseVal(m[k][j+1])
          m[k+1][j] = increaseVal(m[k+1][j])
          m[k+1][j-1] = increaseVal(m[k+1][j-1]) 
          m[k+1][j+1] = increaseVal(m[k+1][j+1]) 
      elif k == len(m)-1: #R-L
        if j == 0: #F,0
          m[k][j+1] = increaseVal(m[k][j+1])
          m[k-1][j] = increaseVal(m[k-1][j])
          m[k-1][j+1] = increaseVal(m[k-1][j+1]) 
        elif j == len(m[k]) - 1: #L, 0
          m[k-1][j] = increaseVal(m[k-1][j])
          m[k-1][j-1] = increaseVal(m[k-1][j-1]) 
          m[k][j-1] = increaseVal(m[k][j-1])
        else:
          m[k][j-1] = increaseVal(m[k][j-1])
          m[k][j+1] = increaseVal(m[k][j+1])
          m[k-1][j] = increaseVal(m[k-1][j])
          m[k-1][j-1] = increaseVal(m[k-1][j-1]) 
          m[k-1][j+1] = increaseVal(m[k-1][j+1]) 
      else:
          if j == 0:
            m[k][j+1] = increaseVal(m[k][j+1])
            m[k-1][j] = increaseVal(m[k-1][j])
            m[k+1][j] = increaseVal(m[k+1][j])
            m[k-1][j+1] = increaseVal(m[k-1][j+1]) 
            m[k+1][j+1] = increaseVal(m[k+1][j+1]) 
          elif j == len(m[k]) - 1:
            m[k][j-1] = increaseVal(m[k][j-1])
            m[k-1][j] = increaseVal(m[k-1][j])
            m[k+1][j] = increaseVal(m[k+1][j])
            m[k-1][j-1] = increaseVal(m[k-1][j-1]) 
            m[k+1][j-1] = increaseVal(m[k+1][j-1]) 
          else:
            m[k][j-1] = increaseVal(m[k][j-1])
            m[k][j+1] = increaseVal(m[k][j+1])
            m[k-1][j] = increaseVal(m[k-1][j])
            m[k+1][j] = increaseVal(m[k+1][j])
            m[k-1][j-1] = increaseVal(m[k-1][j-1]) 
            m[k-1][j+1] = increaseVal(m[k-1][j+1]) 
            m[k+1][j-1] = increaseVal(m[k+1][j-1]) 
            m[k+1][j+1] = increaseVal(m[k+1][j+1]) 
    j += 1
  k += 1

for m in m:
  text = ""
  for n in m:
    text += str(n)
  print(text)