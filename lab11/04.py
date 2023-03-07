word = input()
wordArr = []
correct = 0
while True:
    guess = input()
    if guess == "0": break
    if guess not in wordArr:
        for i in word:
            if i == guess:
                correct += 1
                wordArr.append(guess)
print(f"{correct}/{len(word)}")
