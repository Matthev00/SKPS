import numpy as np
import matplotlib.pyplot as plt


def generate_variable_fill_pwm(frequency, fill):
    dt = 1 / (frequency * 10000)
    t = np.arange(0, 1, dt)
    pwm_signal = np.zeros(len(t))
    pwm_signal[: int(fill * len(t))] = 1
    return t, pwm_signal


def generate_variable_fill_pwm_signal(min_fill, max_fill, step_fill):
    t_full, pwm_full = [], []
    fill_levels = list(range(min_fill, max_fill + step_fill, step_fill)) + list(
        range(max_fill, min_fill - step_fill, -step_fill)
    )
    for index, fill in enumerate(fill_levels):
        t, pwm_signal = generate_variable_fill_pwm(1, fill / 100)
        t = t + index
        t_full = np.concatenate((t_full, t))
        pwm_full = np.concatenate((pwm_full, pwm_signal))
    return t_full, pwm_full


def main():
    min_fill = 10  
    max_fill = 90  
    step = 5  

    t, pwm_signal = generate_variable_fill_pwm_signal(min_fill, max_fill, step)

    plt.plot(t, pwm_signal)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("PWM Signal with Increasing and Decreasing Fill")
    plt.savefig("cw2/praca_domowa/PWM_fill.png")
    plt.show()


if __name__ == "__main__":
    main()