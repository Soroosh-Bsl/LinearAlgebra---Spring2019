import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys

img_path = r"image.jpg"
img = Image.open(img_path)

img = np.asarray(img)
channel = [[], [], []]
channel[0] = [[j[0] for j in i] for i in img]
channel[1] = [[j[1] for j in i] for i in img]
channel[2] = [[j[2] for j in i] for i in img]

print("Enter K (approximation rank: ")
print("K = ", end='')
K = int(input())

if K > min(np.asarray(channel[0]).shape):
    print("Rank more than allowed! Error!")
    sys.exit()

U = [[] for i in range(len(channel))]
S = [[] for i in range(len(channel))]
V_T = [[] for i in range(len(channel))]

img = np.zeros(img.shape)
for i in range(len(channel)):
    U[i], S[i], V_T[i] = np.linalg.svd(channel[i], full_matrices=True)
    S_temp = np.zeros(np.asarray(channel[i]).shape)
    S_temp[:K, :K] = np.diag(S[i][:K])
    channel[i] = np.matmul(U[i], np.matmul(S_temp, V_T[i]))
    img[..., i] = channel[i]

img = np.rint(img)
img = img.astype(int)
img = np.clip(img, 0, 255)
plt.imshow(img)
plt.show()
