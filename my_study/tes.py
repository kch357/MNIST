import sys, os
sys.path.append(os.path.abspath("../deep-learning-from-scratch"))
sys.path.append(os.path.abspath("../deep-learning-from-scratch/ch04"))

import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist

# 데이터 로드
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

# 확인할 이미지의 인덱스 선택
index = 0 
img = x_train[index]
label = t_train[index]

# 데이터 형태 변환 (1차원 784배열 -> 28x28 2차원 배열)
img = img.reshape(28, 28)

# 이미지 시각화
plt.imshow(img, cmap='gray')
plt.title(f"Label: {np.argmax(label)}")
plt.savefig('my_graph.png')