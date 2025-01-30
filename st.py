import streamlit as st
import pandas as pd
import io

def process_inp_file(uploaded_file):
    """Reads an .inp file and converts it into a structured DataFrame"""
    lines = uploaded_file.read().decode("utf-8").splitlines()
    
    data = []
    for line in lines:
        if line.strip():  # Skip empty lines
            data.append(line.split())  # Split line into columns
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    return df

def convert_df_to_excel(df):
    """Converts DataFrame to Excel file and returns as a downloadable bytes object"""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Sheet1")
    processed_data = output.getvalue()
    
    return processed_data

# Streamlit UI
st.title("Hi!, Welcome to INP to Excel Converter")
st.write("Upload a `.inp` file and download the converted Excel file.")

uploaded_file = st.file_uploader("Upload .inp File", type=["inp"])

if uploaded_file:
    st.success("File uploaded successfully!")
    
    # Process file
    df = process_inp_file(uploaded_file)
    
    # Show preview
    st.write("### Preview of Extracted Data:")
    st.dataframe(df)
    
    # Convert DataFrame to Excel
    excel_data = convert_df_to_excel(df)
    
    # Download button
    st.download_button(
        label="📥 Download Excel File",
        data=excel_data,
        file_name="converted_file.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
