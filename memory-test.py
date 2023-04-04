import psutil

# Get the total physical memory available on the system, in bytes
total_memory = psutil.virtual_memory().total

# Get the amount of free physical memory available on the system, in bytes
available_memory = psutil.virtual_memory().available

# Print the total and available memory in gigabytes
print(f"Total memory: {total_memory / (1024 ** 3):.2f} GB")
print(f"Available memory: {available_memory / (1024 ** 3):.2f} GB")