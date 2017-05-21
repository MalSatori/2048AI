import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2


train_data = np.load('training_data.npy')
print(len(train_data))
df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

upleft = []
upright = []
downleft = []
downright = []

shuffle(train_data)

for data in train_data:
    # [UpRight, UpLeft, DownLeft, DownRight]
    img = data[0]
    choice = data[1]
    cv2.imshow('test',img)
    if choice == [0, 1, 0, 0]:
        upleft.append([img, choice])
    elif choice == [1, 0, 0, 0]:
        upright.append([img, choice])
    elif choice == [0, 0, 1, 0]:
        downleft.append([img, choice])
    elif choice == [0, 0, 0, 1]:
        downright.append([img, choice])
    else:
        print('No matches.')

upleft = upleft[:len(upright)][:len(downleft)][:len(downright)]
upright = upright[:len(upleft)][:len(downleft)][:len(downright)]
downleft = downleft[:len(upleft)][:len(upright)][:len(downright)]
downright = downright[:len(upleft)][:len(upright)][:len(downleft)]

final_data = upleft + upright + downleft + downright

shuffle(final_data)

print(len(final_data))
np.save('training_data_v2.npy', final_data)


# for data in train_data:
#     img = data[0]
#     choice = data[1]
#     cv2.imshow('test',img)
#     print(choice)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break