import os


def forecast(*args):
    final_list = []

    weather_dict = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': [],
    }
    for key, value in args:
        weather_dict[value].append(key)

    for key, value in weather_dict.items():
        weather_dict[key] = sorted(value)

        for val in weather_dict[key]:
            final_list.append(f'{val} - {key}')

    return os.linesep.join(final_list)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
