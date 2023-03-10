import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

N = 50
fs = 8000
fc = np.array([1200, 1400, 2500, 2600])
b = sig.firwin(N + 1, fc, fs=fs, window='hamming', pass_zero='bandpass')
w, h_freq = sig.freqz(b, fs=fs)
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(h_freq))
plt.xlabel('frequency(Hz)')
plt.ylabel('Magnitude')

plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(h_freq)))
plt.xlabel('frequency(Hz)')
plt.ylabel('Phase(angel)')
plt.show()
