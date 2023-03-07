text = input().lower()
answer = []
textInLoop = ""
for i in range(len(text)):
    if len(textInLoop) == 2:
        if textInLoop not in answer: answer.append(textInLoop)
        textInLoop = text[i-1]
    textInLoop += text[i]
    if i == len(text)-1 and textInLoop not in answer: answer.append(textInLoop)
answer.sort()
for i in answer: print(i)