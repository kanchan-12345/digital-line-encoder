import numpy as np

import matplotlib.pyplot as plt

# User input for data and bit rate
data = list(map(int, input("Enter binary sequence (e.g., 1100011): ")))
bit_rate = float(input("Enter bit rate (bits per second): "))

# Differential Manchester Encoding function
def diff_manchester(data):
    # Initialize signal array and the last level for encoding
    signal = []
    last_level = 1 # assume that previous level is 1
    
    for bit in data:
        if bit == 0:
            last_level = -last_level
            signal.extend([last_level, -last_level])
        else:
            signal.extend([last_level, -last_level])
    
    return signal

def plot_signal(signal, bit_rate):
    # Calculate time period for each half bit
    T = 1 / (2 * bit_rate)
    
    # Create time array
    time = np.arange(0, len(signal) * T, T)
    
    # Plot the signal
    plt.step(time, signal, where='post')
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Differential Manchester Encoding")
    plt.grid(True)
    plt.show()

# Encode the data using Differential Manchester Encoding
signal = diff_manchester(data)
plot_signal(signal, bit_rate)