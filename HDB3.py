
import matplotlib.pyplot as plt
import numpy as np

# User input for data and bit rate
data = list(map(int, input("Enter binary sequence (e.g., 1100011): ")))
bit_rate = float(input("Enter bit rate (bits per second): "))

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


# HDB3 Encoding function (simplified)
def hdb3(data):
    signal = ami(data)  # Start with AMI encoding
    zero_count = 0
    last_violation = -1
    for i in range(len(data)):
        if data[i] == 0:
            zero_count += 1
        else:
            zero_count = 0
        if zero_count == 4:
            if sum(signal[:i]) % 2 == 0:
                signal[i-3:i+1] = [last_violation, 0, 0, last_violation]
            else:
                signal[i-3:i+1] = [0, 0, 0, -last_violation]
            last_violation *= -1
            zero_count = 0
    return signal

# Plot the HDB3 waveform
def plot_hdb3(data, bit_rate):
    encoded_data = hdb3(data)
    t = np.arange(0, len(data) / bit_rate, 1 / (bit_rate * 2))
    plt.step(t, np.repeat(encoded_data, 2), where='post')
    plt.ylim(-2, 2)
    plt.title("HDB3 Encoding")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

plot_hdb3(data, bit_rate)
