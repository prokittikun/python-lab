i = 0
canSee = 0
heightOne = 0
while True:
    height = int(input())
    if height > 0:
        if i == 0:
            heightOne = height
            canSee += 1
        if heightOne < height:
            heightOne = height
            canSee += 1
    else:
        break
    i += 1
print(canSee)
    