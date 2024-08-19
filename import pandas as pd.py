import pandas as pd
import matplotlib.pyplot as plt

# Load data from log file
data = pd.read_csv('sensor_data.csv')

# Plot data
plt.figure(figsize=(10, 5))
plt.plot(data['Time'], data['Temperature'], label='Temperature (°C)')
plt.plot(data['Time'], data['Distance'], label='Distance (cm)')
plt.xlabel('Time')
plt.ylabel('Sensor Readings')
plt.title('Sensor Data Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()