import numpy as np

deck_balance = np.array([3,4,5,5,5,6,6,7,7,7,8,9])
deck_balance2 = np.array([3,3,4,4,6,6,6,7,7,8,9,9])
deck_swing = np.array([2,2,4,4,5,6,7,8,8,8,9,9])
deck_custom = np.array([2,2,4,4,6,6,7,7,8,8,9,9])
# print(sum(deck_custom))

def generate_array(deck):
    array = np.zeros(6)
    cards = deck
    np.random.shuffle(cards)
    for i in np.arange(6):
        array[i] = cards[i*2] + cards[i*2+1]
    return array

deck = deck_custom
print("Total deck: ", sum(deck))
print("Total standard array: ", sum([15, 14, 13, 12, 10, 8]))
print(generate_array(deck))

# i_custom = 0
# i_balance2 = 0
# i_swing = 0
# n_even = 0
# for i in range(10000):
#     stats = generate_array(deck_balance2)
#     if np.max(stats) > 15: i_balance2 += 1
#     stats = generate_array(deck_custom)
#     if np.max(stats) > 15: i_custom += 1
#     stats = generate_array(deck_swing)
#     if np.max(stats) > 15: i_swing += 1
#     n_even += np.size()

# print("balance:", i_balance2/100.0)
# print("swing:", i_swing/100.0)
# print("custom:", i_custom/100.0)