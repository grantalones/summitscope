from summit_scope_app.models import Mountain

# Define a list of known mountains with their attributes
mountains = [
    {'name': 'Mount Everest', 'elevation': 8848, 'latitude': 27.9881, 'longitude': 86.9250},
    {'name': 'K2', 'elevation': 8611, 'latitude': 35.8815, 'longitude': 76.5132},
    {'name': 'Kangchenjunga', 'elevation': 8586, 'latitude': 27.7025, 'longitude': 88.1466},
    # Add more mountains as needed
]

# Loop through the list of mountains and create a Mountain instance for each
for mountain_data in mountains:
    if Mountain.objects.values()
    mountain = Mountain.objects.create(**mountain_data)
    print(f"Created mountain: {mountain.name}")
