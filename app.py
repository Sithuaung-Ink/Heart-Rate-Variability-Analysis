import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import streamlit as st # type: ignore

# Set up the Streamlit app
st.title("Heart Rate Variability (HRV) Analysis")
st.write("This project provides an interactive tool to analyze Heart Rate Variability (HRV) by visualizing HR and RMSSD trends over time,\n"
" helping users understand stress, recovery, and cardiovascular health through condition-based insights.")
st.write("Select a subject to visualize the HR and RMSSD trends over time.")

base_url = "https://raw.githubusercontent.com/Sithuaung-Ink/Heart-Rate-Variability-Analysis/main/all_subjects_bpm_rmssd/"

# Dictionary of CSV file names for each subject
subject_files = {
    "Subject 1": "subject_1_bpm_rmssd.csv",
    "Subject 2": "subject_2_bpm_rmssd.csv",
    "Subject 3": "subject_3_bpm_rmssd.csv",
    "Subject 4": "subject_4_bpm_rmssd.csv",
    "Subject 5": "subject_5_bpm_rmssd.csv",
    "Subject 6": "subject_6_bpm_rmssd.csv",
    "Subject 7": "subject_7_bpm_rmssd.csv",
    "Subject 8": "subject_8_bpm_rmssd.csv",
    "Subject 9": "subject_9_bpm_rmssd.csv",
    "Subject 10": "subject_10_bpm_rmssd.csv",
    "Subject 11": "subject_11_bpm_rmssd.csv",
    "Subject 12": "subject_12_bpm_rmssd.csv",
    "Subject 13": "subject_13_bpm_rmssd.csv",
    "Subject 14": "subject_14_bpm_rmssd.csv",
    "Subject 15": "subject_15_bpm_rmssd.csv",
    "Subject 16": "subject_16_bpm_rmssd.csv",
    "Subject 17": "subject_17_bpm_rmssd.csv",
    "Subject 18": "subject_18_bpm_rmssd.csv",
    "Subject 19": "subject_19_bpm_rmssd.csv",
    "Subject 20": "subject_20_bpm_rmssd.csv",
    "Subject 21": "subject_21_bpm_rmssd.csv",
    "Subject 22": "subject_22_bpm_rmssd.csv",
    "Subject 23": "subject_23_bpm_rmssd.csv",
    "Subject 24": "subject_24_bpm_rmssd.csv",
    "Subject 25": "subject_25_bpm_rmssd.csv"
}

# Dropdown menu to select a subject
selected_subject = st.selectbox("Select a subject", list(subject_files.keys()))

# Construct the full URL for the selected subject
file_name = subject_files[selected_subject]
file_url = base_url + file_name

# Load the selected CSV file
try:
    df = pd.read_csv(file_url)

    # Display the data summary
    st.subheader("Data Summary")
    st.write(df[['HR', 'RMSSD']].describe())

    # Plot HR over time
    st.subheader("HR Over Time")
    plt.figure(figsize=(12, 6))
    plt.plot(df['HR'], label='HR (bpm)', color='blue')

    # Track the start and end of each condition block
    current_condition = None
    start_index = None

    for i, row in df.iterrows():
        if current_condition is None:
            # First condition block
            current_condition = row['Condition']
            start_index = i
            # Add vertical line at the start of the condition block
            plt.axvline(x=start_index, color='red', linestyle='--')
            # Add text label next to the vertical line
            plt.text(x=start_index + 3, y=plt.ylim()[1] * 0.95, s=current_condition, color='black', fontsize=12, ha='right')
        elif row['Condition'] != current_condition:
            # Condition changed, so the previous block ended
            # Start a new condition block
            current_condition = row['Condition']
            start_index = i
            # Add vertical line at the start of the condition block
            plt.axvline(x=start_index, color='red', linestyle='--')
            # Add text label next to the vertical line
            plt.text(x=start_index + 3, y=plt.ylim()[1] * 0.95, s=current_condition, color='black', fontsize=12, ha='right')

    # Add condition descriptions outside the plot (lower left corner)
    condition_descriptions = "R = Relax\nN = Neural\nT = Stressor 'Time pressure'\nI = Stressor 'Interruption'"
    plt.text(x=-0, y=-0.08, s=condition_descriptions, color='black', fontsize=12, ha='left', va='top', transform=plt.gca().transAxes)

    # Add labels and title
    plt.title('HR Over Time')
    plt.xlabel('Time (minute)')
    plt.ylabel('BPM')
    plt.grid(True)

    # Display the plot in Streamlit
    st.pyplot(plt)

    # Plot RMSSD over time
    st.subheader("RMSSD Over Time")
    plt.figure(figsize=(12, 6))
    plt.plot(df['RMSSD'] * 1000, label='RMSSD (ms)', color='blue')

    # Track the start and end of each condition block
    current_condition = None
    start_index = None

    for i, row in df.iterrows():
        if current_condition is None:
            # First condition block
            current_condition = row['Condition']
            start_index = i
            # Add vertical line at the start of the condition block
            plt.axvline(x=start_index, color='red', linestyle='--')
            # Add text label next to the vertical line
            plt.text(x=start_index + 3, y=plt.ylim()[1] * 0.75, s=current_condition, color='black', fontsize=12, ha='right')
        elif row['Condition'] != current_condition:
            # Condition changed, so the previous block ended
            # Start a new condition block
            current_condition = row['Condition']
            start_index = i
            # Add vertical line at the start of the condition block
            plt.axvline(x=start_index, color='red', linestyle='--')
            # Add text label next to the vertical line
            plt.text(x=start_index + 3, y=plt.ylim()[1] * 0.75, s=current_condition, color='black', fontsize=12, ha='right')

    # Add condition descriptions outside the plot (lower left corner)
    condition_descriptions = "R = Relax\nN = Neural\nT = Stressor 'Time pressure'\nI = Stressor 'Interruption'"
    plt.text(x=-0, y=-0.08, s=condition_descriptions, color='black', fontsize=12, ha='left', va='top', transform=plt.gca().transAxes)

    # Add labels and title
    plt.title('RMSSD Over Time')
    plt.xlabel('Time (minute)')
    plt.ylabel('RMSSD (ms)')
    plt.grid(True)

    # Display the plot in Streamlit
    st.pyplot(plt)

    st.write("HR (Heart Rate): The number of heart beats per minute (bpm); a higher HR typically indicates increased stress, while a lower HR suggests better relaxation or recovery for this experiment.")
    st.write("RMSSD (Root Mean Square of Successive Differences): A measure of heart rate variability (HRV); A higher RMSSD is generally better, indicating relaxation and recovery, while a lower RMSSD may indicate stress or poor recovery.")

except Exception as e:
    st.error(f"An error occurred while loading the data: {e}")