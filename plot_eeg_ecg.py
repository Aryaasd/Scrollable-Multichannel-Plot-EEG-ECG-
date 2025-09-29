import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# -------- Load CSV --------
def load_data(path):
    # Ignore metadata lines starting with #
    df = pd.read_csv(path, comment="#")
    
    # Drop irrelevant columns
    drop_cols = ["X3:", "Trigger", "Time_Offset", "ADC_Status", "ADC_Sequence", "Event", "Comments"]
    df = df.drop(columns=[c for c in drop_cols if c in df.columns], errors="ignore")
    
    return df

# -------- Create Interactive Plot --------
def plot_multichannel(df):
    time = df["Time"]

    # Define channel groups
    eeg_channels = [c for c in df.columns if c not in ["Time", "X1:LEOG", "X2:REOG", "CM"]]
    ecg_channels = ["X1:LEOG", "X2:REOG"]
    cm_channel = "CM"

    # Create subplots with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # EEG traces (μV) on left axis
    for ch in eeg_channels:
        fig.add_trace(go.Scatter(x=time, y=df[ch], mode="lines", name=f"EEG {ch}"), secondary_y=False)
    
    # ECG traces (mV) on right axis (convert μV → mV)
    for ch in ecg_channels:
        if ch in df.columns:
            fig.add_trace(go.Scatter(x=time, y=df[ch]/1000.0, mode="lines", name=f"ECG {ch} (mV)"), secondary_y=True)

    # CM trace on right axis as well (μV → mV)
    if cm_channel in df.columns:
        fig.add_trace(go.Scatter(x=time, y=df[cm_channel]/1000.0, mode="lines", name="CM (mV)"), secondary_y=True)

    # Layout
    fig.update_layout(
        title="Scrollable Multichannel EEG + ECG Plot",
        xaxis_title="Time (s)",
        yaxis_title="EEG (μV)",
        legend=dict(orientation="h", y=-0.2),
        height=600
    )

    fig.update_yaxes(title_text="EEG (μV)", secondary_y=False)
    fig.update_yaxes(title_text="ECG / CM (mV)", secondary_y=True)

    # Add range slider
    fig.update_xaxes(rangeslider_visible=True)

    fig.show()

# -------- Main --------
if __name__ == "__main__":
    df = load_data("EEG and ECG data_02_raw.csv")  # make sure your CSV is in the same folder
    plot_multichannel(df)