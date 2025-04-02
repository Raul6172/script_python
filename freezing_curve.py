#Unit 2
#Script: Freezing curve
import matplotlib.pyplot as plt
import numpy as np
import os

print("**********FREEZING CURVE*********")
#Store data and check it on screen
data = np.array([[0,20],[20,8],[40,5],[60,1],[80,0],[100,-2.5],[120,-4],[140,-5.5],[160,-7],[180,-9],[190,-10]])
print(data)
#Plot configuration
plt.grid()
plt.title('Freezing curve')
plt.xlabel('Time [s]')
plt.ylabel('Temprature [ºC]')
#PLot
plt.plot(data[:, 0],data[:, 1],marker='o', color='r', linestyle='--')

folder_path =''

# Save plot
file_name = 'freezing_curve.png'
full_path = os.path.join(folder_path, file_name)
plt.savefig(full_path)

# Show the plot (if necesary)
plt.show()