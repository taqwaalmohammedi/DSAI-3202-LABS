import time
from src.utils import latest_temperatures, temperature_averages, lock
from collections import defaultdict

temperature_history = defaultdict(list)

def process_temperatures():
    """Computes the average temperature for each sensor every 5 seconds."""
    while True:
        with lock:
            for sensor_id, temp in latest_temperatures.items():
                temperature_history[sensor_id].append(temp)
                
                # Keep only the last 5 readings to compute moving average
                if len(temperature_history[sensor_id]) > 5:
                    temperature_history[sensor_id].pop(0)

                # Compute individual moving average
                temperature_averages[sensor_id] = sum(temperature_history[sensor_id]) / len(temperature_history[sensor_id])

        time.sleep(5)
