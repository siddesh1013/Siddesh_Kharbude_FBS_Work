### Write a program to accept distance in km and convert it into meters and centimeters both. 

Distance_km = int(input('Enter distance in km: '))

Distance_meters = Distance_km * 1000
Distance_centimeters = Distance_km * 100000

print(f'Distance in meters: {Distance_meters}')
print(f'Distance in centimeters: {Distance_centimeters}')