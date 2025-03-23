import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import altair as alt

# 💎 Custom Styling (Glassmorphism & Dark Mode)
st.markdown(
    """
    <style>
    body { background: linear-gradient(to right, #8e2de2, #4a00e0); }
    .stApp { backdrop-filter: blur(10px); border-radius: 15px; padding: 20px; }
        .stApp {
        max-width: 800px;
        margin: auto;
        padding: 20px;
        border: 2px solid  #D90429 ;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #0D0D0D ;
        animation: fadeIn 1s ease-in-out;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #ff416c, #ff4b2b);
        border: none;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 25px;
        transition: 0.3s ease-in-out;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }

    /* Toggle Switch */
    .toggle { position: fixed; top: 10px; right: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)

# 🌙 Dark Mode Toggle
dark_mode = st.checkbox("🌙 Dark Mode")
if dark_mode:
    st.markdown("<style>body { background: #121212; color: white; }</style>", unsafe_allow_html=True)

# 🚀 Title
st.title("🚀 AI-Powered Data Dashboard")

# 📂 File Upload
uploaded_file = st.file_uploader("📥 Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 📝 Data Preview
    st.subheader("🔍 Data Preview")
    st.write(df.head())

    # 📊 Data Summary
    st.subheader("📜 Data Summary")
    st.write(df.describe())

    # 🔍 Multi-Column Filtering
    st.subheader("🎯 Filter Data")
    selected_columns = st.multiselect("Select columns to filter", df.columns)
    
    if selected_columns:
        filters = {}
        for col in selected_columns:
            unique_values = df[col].dropna().unique()
            selected_value = st.selectbox(f"Filter by {col}", unique_values)
            filters[col] = selected_value

        filtered_df = df
        for col, val in filters.items():
            filtered_df = filtered_df[filtered_df[col] == val]

        if not filtered_df.empty:
            st.write(filtered_df)
            # 📤 Export Filtered Data
            st.download_button(
                label="📥 Download Filtered Data",
                data=filtered_df.to_csv(index=False),
                file_name="filtered_data.csv",
                mime="text/csv"
            )
        else:
            st.warning("⚠️ No matching data found.")

    # 📊 Custom Charts with PROPER ERROR HANDLING
    st.subheader("📊 Interactive Data Visualization")
    columns = df.columns.tolist()
    x_column = st.selectbox("📌 Select x-axis", columns, key="x_axis")
    y_column = st.selectbox("📌 Select y-axis (Numeric Only)", columns, key="y_axis")

    chart_type = st.radio("📡 Choose Chart Type:", ["Line", "Bar", "Scatter", "Pie"])

    if st.button("🎨 Generate Plot"):
        # 🔥 **FIX 1: Make sure x & y columns exist**
        if x_column not in df.columns or y_column not in df.columns:
            st.error("❌ Invalid column selection. Choose correct columns.")
        elif not pd.api.types.is_numeric_dtype(df[y_column]):
            st.error("❌ The selected Y-axis column must be numeric!")
        elif df.empty:
            st.error("❌ The dataset is empty. Upload a valid CSV.")
        else:
            # **🔥 FIX 2: Aggregate duplicate x_column values**
            plot_df = df.groupby(x_column, as_index=False)[y_column].mean()

            # **🔥 FIX 3: Handle different chart types properly**
            if chart_type == "Line":
                st.line_chart(plot_df.set_index(x_column)[y_column])
            elif chart_type == "Bar":
                st.bar_chart(plot_df.set_index(x_column)[y_column])
            elif chart_type == "Scatter":
                fig, ax = plt.subplots()
                ax.scatter(plot_df[x_column], plot_df[y_column], color='red')
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                st.pyplot(fig)
            elif chart_type == "Pie":
                fig, ax = plt.subplots()
                plot_df.set_index(x_column)[y_column].plot.pie(autopct='%1.1f%%', ax=ax)
                st.pyplot(fig)

else:
    st.info("📌 Upload a CSV file to get started!")

# 📌 Footer
st.markdown("---")
st.markdown("🔥 Built with **Streamlit** | 🚀 Created by You!")