import matplotlib.pyplot as plt
import numpy as np

# User input for data and bit rate
data = list(map(int, input("Enter binary sequence (e.g., 11011001): ")))
bit_rate = float(input("Enter bit rate (bits per second): "))

# Manchester Encoding function
def manchester(data):
    encoded_signal = []
    for bit in data:
        if bit == 0:
            encoded_signal.extend([1, -1])  # 0 -> high-to-low
        else:
            encoded_signal.extend([-1, 1])  # 1 -> low-to-high
    return encoded_signal

# Plot the Manchester waveform
def plot_manchester(data, bit_rate):
    encoded_data = manchester(data)
    # Adjust time array to match the doubled length of encoded_data
    t = np.arange(0, len(data) * 2 / bit_rate, 1 / (bit_rate * 2))

    # Plot the Manchester encoded signal
    plt.step(t, np.repeat(encoded_data, 2), where='post')
    plt.ylim(-2, 2)
    plt.title("Manchester Encoding")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

# Call the plotting function with user input
plot_manchester(data, bit_rate)

