import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

fs = 8000
n, w = sig.buttord(1200 / 4000, 1500 / 4000, 1, 50)
[b, a] = sig.butter(n, w)
w, h = sig.freqz(b, a, 512, fs=8000)
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(h))

plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(h)))
plt.tight_layout()
plt.show()
