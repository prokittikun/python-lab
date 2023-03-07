original = []
frequency = [0,0,0,0,0,0,0,0,0,0,0] 
student = 1
while True:
  if student <= 20 :
    score = int(input("Enter score: "))
    if score >= 0 and score <= 10:
      frequency[score] += 1
      original.append(score)
    else:
      print("Score is out of range.")
      continue
  else: break
  student += 1
print(f"Original list:")
print(original)
for i in range(0, len(frequency)):
  print(f"{i:2d} " + "*"*frequency[i])
    