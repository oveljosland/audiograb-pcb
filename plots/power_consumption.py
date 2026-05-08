from pathlib import Path
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

files = [
    "Power_consumption/TEST1.CSV"
]

line_names = {
    "Power_consumption/TEST1.CSV": "Power Consumption Test 1"
}


plt.figure(figsize=(12,6))

for file in files:
    # Try common oscilloscope CSV formats
    df = pd.read_csv(file, sep=';', comment='#')
    
    # Convert columns to numeric, coercing errors to NaN
    df["U2[V]"] = pd.to_numeric(df["U2[V]"], errors='coerce')
    df["I2[A]"] = pd.to_numeric(df["I2[A]"], errors='coerce')

    # Parse timestamp
    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"],
        format="%H:%M:%S:%f"
    )
    
    time = df["Timestamp"]
    signal = df["I2[A]"] 
    
    label = line_names[file]
    plt.plot(time, signal, label=label)

plt.xlabel("Time [s]")
plt.ylabel("Ampere [A]")
plt.title("Power Consumption Test 1")
plt.legend()
plt.grid(True)
plt.show()

#output_path = "sd_overlay_plot.png"

#plt.savefig(output_path, bbox_inches='tight', dpi=300)

#print(f"Saved plot to: {output_path}")
