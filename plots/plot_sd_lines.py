from pathlib import Path
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

files = [
   "direct_generator_to_probe/BASELI01.CSV",   
   
   "phase_corrected_25MHz/phase_corrected_csv/SD_line1.csv",
   "phase_corrected_25MHz/phase_corrected_csv/SD_line2.csv",
   "phase_corrected_25MHz/phase_corrected_csv/SD_line3.csv",
   "phase_corrected_25MHz/phase_corrected_csv/SD_line5.csv",
   "phase_corrected_25MHz/phase_corrected_csv/SD_line7.csv",
   "phase_corrected_25MHz/phase_corrected_csv/SD_line8.csv"
]

line_names = {
    "direct_generator_to_probe/BASELI01.CSV": "Direct generator to oscilloscope",
    "phase_corrected_25MHz/phase_corrected_csv/SD_line1.csv": "SD Line 1",
    "phase_corrected_25MHz/phase_corrected_csv/SD_line2.csv": "SD Line 2",
    "phase_corrected_25MHz/phase_corrected_csv/SD_line3.csv": "SD Line 3",
    "phase_corrected_25MHz/phase_corrected_csv/SD_line5.csv": "SD Line 5",
    "phase_corrected_25MHz/phase_corrected_csv/SD_line7.csv": "SD Line 7",
    "phase_corrected_25MHz/phase_corrected_csv/SD_line8.csv": "SD Line 8"
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

output_path = "sd_overlay_plot.png"

plt.savefig(output_path, bbox_inches='tight', dpi=300)

print(f"Saved plot to: {output_path}")
