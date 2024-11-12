import matplotlib.pyplot as plt
import numpy as np

# User input for data and bit rate
data = list(map(int, input("Enter binary sequence : ")))
bit_rate = float(input("Enter bit rate (bits per second): "))

# AMI Encoding function
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

# Plot the AMI waveform
def plot_ami(data, bit_rate):
    encoded_data = ami(data)
    # Adjust time array to match the doubled length of encoded_data
    t = np.arange(0, len(data) * 2 / bit_rate, 1 / bit_rate)
    
    # Make sure the time array matches the length of the encoded data
    plt.step(t, np.repeat(encoded_data, 2), where='post')
    plt.ylim(-2, 2)
    plt.title("AMI Encoding")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

plot_ami(data, bit_rate)
