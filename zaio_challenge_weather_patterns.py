import numpy as np

def generate_weather_data():
    np.random.seed(42)
    days = np.arange(1, 366)
    minimum_temps = np.random.randint(-10, 16, size = 365)
    maximum_temps = np.random.randint(5, 36, size = 365)
    weather_data = np.column_stack((days, minimum_temps, maximum_temps))
    return weather_data

data = generate_weather_data()
print(data)

def basic_statistics(data):
    min_temps = data[:, 1]
    max_temps = data[:, 2]

    avg_min = np.mean(min_temps)
    avg_max = np.mean(max_temps)

    max_temp = np.max(max_temps)
    min_temp = np.min(min_temps)

    return avg_min, avg_max, max_temp, min_temp

def daily_temperature_range(data):
    temp_range = data[:, 2] - data[:, 1]
    max_range_value = np.max(temp_range)
    max_range_day = int(data[np.argmax(temp_range), 0])
    return temp_range, (max_range_day, max_range_value)


def identify_heatwaves(data):
    max_temps = data[:, 2]
    is_hot = max_temps > 30

    padded = np.pad(is_hot.astype(int), (1, 1))
    diff = np.diff(padded)
    starts = np.where(diff == 1)[0]
    ends = np.where(diff == -1)[0] - 1

    heatwaves = []
    for s, e in zip(starts, ends):
        if e - s + 1 >= 3:
            heatwaves.append((int(data[s, 0]), int(data[e, 0])))

    return len(heatwaves), heatwaves

if __name__ == "__main__":
    data = generate_weather_data()
    
    print("=== Basic Statistics ===")
    stats = basic_statistics(data)
    print(f"Average Min Temp: {stats[0]:.2f}°C")
    print(f"Average Max Temp: {stats[1]:.2f}°C")
    print(f"Highest Temp: {stats[2]}°C on Day {stats[3]}")
    print(f"Lowest Temp: {stats[4]}°C on Day {stats[5]}")
    
    print("\n=== Daily Temp Range ===")
    ranges, max_day, max_range = daily_temperature_range(data)
    print(f"Largest range of {max_range}°C on Day {max_day}")
    
    print("\n=== Heatwaves ===")
    total_heatwaves, heatwave_periods = identify_heatwaves(data)
    print(f"Total Heatwaves: {total_heatwaves}")
    print("Heatwave Periods:", heatwave_periods)

