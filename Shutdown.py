import os
import time

# Get the current operating system.
operating_system = os.name

# Define the shutdown command based on the operating system.
if operating_system == 'nt':
    # Windows.
    shutdown_command = 'shutdown /s /t 0'
elif operating_system == 'posix':
    # Linux or macOS.
    shutdown_command = 'shutdown -h now'
else:
    # Unsupported operating system.
    raise ValueError('Unsupported operating system: {}'.format(operating_system))

# Print a message to the user.
print('Your computer will shut down in 5 seconds.')

# Wait for 5 seconds.
time.sleep(5)

# Execute the shutdown command.
os.system(shutdown_command)