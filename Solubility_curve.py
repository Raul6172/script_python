#Unit 3
#Script: Solubility curve + Interpolation
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import scipy.interpolate

print("************SOLUBILITY CURVE KNO3***********")

# Read Excel file
excel_file = 'solubility.xlsx'
df = pd.read_excel(excel_file)

# DataFrame conversation to NumPy array
data = df.to_numpy()

print(data)

#Ask value
temperature = int(input("What is the temperature to interpolate?: "))

# #Find value. Interpolation
interp_func = scipy.interpolate.interp1d(data[:, 0], data[:, 1], kind='linear')
sol_interp = interp_func(temperature)
print(f"The solubility is {sol_interp:.2E} g/100g H2O")

#Plot configuration
plt.grid()
plt.title('Solubility curve + Interpolation')
plt.xlabel('Time [s]')
plt.ylabel('Temperature [ºC]')
#Plot
plt.plot(data[:, 0],data[:, 1],marker='o', color='r', linestyle='--')

#Plot point
plt.scatter(temperature, sol_interp, color='blue', marker='o', label='Interpolated Solubility')
plt.legend()

folder_path = ''

# Save plot
file_name = 'solubility_curve_interpolation.png'
full_path = os.path.join(folder_path, file_name)
plt.savefig(full_path)

# Show the plot (if necesary)
plt.show()