import numpy as np

import matplotlib.pyplot as plt

# Take user inputs
sampling_frequency = float(input("Enter the sampling frequency (in Hz): "))
signal_duration = float(input("Enter the signal duration (in seconds): "))
message_frequency_cosine = float(input("Enter the message frequency for cosine (in Hz): "))
message_frequency_sine = float(input("Enter the message frequency for sine (in Hz): "))
message_amplitude_cosine = float(input("Enter the message amplitude for cosine: "))
message_amplitude_sine = float(input("Enter the message amplitude for sine: "))

# Initialize the time vector
time = np.arange(signal_duration * sampling_frequency) / sampling_frequency

# Calculate the message signal
message_cosine = message_amplitude_cosine * np.cos(2 * np.pi * message_frequency_cosine * time)
message_sine = message_amplitude_sine * np.sin(2 * np.pi * message_frequency_sine * time)
message = message_cosine + message_sine

# The component with the highest frequency carries the bandwidth
bandwidth = max(message_frequency_cosine, message_frequency_sine)  # in Hertz (Hz)

# Define delta sampling frequency as 4 times the Nyquist rate
nyquist_rate_factor = 4
delta_sampling_frequency = nyquist_rate_factor * 2 * bandwidth  # in Hertz (Hz)

delta_epsilon = 0.2  # define step size in seconds (s)

# Define sample time array
delta_time = np.arange(signal_duration * delta_sampling_frequency) / delta_sampling_frequency

# Calculate the sampled message signal
sampled_message_cosine = message_amplitude_cosine * np.cos(2 * np.pi * message_frequency_cosine * delta_time)
sampled_message_sine = message_amplitude_sine * np.sin(2 * np.pi * message_frequency_sine * delta_time)
sampled_message = sampled_message_cosine + sampled_message_sine

# Allocate memory
prediction = np.zeros(len(sampled_message))
modulated = np.zeros(len(sampled_message))

# Go through the modulation loop
for i in range(1, len(sampled_message)):
    amplitude_diff = sampled_message[i] - prediction[i - 1]
    modulated[i] = (2 * int(amplitude_diff > 0) - 1) * delta_epsilon
    prediction[i] = prediction[i - 1] + modulated[i]

# Define plot parameters
plt.figure(figsize=(20, 12))
plot_time = 0.1

# Plot the message and predicted signals
plt.subplot(2, 1, 1)
plt.plot(time, message, 'b')
plt.step(delta_time, prediction, 'r', where='post')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Message and Predicted Signals')
plt.legend(['Message signal', 'Predicted signal'])
plt.axis([0, plot_time, -2, 2])
plt.xticks(np.arange(0, plot_time, plot_time / 10))
plt.grid()

# Plot the transmitted DM signal
plt.subplot(2, 1, 2)
plt.stem(delta_time, modulated, 'b')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Transmitted DM Signal')
plt.axis([0, plot_time, -2 * delta_epsilon, 2 * delta_epsilon])
plt.xticks(np.arange(0, plot_time, plot_time / 10))
plt.grid()

plt.show()