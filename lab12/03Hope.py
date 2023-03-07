ss_list = []
max_space = 0
while True:
  ss = input()
  if ss == "-1":
    break
  ss_list_temp = []
  for c in ss.split("=",1):
    ss_list_temp.append(c.strip())
  ss_list.append(ss_list_temp)

for ss in ss_list:
  if max_space == 0:
    max_space = len(ss[0])
  elif len(ss[0]) > max_space:
    max_space = len(ss[0])
    
for c in ss_list:
  space_count = max_space-len(c[0]) 
  print(" "*space_count,end="")
  print(c[0],end="")
  print(" = ",end="")
  print(c[1])