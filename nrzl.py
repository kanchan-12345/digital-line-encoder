import matplotlib.pyplot as plt
import numpy as np

# User input for data and bit rate
data = list(map(int, input("Enter binary sequence (e.g., 1100011): ")))
bit_rate = float(input("Enter bit rate (bits per second): "))

# NRZ-L Encoding function
def nrz_l(data):
    return [1 if bit == 1 else -1 for bit in data]

# Plot the NRZ-L waveform
def plot_nrz_l(data, bit_rate):
    encoded_data = nrz_l(data)
    # Adjust time array to match the doubled length of encoded_data
    t = np.arange(0, len(data) / bit_rate, 1 / (bit_rate * 2))

    # Plot the NRZ-L encoded signal
    plt.step(t, np.repeat(encoded_data, 2), where='post')
    plt.ylim(-2, 2)
    plt.title("NRZ-L Encoding")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

# Call the plotting function with user input
plot_nrz_l(data, bit_rate)
