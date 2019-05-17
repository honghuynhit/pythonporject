point = {'x':3,'y':4}
print(point['y'])
print(point)
point['z'] = 123
print(point)
# Copy object
pointcopy = point.copy()

# Clear object
point.clear()

print(point)
# print pointcopy
print(pointcopy)

# print all key
print(pointcopy.keys())
# print all value
print(pointcopy.values())
