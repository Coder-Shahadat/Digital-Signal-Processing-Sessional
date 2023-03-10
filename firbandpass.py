import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

fs = 8000  # sampling rate
N = 50  # order of filer
fc = np.array([1200, 1800])  # cutoff frequency
# wc = 2 * fc / fs  # normalized cutoff frequency to the nyquist frequency
b = sig.firwin(N + 1, fc, fs=fs, window='hamming', pass_zero='bandpass')
w, h_freq = sig.freqz(b, fs=fs)
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(h_freq))  # magnitude
plt.xlabel('frequency(Hz)')
plt.ylabel('Magnitude')
plt.subplot(2, 1, 2)
plt.plot(w, np.angle(h_freq))  # phase
plt.xlabel('frequency(Hz)')
plt.ylabel('Phase(angel)')
plt.show()
