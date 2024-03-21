import numpy as np
import matplotlib.pyplot as plt


def generate_pwm_signal_with_frequency_modulation(min_frequency, max_frequency, duration):
    t = np.linspace(0, duration, int(44100 * duration / 2), endpoint=False)
    freq_range = np.linspace(min_frequency, max_frequency, len(t))
    pwm_signal = np.zeros_like(t)

    for i, f in enumerate(freq_range):
        pwm_signal[i] = np.sin(2 * np.pi * f * t[i]) > 0

    t = np.concatenate((t, t + duration / 2))
    pwm_signal = np.concatenate((pwm_signal, pwm_signal[::-1]))

    return t, pwm_signal

def main():
    min_frequency = 30  
    max_frequency = 1000  
    duration = 0.05  

    t, pwm_signal = generate_pwm_signal_with_frequency_modulation(min_frequency, max_frequency, duration)

    plt.plot(t, pwm_signal)
    plt.title("PWM")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    plt.savefig("cw2/praca_domowa/frequency_modulation.png")


if __name__ == "__main__":
    main()
