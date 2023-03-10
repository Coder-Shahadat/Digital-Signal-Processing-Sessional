import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np

fs = 8000
N = 50
fc = np.array([2000, 2050])
b = sig.firwin(N + 1, fc, fs=fs, window='hamming', pass_zero='bandstop')
w, h_freq = sig.freqz(b, fs=fs)
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(h_freq))
plt.xlabel('frequency(Hz)')
plt.ylabel('Magnitude')
plt.subplot(2, 1, 2)
plt.plot(w, np.angle(h_freq))
plt.xlabel('frequency(Hz)')
plt.ylabel('Phase(angel)')
plt.tight_layout()
plt.show()
