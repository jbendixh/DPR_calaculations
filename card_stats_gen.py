import numpy as np

deck_balance = np.array([3,4,5,5,5,6,6,7,7,7,8,9])
deck_swing = np.array([1,2,3,5,6,7,7,7,8,8,9,9])
deck_custom = np.array([1,3,3,4,6,7,7,7,8,8,9,9])
print(sum(deck_custom))
array = np.zeros(6)

good_counter = 0.0
n = 100000

def generate_array(deck):
    array = np.zeros(6)
    cards = deck
    np.random.shuffle(cards)
    for i in np.arange(6):
        array[i] = cards[i*2] + cards[i*2+1]
    return array

def check_quality(array):
    a = np.flip(np.sort(array))
    if a[0] >=18:
        if a[1] >=17 and a[2] >=13:
            return 3
        if a[1] >=15 and a[2] >=13:
            return 2
        return 0
    if a[0] >=17:
        if a[1] >=17 and a[2] >=14:
            return 3
        if a[1] >=16 and a[2] >=13:
            return 2
        if a[1] >=15 and a[2] >=14:
            return 2
        return 0
    if a[0] >=16:
        if a[1] >=15 and a[2] >=14 and a[3]>=13:
            return 2
        if a[1] >=16 and a[2] >=13 and a[3]>=13:
            return 2
        if a[1] >=15 and a[2] >=13 and a[3]>=12:
            return 1
        if a[1] >=15 and a[2] >=14 and a[3]>=11:
            return 1
        if a[1] >=16 and a[2] >=13 and a[3]>=11:
            return 1
        if a[1] >=16 and a[2] >=11 and a[3]>=11:
            return 0
        if a[1] >=15 and a[2] >=12 and a[3]>=11:
            return 0
    if a[0] >=15 and a[1] >= 15:
        if a[2] >=14 and a[3]>=14:
            return 2
        if a[2] >=14 and a[3]>=12:
            return 1
        if a[2] >=12 and a[3]>=12:
            return 0
    return -1

n_top = 0.0
n_great = 0.0
n_good = 0.0
n_decent = 0.0
n_bad = 0.0
for j in np.arange(n):
    b = generate_array(deck_swing)
    check = check_quality(b)
    if check == -1:
        n_bad += 1.0
    if check == 0:
        n_decent += 1.0
    if check == 1:
        n_good += 1.0
    if check == 2:
        n_great += 1.0
    if check == 3:
        n_top += 1.0

print("Top: ",n_top/n)
print("Great: ",n_great/n)
print("Good: ",n_good/n)
print("Decent: ",n_decent/n)
print("Bad: ",n_bad/n)
print(" ")
print("Sum useable: ",(n_decent+n_good+n_great+n_top)/n)
print("Sum: ",(n_decent+n_good+n_great+n_top+n_bad)/n)


# for j in np.arange(n):
#     a = generate_array(deck_balance)
#     b = generate_array(deck_swing)


# for i in range(n-1):
#     cards = deck_1
#     random.shuffle(cards)
#     i_card = 0
#     n_15 = 0
#     n_14 = 0
#     n_16 = 0
#     for j in [0,1,2,3,4,5]:
#         if cards[i_card] + cards[i_card+1] >= 16:
#             n_16 +=1
#         elif cards[i_card] + cards[i_card+1] >= 15:
#             n_15 +=1
#         elif cards[i_card] + cards[i_card+1] >= 14:
#             n_14 +=1
#         i_card += 2
#     if (n_16 + n_15 >= 3):
#         good_counter += 1
#     if (n_14 >= 1) and (n_15 >= 1) and (n_16 >= 1):
#         good_counter += 1
#     # array.sort()
#     # print(array)
# print('Deck 1: ',good_counter/float(n))

# good_counter = 0.0
# for i in range(n-1):
#     cards = deck_2
#     random.shuffle(cards)
#     i_card = 0
#     n_15 = 0
#     n_14 = 0
#     n_16 = 0
#     for j in [0,1,2,3,4,5]:
#         if cards[i_card] + cards[i_card+1] >= 16:
#             n_16 +=1
#         elif cards[i_card] + cards[i_card+1] >= 15:
#             n_15 +=1
#         elif cards[i_card] + cards[i_card+1] >= 14:
#             n_14 +=1
#         i_card += 2
#     if (n_16 + n_15 >= 3):
#         good_counter += 1
#     elif (n_14 >= 1) and (n_15 >= 1) and (n_16 >= 1):
#         good_counter += 1
#     # array.sort()
#     # print(array)
# print('Deck 2: ',good_counter/float(n))

# good_counter = 0.0
# for i in range(n-1):
#     n_15 = 0
#     n_14 = 0
#     n_16 = 0
#     for j in [0,1,2,3,4,5]:
#         x = sum(np.random.randint(1,high=7,size=3))
#         if x >= 16:
#             n_16 +=1
#         elif x >= 15:
#             n_15 +=1
#         elif x >= 14:
#             n_14 +=1
#     if (n_16 + n_15 >= 3):
#         good_counter += 1
#     elif (n_14 >= 1) and (n_15 >= 1) and (n_16 >= 1):
#         good_counter += 1
#     # array.sort()
#     # print(array)
# print('3d6: ',good_counter/float(n))

