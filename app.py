import streamlit as st


st.set_page_config(page_title="Introduction", layout="wide")

col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

with col1:
    st.write("[https://www.linkedin.com/in/daniellapolor/)")



custom_section_html = """
    <style>
    .custom-section {
        background: linear-gradient(to right, #83a4d4, #b6fbff); /* Ombre effect from blue to light blue */
        padding: 20px;
        text-align: center;
        border-radius: 10px; /* Rounded corners */
        margin: 10px 0; /* Margin for spacing */
    }
    .custom-section h2, .custom-section p {
        color: #fff; /* Explicitly setting text color to white for both elements */
        margin: 0;
        padding: 0;
    }
    .custom-section h2 {
        font-size: 36px; /* Larger font size */
        font-weight: bold; /* Bold font */
    }
    .custom-section p {
        font-size: 24px; /* Smaller font size for 'Data Analyst' */
    }
    </style>
    <div class='custom-section'>
        <h2>Daniella Edokpolor</h2>
        <p>Commercial Analyst | Salesforce Specialist</p>
    </div>
"""

st.markdown(custom_section_html, unsafe_allow_html=True)




st.markdown("""
            I am an experienced data analyst who specialises in data visualisation. I play a key role at Immediate Media, the publisher behind BBC Good Food and Radio Times, focusing on advertising revenue and sales performance.
            My expertise and passion lies in transforming data into clear, actionable insights.

            Please find my key skills below. On seperate pages, I have included a range of dashboards I have created with short descriptions. Any sensitive data has been redacted, to maintain confidentiality.

            If you have any questions, please contact me using the form!
            """)

st.header("Skills")

col1, col2, col3, col4, col5, col6 = st.columns(6)

