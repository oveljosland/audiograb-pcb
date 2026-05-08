from pathlib import Path
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

files = [
    "direct_generator_to_probe/BASELI01.CSV",
    "Stump_test/SD7ST201.CSV",
    "Stump_test/SD8ST25M.CSV"
]

line_names = {
    "direct_generator_to_probe/BASELI01.CSV": "Direct generator to oscilloscope",

    "Stump_test/SD7ST201.CSV": "SD Line 7",
    "Stump_test/SD8ST25M.CSV": "SD Line 8"
}


plt.figure(figsize=(12,6))

for file in files:
    # Try common oscilloscope CSV formats
    df = pd.read_csv(file, comment='#')
    
    # Keep only numeric columns
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.dropna(axis=1, how='all')
    
    # Assume first column is time and second is signal
    time = df.iloc[:, 0]
    signal = df.iloc[:, 1] 
    
    label = line_names[file]
    plt.plot(time, signal, label=label)

plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("Overlay of SD Signals")
plt.legend()
plt.grid(True)
plt.show()

#output_path = "sd_overlay_plot.png"

#plt.savefig(output_path, bbox_inches='tight', dpi=300)

#print(f"Saved plot to: {output_path}")