# good_counter = 0.0
# for i in range(n-1):
#     n_15 = 0
#     n_14 = 0
#     n_16 = 0
#     for j in [0,1,2,3,4,5]:
#         rolls = np.random.randint(1,high=7,size=4)
#         x = sum(rolls) - min(rolls)
#         if x >= 16:
#             n_16 +=1
#         elif x >= 15:
#             n_15 +=1
#         elif x >= 14:
#             n_14 +=1
#         i_card += 2
#     if (n_16 + n_15 >= 3):
#         good_counter += 1
#     elif (n_14 >= 1) and (n_15 >= 1) and (n_16 >= 1):
#         good_counter += 1
#     # array.sort()
#     # print(array)
# print('4d6 drop low: ',good_counter/float(n))

# good_counter = 0.0
# for i in range(n-1):
#     n_15 = 0
#     n_14 = 0
#     n_16 = 0
#     n_17 = 0
#     n_18 = 0
#     for j in [0,1,2,3,4,5]:
#         rolls = np.random.randint(1,high=7,size=4)
#         x = sum(rolls) - min(rolls)
#         if x >= 18:
#             n_18 +=1
#         elif x >= 17:
#             n_17 +=1
#         elif x >= 16:
#             n_16 +=1
#         elif x >= 15:
#             n_15 +=1
#         elif x >= 14:
#             n_14 +=1
#         array[j] = x
#     if (n_18 + n_17 + n_16 + n_15 >= 3):
#         good_counter += 1
#     elif (n_18 >= 1) and (n_14 + n_15 + n_16 + n_17 >= 1):
#         good_counter += 1
#     elif (n_17 >= 1) and (n_14 + n_15 + n_16 + n_18 >= 1):
#         good_counter += 1
#     elif (n_16 >= 1) and (n_15 + n_16 + n_17 + n_18 >= 1):
#         good_counter += 1
#     elif (n_14 >= 1) and (n_15 >= 1) and (n_16 >= 1):
#         good_counter += 1
#     # array.sort()
#     # print(array)
# print('4d6 drop low: ',good_counter/float(n))

# good_counter = 0.0
# for i in range(n-1):
#     n_15 = 0
#     n_14 = 0
#     n_16 = 0
#     n_17 = 0
#     n_18 = 0
#     for j in [0,1,2,3,4,5]:
#         rolls = np.random.randint(1,high=13,size=1)
#         x = sum(rolls) + 6
#         if x >= 18:
#             n_18 +=1
#         elif x >= 17:
#             n_17 +=1
#         elif x >= 16:
#             n_16 +=1
#         elif x >= 15:
#             n_15 +=1
#         elif x >= 14:
#             n_14 +=1
#         array[j] = x
#     if (n_18 + n_17 + n_16 + n_15 >= 3):
#         good_counter += 1
#     elif (n_18 >= 1) and (n_14 + n_15 + n_16 + n_17 >= 1):
#         good_counter += 1
#     elif (n_17 >= 1) and (n_14 + n_15 + n_16 + n_18 >= 1):
#         good_counter += 1
#     elif (n_16 >= 1) and (n_15 + n_16 + n_17 + n_18 >= 1):
#         good_counter += 1
#     elif (n_14 >= 1) and (n_15 >= 1) and (n_16 >= 1):
#         good_counter += 1
#     # array.sort()
#     # print(array)
# print('1d12+6: ',good_counter/float(n))

# good_counter = 0.0
# for i in range(n-1):
#     n_15 = 0
#     n_14 = 0
#     n_16 = 0
#     n_17 = 0
#     n_18 = 0
#     for j in [0,1,2,3,4,5]:
#         rolls = np.random.randint(1,high=11,size=1)
#         x = sum(rolls) + 7
#         if x >= 18:
#             n_18 +=1
#         elif x >= 17:
#             n_17 +=1
#         elif x >= 16:
#             n_16 +=1
#         elif x >= 15:
#             n_15 +=1
#         elif x >= 14:
#             n_14 +=1
#         array[j] = x
#     if (n_18 + n_17 + n_16 + n_15 >= 3):
#         good_counter += 1
#     elif (n_18 >= 1) and (n_14 + n_15 + n_16 + n_17 >= 1):
#         good_counter += 1
#     elif (n_17 >= 1) and (n_14 + n_15 + n_16 + n_18 >= 1):
#         good_counter += 1
#     elif (n_16 >= 1) and (n_15 + n_16 + n_17 + n_18 >= 1):
#         good_counter += 1
#     elif (n_14 >= 1) and (n_15 >= 1) and (n_16 >= 1):
#         good_counter += 1
#     # array.sort()
#     # print(array)
# print('1d10+7: ',good_counter/float(n))