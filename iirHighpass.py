import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

fs = 8000
[n, w] = sig.buttord(1200 / 4000, 1500 / 4000, 1, 50)
[b, a] = sig.butter(n, w, btype='highpass')
w, h = sig.freqz(b, a, 512, fs=fs)
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(h))

plt.subplot(2, 1, 2)
plt.plot(w, np.angle(h))
plt.tight_layout()
plt.show()