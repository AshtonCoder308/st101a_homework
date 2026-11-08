# =========== Please do not change the code here ===========
import pickle
from distance_util import get_average_group_distance, get_distance

with open('../data/handwritten_digits.pkl', 'rb') as f:
    digit_train_0, digit_train_3, digit_test = pickle.load(f)

# =========== start your code here for Q4 parts 4-6 ===========

# Part 4

required_img_1 = digit_test[0]
required_img_2 = digit_train_0[0]
required_img_3 = digit_train_3[0]

required_dist_1 = get_distance(required_img_1, required_img_2)
required_dist_2 = get_distance(required_img_1, required_img_3)

# Part 5

predicted_labels = []

for i in digit_test:
    distance_1 = get_average_group_distance(i, digit_train_0)
    distance_2 = get_average_group_distance(i, digit_train_3)
    if distance_1 <= distance_2:
        predicted_labels.append(0)
    else:
        predicted_labels.append(3)

print(predicted_labels)

actual = [0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3]

counter = 0

for i in range(10):
    if predicted_labels[i] == actual[i]:
        counter += 1

accuracy = counter / 10
print(accuracy)