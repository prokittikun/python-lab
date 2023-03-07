text = input()
text += "-"*2
list = ["a", "e", "i", "o", "u"]
answer = ""
i = 0
while i < len(text): 
    answer += text[i]
    if text[i] in list and text[i+1] == "p" and text[i+2] == text[i] :
        i += 3
    else :
        i += 1
print(answer[:-2])