import streamlit as st
import pandas as pd
import altair as alt

# 🎨 Custom Styling & Animations
st.markdown(
    """
    <style>
    /* Background */
    body { background: linear-gradient(to right, #ffafbd, #ffc3a0); }
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

    /*  button animations */
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

    /* Text animations */
    .stMarkdown {
        animation: fadeIn 1s ease-in-out;
    }

    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎯 App Title
st.title("🔥BMI Calculator ")
st.markdown("### Get your **Body Mass Index (BMI)** with style!")

# 🌍 Unit Selection
unit = st.radio("Select Measurement Unit:", ("Metric (kg, cm)", "Imperial (lbs, inches)"))

# 📌 User Input
if unit == "Metric (kg, cm)":
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.1f")
    height = st.number_input("Enter your height (cm)", min_value=1.0, format="%.1f")
    bmi = weight / ((height / 100) ** 2) if height > 0 else 0
else:
    weight = st.number_input("Enter your weight (lbs)", min_value=1.0, format="%.1f")
    height = st.number_input("Enter your height (inches)", min_value=1.0, format="%.1f")
    bmi = (weight / (height ** 2)) * 703 if height > 0 else 0

# 🚀 BMI Calculation
if st.button(" Calculate My BMI"):
    if height > 0 and weight > 0:
        # SweetAlert Popup for BMI Result
        st.markdown(
            f"""
            <script>
            Swal.fire({{
                title: "Your BMI is: {bmi:.2f} 🎉",
                text: "Let's see where you stand!",
                icon: "success",
                confirmButtonColor: "#ff4b2b"
            }});
            </script>
            """,
            unsafe_allow_html=True
        )

        # BMI Classification & Health Tips
        if bmi < 18.5:
            st.warning("⚠️ **Underweight** - Eat more nutritious foods! 🍎🥑")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ **Normal weight** - Keep up the good lifestyle! 🏃‍♂️💪")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ **Overweight** - Consider more exercise! 🏋️‍♀️🥦")
        else:
            st.error("🚨 **Obese** - A balanced diet and activity is key! 🥗🚴‍♂️")

# 📊 Fixed BMI Category Chart
bmi_data = pd.DataFrame({
    "Category": ["Underweight", "Normal", "Overweight", "Obese"],
    "BMI": [18.5, 24.9, 29.9, 40]
})

bmi_chart = alt.Chart(bmi_data).mark_bar().encode(
    x=alt.X("Category", sort=None),
    y="BMI",
    color="Category"
).properties(title="BMI Categories")

st.altair_chart(bmi_chart, use_container_width=True)

# 📌 Footer
st.markdown("---")
st.markdown("💡 _Maintaining a healthy BMI is essential for overall well-being._")

# 📢 Importing SweetAlert JS
st.markdown(
    """
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    """,
    unsafe_allow_html=True
)

