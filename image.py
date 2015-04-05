from scipy import misc
l=misc.lena()
misc.imsave('lena.png',l)

import matplotlib.pyplot as plt
plt.imshow(l)
plt.show()