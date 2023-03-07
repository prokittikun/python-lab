reversed = "-_=.$"
camelCase = ""
text = input()
for i in range(0, len(text)):
    if text[i-1] in reversed and text[i] not in reversed and camelCase != "":
        camelCase += text[i].upper()
    elif text[i] not in reversed:
        camelCase += text[i].lower()
print(camelCase)
