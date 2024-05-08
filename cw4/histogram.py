import matplotlib.pyplot as plt
from pathlib import Path

for subdir in Path(".").glob("z5?"):
    clients = []

    for client in sorted(subdir.glob("cli_?.txt"), key=lambda f: f.name):
        readings = []
        with client.open() as file:
            for line in file:
                tokens = line.split()
                readings.append(int(tokens[-1]))
            clients.append(readings)

    plt.clf()
    plt.hist(clients, label=[f"Klient {idx}" for idx, _ in enumerate(clients)], bins=20)
    plt.legend()
    plt.xlabel("czas wysłania [mikrosekundy]")
    plt.ylabel("Zapytania")
    plt.savefig(subdir / "hist.png")
