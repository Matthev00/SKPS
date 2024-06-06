import matplotlib.pyplot as plt
import requests

api_url = "http://10.42.0.124:9005"

def update_graph(new_data1):
    data_list1.append(new_data1)

    plt.xlim(0, len(data_list1))
    plt.ylim(0, 100)

    plt.plot(data_list1, color='red')
    plt.title('distance')

    plt.draw()


data_list1 = []

plt.title("Wizualizacja danych w czasie rzeczywistym")
plt.xlabel("Krok")
plt.ylabel("Wartość")


while True:
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        update_graph(data["distance"])
        plt.pause(1)

    else:
        print("Błąd podczas pobierania danych z API")

