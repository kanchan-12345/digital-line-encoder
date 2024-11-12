import matplotlib.pyplot as plt
import numpy as np

# User input for data and bit rate
data = list(map(int, input("Enter binary sequence (e.g., 11100101): ")))
bit_rate = float(input("Enter bit rate (bits per second): "))

# NRZ-I Encoding function
def nrz_i(data):
    encoded_signal = []
    last_level = -1  # Initial level, can start at either -1 or 1
    for bit in data:
        if bit == 1:
            last_level *= -1  # Toggle level on '1'
        encoded_signal.append(last_level)
    return encoded_signal

# Plot the NRZ-I waveform
def plot_nrz_i(data, bit_rate):
    encoded_data = nrz_i(data)
    # Adjust time array to match the doubled length of encoded_data
    t = np.arange(0, len(data) / bit_rate, 1 / (bit_rate * 2))

    # Plot the NRZ-I encoded signal
    plt.step(t, np.repeat(encoded_data, 2), where='post')
    plt.ylim(-2, 2)
    plt.title("NRZ-I Encoding")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

# Call the plotting function with user input
plot_nrz_i(data, bit_rate)
