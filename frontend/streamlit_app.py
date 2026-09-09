import requests
import streamlit as st


API_BASE_URL = "http://127.0.0.1:8000"
API_KEY = "gallivis-dev-key"


st.set_page_config(
    page_title="GALLIVIS",
    page_icon="🩺",
    layout="wide",
)


st.title("GALLIVIS")
st.subheader("Gallstone Intelligent Vision System")

st.markdown(
    """
    ### Intelligent Multimodal Clinical Decision Support System

    GALLIVIS is designed to assist clinicians in the
    pre-operative classification of gallstones using
    multimodal clinical information.
    """
)

st.divider()

st.header("Patient Information")

col1, col2 = st.columns(2)

with col1:
    st.text_input("Patient ID")

with col2:
    st.number_input("Age", min_value=0, max_value=120, value=30)

st.selectbox(
    "Gender",
    ["Select", "Male", "Female", "Other"],
)

st.divider()

st.header("Ultrasound Image")

uploaded_file = st.file_uploader(
    "Upload a preoperative ultrasound image (JPEG or PNG)",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded ultrasound image",
        width=400,
    )

    if st.button("Analyze Ultrasound Image"):

        with st.spinner("Analyzing image..."):

            try:
                response = requests.post(
                    f"{API_BASE_URL}/predict/ultrasound",
                    headers={"x-api-key": API_KEY},
                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            uploaded_file.type,
                        )
                    },
                    timeout=30,
                )
            except requests.exceptions.ConnectionError:
                st.error(
                    "Could not reach the GALLIVIS API. "
                    "Make sure it is running (see run.py)."
                )
                response = None

        if response is not None:

            if response.status_code == 200:

                result = response.json()

                st.success(f"Predicted stone type: **{result['prediction']}**")
                st.metric(
                    "Model Confidence",
                    f"{result['confidence'] * 100:.1f}%",
                )

                st.subheader("Full Probability Breakdown")
                st.bar_chart(result["probabilities"])

                st.warning(result["disclaimer"])

            elif response.status_code == 503:
                st.warning(response.json()["detail"])

            else:
                st.error(
                    f"Prediction failed ({response.status_code}): "
                    f"{response.json().get('detail', 'Unknown error')}"
                )

st.divider()

st.caption(
    "GALLIVIS provides AI-assisted clinical decision support only. "
    "It does not replace a qualified doctor's diagnosis."
)