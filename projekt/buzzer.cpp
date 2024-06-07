#include <iostream>
#include <fstream>
#include <cmath>
#include <unistd.h>
#include <chrono>
#include <thread>

#define GPIO_PIN "24"
#define GPIO_PATH "/sys/class/gpio/"

void writeFile(const std::string& path, const std::string& value) {
    std::ofstream fs;
    fs.open(path);
    if (!fs.is_open()) {
        std::cerr << "Error: could not open " << path << std::endl;
        return;
    }
    fs << value;
    fs.close();
}

int main() {
    // Eksportowanie pinu
    writeFile(GPIO_PATH "export", GPIO_PIN);
    usleep(100000); // Czekaj na zakończenie eksportowania

    // Ustawienie kierunku pinu na wyjście
    writeFile(GPIO_PATH "gpio" GPIO_PIN "/direction", "out");

    const double MAX_TIME = 10.0;
    double current_time = 0.0;
    const double frequency = 100.0;
    const double step = 0.0001;

    while (current_time < MAX_TIME) {
        double duty_cycle = std::abs(std::sin(current_time * M_PI) / 2.0);
        double period = 1.0 / frequency;
        if (std::fmod(current_time, period) < duty_cycle * period) {
            writeFile(GPIO_PATH "gpio" GPIO_PIN "/value", "1"); // Włącz buzzer
        } else {
            writeFile(GPIO_PATH "gpio" GPIO_PIN "/value", "0"); // Wyłącz buzzer
        }
        current_time += step;
        std::this_thread::sleep_for(std::chrono::microseconds(static_cast<int>(step * 1000000)));
    }

    // Wyeksportowanie pinu
    writeFile(GPIO_PATH "unexport", GPIO_PIN);

    return 0;
}
