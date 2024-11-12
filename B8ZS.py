import matplotlib.pyplot as plt
import numpy as np


# User input for data and bit rate
data = list(map(int, input("Enter binary sequence (e.g., 1100011): ")))
bit_rate = float(input("Enter bit rate (bits per second): "))
# B8ZS Encoding function (simplified)
def b8zs(data):
    signal = ami(data)  # Start with AMI encoding
    zero_count = 0
    for i in range(len(data)):
        if data[i] == 0:
            zero_count += 1
        else:
            zero_count = 0
        if zero_count == 8:
            # Replace 8 zeros with a special pattern
            signal[i-7:i+1] = [signal[i-1], 0, 0, signal[i-1], 0, 0, signal[i-1], 0]
            zero_count = 0
    return signal


# AMI Encoding function (needed for HDB3)
def ami(data):
    signal = []
    last_polarity = -1
    for bit in data:
        if bit == 1:
            last_polarity *= -1
            signal.append(last_polarity)
        else:
            signal.append(0)
    return signal

# Plot the B8ZS waveform
def plot_b8zs(data, bit_rate):
    encoded_data = b8zs(data)
    t = np.arange(0, len(data) / bit_rate, 1 / (bit_rate * 2))
    plt.step(t, np.repeat(encoded_data, 2), where='post')
    plt.ylim(-2, 2)
    plt.title("B8ZS Encoding")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

plot_b8zs(data, bit_rate)
