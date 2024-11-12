import numpy as np

import matplotlib.pyplot as plt

def pcm_encoding(analog_signal, quantization_levels):
    # Normalize the analog signal to the range [0, 1]
    normalized_signal = (analog_signal - np.min(analog_signal)) / (np.max(analog_signal) - np.min(analog_signal))

    # Quantize the normalized signal
    quantized_signal = np.round(normalized_signal * (quantization_levels - 1))

    return quantized_signal

def generate_analog_signal(time, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * time) + amplitude * np.sin(2 * np.pi * (2 * frequency) * time)

def main():
    # Generate a sample analog signal (sine wave)
    time = np.arange(0, 1, 0.001)
    amp = float(input("Enter Amplitude of signal:\n"))
    freq = float(input("Enter frequency of signal:\n"))
    analog_signal = generate_analog_signal(time, amp, freq)

    # Set the number of quantization levels (bits per sample)
    quantization_levels = 8

    # PCM encoding
    pcm_encoded_signal = pcm_encoding(analog_signal, quantization_levels)

    # Plot the original analog signal and the PCM encoded signal
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(time, analog_signal)
    plt.title('Original Analog Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.subplot(2, 1, 2)
    plt.step(time, pcm_encoded_signal, linewidth=1)
    plt.title('PCM Encoded Signal')
    plt.xlabel('Time')
    plt.ylabel('Quantized Level')

    plt.tight_layout()
    plt.show()

    print(pcm_encoded_signal)

if __name__ == "__main__":
    main()