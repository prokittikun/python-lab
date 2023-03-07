word = input()
ans = ""
guessGroup = ""
while True:
    guess = input()
    if guess == "0": break
    guessGroup += guess
for i in word:
    if i not in guessGroup: 
        ans += "-"
    else: ans += i
print(f"{ans}")
