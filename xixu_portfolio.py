
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Xixu's Portfolio", layout="wide")


menu = st.sidebar.radio("Navigate", ["About Me", "Professional Experience", "Skills & Projects", "Activities & Interests"])

if menu == "About Me":
    st.info("Welcome! Some sections may take a few seconds to load, thanks for your patience!")
    st.title("About Me")
    col1, col2 = st.columns([1,2])
    with col1:
        st.image("xixu.png")
    with col2:
        st.markdown(
        """
<div style='max-width: 500px; padding-left: 30px;'>
    <h2 style='font-size: 28px; margin-bottom: 20px;'>Hi, I’m Xixu!</h2>
    <p style='font-size: 20px; line-height: 1.8; margin-bottom: 15px;'>
        I’m a master’s student in <strong>Digital Marketing & Data Science</strong> at Emlyon Business School. I majored in <strong>French</strong> during my undergraduate studies.
    </p>
    <p style='font-size: 20px; line-height: 1.8; margin-bottom: 15px;'>
        I have 1+ year of <strong>media planning</strong> experience at Publicis.
    </p>
    <p style='font-size: 20px; line-height: 1.8;'>
        I’m skilled in <strong>data-driven marketing</strong>, <strong>campaign strategy</strong>, and <strong>consumer insights</strong>.
    </p>
</div>
        """,
        unsafe_allow_html=True
    )
    st.text("")
    st.text("")
    from PIL import Image
    
    col1, col2 = st.columns([1.2, 1.8])
    with col1:
        st.markdown(
        """
        <div style='display: flex; justify-content: center; align-items: center; height: 100%; min-height:400px;'>
            <h1 style='font-size: 48px; margin: 0;'>Creative💡</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    with col2:
        img1 = Image.open("creative.png")
        st.image(img1, width=350)
    
    st.text("")
    st.text("")
    col3, col4 = st.columns([1.2, 1.8])
    with col3:
        img2 = Image.open("rigorous.jpg")
        st.image(img2, width=350)

    with col4:
        st.markdown(
        """
        <div style='display: flex; justify-content: center; align-items: center; height: 100%; min-height:400px;'>
            <h1 style='font-size: 48px; margin: 0;'>Rigorous🗒️</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.text("")
    st.text("")    
    col5, col6 = st.columns([1.2, 1.8])
    with col5:
        st.markdown(
        """
        <div style='display: flex; justify-content: center; align-items: center; height: 100%; min-height:400px;'>
            <h1 style='font-size: 48px; margin: 0;'>and... Nothing can stop me!</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    with col6:
        img3 = Image.open("tea.jpg")
        st.image(img3, width=350) 
      



elif menu == "Professional Experience":
    st.title("Professional Experience")

    # Section 1: Summary Chart
    st.header("📊 Key Deliverables Overview")
    st.subheader("Below is a summary of major outputs during my time at Publicis:")

    labels = ["New Product Strategies", "Thematic Research", "Weekly Reports", "Monthly Data Reports"]
    values = [9, 11, 76, 19]

    fig, ax = plt.subplots(figsize=(4, 2))
    bars = ax.bar(labels, values, width=0.4, color="#4C72B0")
    ax.set_ylabel("Count", fontsize=6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.bar_label(bars, padding=3, fontsize=6)
    plt.xticks(fontsize=6, rotation=15)
    ax.tick_params(axis='y', labelsize=6)

    st.pyplot(fig,use_container_width=False)

    # Section 2: Thematic Report
    st.header("📎 Sample Thematic Report")
    
    st.markdown(
    '<iframe src="https://drive.google.com/file/d/1QXgRw9Gx9qOhSPMeq5qbdaa2DK4jkCr5/preview" width="700" height="500"></iframe>',
    unsafe_allow_html=True
)
   
   
   
    # Section 3: other works
    st.text("")
    st.text("")
    from PIL import Image
    st.header("🧩 Other works")
    
    st.subheader("Here are snapshots from other professional tasks I contributed to.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        img1 = Image.open("data analysis.png")
        st.image(img1, caption="📊 data analysis", use_container_width=True)
        
    with col2:
        img2 = Image.open("competitor analysis.png")
        st.image(img2, caption="🔍 competitor analysis", use_container_width=True)
            
    with col3:
        img3 = Image.open("consumer insight.png")
        st.image(img3, caption="👥 consumer insight", use_container_width=True)


    # Section 4: Knowledge Sharing & Team Building
    st.text("")
    st.text("")
    st.header("🧰 Tools Guide & Team Activities")
    
    col1, col2 = st.columns(2)
    
    with col1:
        img1 = Image.open("guide.png")
        st.image(img1, caption="I created internal documentation to help onboard new teammates more efficiently", use_container_width=True)
        
    with col2:
        img2 = Image.open("TB.jpg")
        st.image(img2, caption="I organized a team-building event for collaboration and fun", use_container_width=True)



elif menu == "Skills & Projects":
    st.title("Skills & Projects")
    st.subheader("💻Python Project: Wine exploration")
    st.write(
    "This Streamlit app helps users explore wine dataset based on data visualization, text analysis and also makes wine recommendation. ")
    
    st.markdown(
    '[🔗 Click here to explore the live app](https://f63dagqkdmrdepur6vzz4a.streamlit.app/)',
    unsafe_allow_html=True)


    st.subheader("📊 Tableau Project: Airbnb NYC Dashboard")
    
    st.write("""
             This interactive dashboard analyzes Airbnb listings by neighborhood, price, room type, and rating.
             It was built with Tableau based on a real-world NYC dataset.""")
    st.markdown(
    '[🔗 View full dashboard on Tableau Public](https://public.tableau.com/views/Airbnb_17474214581410/Airbnb)'
)

    st.subheader("🎨 Prototype Project: Fitness Social App")
    
    st.write("This is an interactive prototype built using Figma, demonstrating key user flows for a sports community app.")
    
    st.markdown('[🔗 Click here to view the interactive Figma prototype](https://www.figma.com/proto/aMdkbf82NIc2hy3XsPPGRO/Prototype-Sports-community-app?node-id=1-3&t=44AaNueyVgDAkzjY-1)')

    st.text("")
    st.text("")
    st.markdown(
    "<h4>I'm also familiar with SQL, Dataiku, GA4, and CRM strategy...</h4>",
    unsafe_allow_html=True
)


elif menu == "Activities & Interests":
    st.title("Activities & Interests")
    st.subheader("""
    🏊‍♀️ Volunteer at Paris 2024 Paralympics (Event Services Team)  
    """)
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("paralympic1.jpg")
    
    with col2:
        st.image("paralympic2.jpg")

    
    st.subheader("""
    🎬 Filming and editing video  
    """)
    st.write("A street interview project 'Got News?' where I invited random people to share the 'good news' or 'bad news' in their lives.")
    
    col1, col2 = st.columns([1,1])
    
    with col1:
        st.image("got news.jpg")
    
    with col2:
        st.video("https://youtu.be/PaUn2W27z1s?si=1R5sIveJD2KqLUnL")

    st.subheader("""
    🎵 A huge fan of musical theater  
    """)
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("musical1.jpg")
    
    with col2:
        st.image("musical2.jpg")
    
    st.text("")
    st.text("")
    st.markdown(
    """
    <div style='text-align: right; font-size: 14px; color: gray;'>
        <p>This portfolio was built with Python and Streamlit</p>
        <p>Thank you for viewing</p>
    </div>
    """,
    unsafe_allow_html=True
)
