exam = input().split(' ')
percent = input().split(' ')
n = int(input())

listEx = sum([int(i) for i in exam])
present = []
progress = []
dis = []

for i in range(n):
  act = input().split(' ')
  all = len(act)
  one = act.count('1')
  present.append((one * 100) / all)
    

for i in range(n):
  don = input().split(' ')
  ls_don = sum([int(i) for i in don])
  all = len(don)
  progress.append((ls_don * 100) / listEx)

count = 0
for i in range(n):
  order = str(i+1)
  if present[i] < float(percent[0]) and progress[i] < float(percent[1]):
    count += 1
    order = '(' + str(i+1) + ')'
  dis.append(order + ' ' + f'{present[i]:.2f} {progress[i]:.2f}')

print(count)
[print(i) for i in dis]