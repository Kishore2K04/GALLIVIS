import streamlit as st


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

st.info(
    "AI prediction modules will be integrated in upcoming sprints."
)

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

st.header("Current Status")

st.write(
    "GALLIVIS application foundation is running successfully."
)