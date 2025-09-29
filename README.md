EEG & ECG Visualization Tool

How to Run:
- Install Python
- Install dependencies (pip install pandas plotly kaleido)
- Run script on Powershell
    - python plot_eeg_ecg.py
- Output:
    - Interactive browser plot
    - eeg_ecg_plot.html (shareable interactive file)  
    - eeg_ecg_plot.png (static export)
 

Design Choices:
- caling: EEG shown in µV (left y-axis), ECG in mV (right y-axis) to keep both readable.
- Usability: Zoom, scroll, hover tooltips, channel toggling via legend.
- Extras: Automatic export to HTML/PNG.

Future Work:
- Automatic export to HTML and PNG
