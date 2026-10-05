import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Halle's Webpage",
    page_icon="🌸",
    layout="wide"
)

# Embedded CSS
st.markdown(
    """
    <style>
        /* Import an elegant Google Font */
        @import url('[fonts.googleapis.com](https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:wght@600;700&display=swap)');

        /* Main page */
        .stApp {
            background:
                radial-gradient(circle at top left, #ffd6e7 0%, transparent 35%),
                radial-gradient(circle at bottom right, #f4c2ff 0%, transparent 30%),
                linear-gradient(135deg, #fff7fb 0%, #ffe8f3 50%, #fce8ff 100%);
            color: #572846;
        }

        /* Main content area */
        .block-container {
            max-width: 1150px;
            padding-top: 3rem;
            padding-bottom: 4rem;
        }

        /* Typography */
        h1, h2, h3 {
            color: #b83280 !important;
            font-family: "Playfair Display", serif !important;
        }

        h1 {
            font-size: 3.3rem !important;
            line-height: 1.15 !important;
            text-shadow: 1px 2px 0 #ffffff;
        }

        p, label, .stMarkdown {
            color: #572846;
            font-family: "DM Sans", sans-serif;
        }

        /* Soft pink dividers */
        hr {
            border: none;
            height: 2px;
            margin: 2.5rem 0;
            background: linear-gradient(
                90deg,
                transparent,
                #e98ab8,
                #c86ddd,
                transparent
            );
        }

        /* Form fields */
        input,
        textarea {
            width: 100%;
            padding: 0.9rem 1rem;
            margin-bottom: 1rem;
            border: 2px solid #f2b6d2;
            border-radius: 14px;
            background-color: rgba(255, 255, 255, 0.9);
            color: #572846;
            font-family: "DM Sans", sans-serif;
            font-size: 1rem;
            box-sizing: border-box;
            outline: none;
            transition: 0.2s ease;
            box-shadow: 0 5px 14px rgba(190, 74, 137, 0.08);
        }

        textarea {
            min-height: 150px;
            resize: vertical;
        }

        input:focus,
        textarea:focus {
            border-color: #d85ba5;
            box-shadow: 0 0 0 4px rgba(216, 91, 165, 0.15);
        }

        input::placeholder,
        textarea::placeholder {
            color: #aa7895;
        }

        /* Form button */
        button[type="submit"] {
            padding: 0.85rem 2rem;
            border: none;
            border-radius: 999px;
            background: linear-gradient(135deg, #ed75ad, #b84bd2);
            color: white;
            font-family: "DM Sans", sans-serif;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 8px 20px rgba(184, 75, 210, 0.25);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        button[type="submit"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 24px rgba(184, 75, 210, 0.35);
        }

        /* Style links */
        a {
            color: #bd2f7b !important;
            font-weight: 600;
        }

        /* Hide Streamlit's default menu and footer */
        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        /* Mobile adjustments */
        @media (max-width: 700px) {
            .block-container {
                padding: 1.5rem;
            }

            h1 {
                font-size: 2.3rem !important;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)


def load_lottieurl(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


# Assets
lottie_coding = load_lottieurl("https://lottie.host/4e474525-5012-4f53-a2ea-794553fe5aab/qXlo28lQ9X.json")


# Header
with st.container():
    st.subheader("Hi, I'm Halle!")
    st.title("A Cybersecurity Co-op and MBA Student in Memphis, TN")
    st.write(
        "Combining technology, creativity, and continuous learning "
        "to help build safer digital experiences."
    )

# What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2, gap="large")

    with left_column:
        st.header("What I Do")
        st.write(
            """
            Hi, I'm Halle! I am currently getting my MBA in Cybersecurity at East Tennessee State University and have a solid
            foundation in information technology, cybersecurity, and
            software design. I have a Bachelor's degree in Computer Science from the University of Tennessee at Chattanooga (UTC) and have gained practical experience through various internships and co-op positions.

            I am seeking an opportunity to develop technical skills while
            contributing to meaningful projects. I bring strong
            troubleshooting abilities, adaptability, and a commitment to
            continuous learning.
            """
        )

    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.info("The animation is currently unavailable.")
# work experience
with st.container():
    st.write("---")
    st.subheader("Work Experience")
    st.write("I have experience in IT support, cybersecurity, and software design. Here are some of my previous roles:" \
    "\n- **Cybersecurity Co-op**: Supported cybersecurity initiatives and contributed to threat analysis.\n- **IT Support Specialist**: Provided technical support and troubleshooting for hardware and software issues.\n- **Cybersecurity Intern**: Assisted in monitoring and analyzing security threats within UTC, including phishing emails. \n- **Web Design Intern**: Worked with the UTC Web Development team in updating UTC websites with requests from faculty.")

#tech skills
with st.container():
    st.write("---")
    st.subheader("Technical Skills")
    st.write("My technical skills include:\n- **Programming Language**: Python \n- **Framework**: Streamlit \n- **Other Tools**: Windows, Microsoft Office Suite, Zoom, Google Workspace, ticketing systems.")

# Contact
with st.container():
    st.write("---")
    st.header("Get in Touch With Me! 💌")
    st.write("##")

    contact_form = """  
<form action="https://formsubmit.co/hallebarber15@gmail.com" method="POST">  
 <input type="hidden" name="_captcha" value = "false">  
 <input type="text" name="name" placeholder = "Your name" required>  
 <input type="email" name="email" placeholder = "Your email" required>  
 <textarea name="message" placeholder = "Your message here" required></textarea>  
 <button type="submit">Send</button>  
"""

    left_column, right_column = st.columns(2, gap="large")

    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st.markdown(
            """
            ### Let's connect 🌷

            I'm interested in cybersecurity, software design, and
            opportunities to contribute to meaningful technical projects.
            """
        )
