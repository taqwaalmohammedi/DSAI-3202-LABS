import os
import time
from src.utils import latest_temperatures, temperature_averages, lock

def initialize_display():
    """Prints the initial layout for temperature monitoring."""
    with lock:
        print("Current temperatures:\n")
        print(f"Latest Temperatures: Sensor 0: {latest_temperatures.get(0, 'N/A')}°C  "
              f"Sensor 1: {latest_temperatures.get(1, 'N/A')}°C  "
              f"Sensor 2: {latest_temperatures.get(2, 'N/A')}°C")
        for i in range(3):
            print(f"Sensor {i} Average: {temperature_averages.get(i, 'N/A')}°C")
        print("\nUpdating every 5 seconds...\n")

def update_display():
    """Refreshes temperature display every 5 seconds."""
    initialize_display()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        with lock:
            print("Current temperatures:\n")
            print(f"Latest Temperatures: Sensor 0: {latest_temperatures.get(0, 'N/A')}°C  "
                  f"Sensor 1: {latest_temperatures.get(1, 'N/A')}°C  "
                  f"Sensor 2: {latest_temperatures.get(2, 'N/A')}°C")
            for i in range(3):
                print(f"Sensor {i} Average: {temperature_averages.get(i, 'N/A')}°C")
        time.sleep(5)
