def  cloth_size(width_list):
    dic = {"S": 0,"M": 0, "L": 0}
    for i in width_list:
        if i <= 36: dic["S"] += 1
        elif i <= 44: dic["M"] += 1
        else: dic["L"] += 1

    return dic
print(cloth_size([50, 44, 40, 48]))