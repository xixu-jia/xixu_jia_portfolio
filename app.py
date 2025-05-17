import streamlit as st
import pandas as pd
import plotly.express as px
import time
import re

#data visualization
st.set_page_config(
    page_title="Wine Data Dashboard",
    page_icon="🍷",
    layout="wide"
)

if 'load_data' not in st.session_state:
    st.session_state.load_data = False

def load_wine_data():
    st.session_state.load_data = True

st.title("Wine Data Visualization")
st.button("Load Wine Data", on_click=load_wine_data)

if st.session_state.load_data:
    file_path = "wine database.xlsx"
    df = pd.read_excel(file_path, sheet_name='winedataset')
    
    # Clean Price Column
    df['Price'] = df['Price'].astype(str).apply(lambda x: re.sub(r'[^0-9.]', '', x))
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    
    # Clean ABV Column
    df['ABV'] = df['ABV'].str.replace('%', '').astype(float)
    
    # Clean Vintage Column
    df['Vintage'] = df['Vintage'].astype(str).str[:4]
    df['Vintage'] = pd.to_numeric(df['Vintage'], errors='coerce')
    
    bar = st.progress(0)
    time.sleep(1)
    bar.progress(100)
    st.success("Data Loaded Successfully!")
    
    st.header("Global Wine Distribution")
    wine_count = df.groupby(['Country', 'Type']).size().reset_index(name='Count')
    fig_map = px.scatter_geo(wine_count, locations="Country", locationmode='country names',
                             size="Count", color="Type", projection="natural earth",
                             title="Wine Types by Country")
    st.plotly_chart(fig_map)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Wine Price Analysis")
        fig_price = px.box(df, x="Type", y="Price", color="Type",
                           title="Price Distribution of Different Wine Types")
        st.plotly_chart(fig_price, use_container_width=True)
        
        with st.expander("View Code"):
            st.code('''fig_price = px.box(df, x="Type", y="Price", color="Type", title="Price Distribution")''')
    
    with col2:
        st.header("Alcohol Content (ABV) Distribution")
        fig_abv = px.histogram(df, x="ABV", color="Type", barmode="overlay",
                               title="ABV Distribution Across Wine Types")
        st.plotly_chart(fig_abv, use_container_width=True)
        
        with st.expander("View Code"):
            st.code('''fig_abv = px.histogram(df, x="ABV", color="Type", barmode="overlay", title="ABV Distribution")''')
    
    st.header("Vintage Trends")
    vintage_count = df.groupby("Vintage").size().reset_index(name='Count')
    fig_vintage = px.line(vintage_count.sort_values("Vintage"), x="Vintage", y="Count", markers=True,
                           title="Wine Production by Vintage Year")
    st.plotly_chart(fig_vintage)
    
    st.header("Wine Style Distribution")
    style_count = df.groupby(["Style", "Type"]).size().reset_index(name="Count")
    fig_style = px.bar(style_count, x="Style", y="Count", color="Type",
                       title="Distribution of Wine Styles", barmode="stack")
    st.plotly_chart(fig_style)
    
    st.write("Data Source: Provided Wine Database")

st.write("") 


#wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("Wine Characteristics Word Cloud 🍷")

df = pd.read_excel("wine database.xlsx", sheet_name="winedataset")

df = df[df["Characteristics"].notna()]

text = " ".join(df["Characteristics"].astype(str).tolist())

wordcloud = WordCloud(width=800, height=400, background_color="linen",colormap="PuRd").generate(text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

st.write("") 
st.write("") 
st.write("") 

# wine recommendation
file_path = "wine database.xlsx"
df = pd.read_excel(file_path, sheet_name='winedataset')

df['Price'] = df['Price'].astype(str).str.replace("\u00a3", "").str.replace(" each", "").astype(float)

df['ABV'] = df['ABV'].astype(str).str.replace("%", "").astype(float)

st.markdown("<h2 style='text-align: center;'>🍷 Choose Your Wine</h2>", unsafe_allow_html=True)

with st.expander("Click to customize your wine preferences 👇"):

    st.header("🍽️ What type of meal would you like to pair?")
    pairing_options = {
        "Select your meal type": [],
        "Steak or red meat 🥩": ["Red"],
        "Barbecue 🍖": ["Red"],
        "Cheese 🧀️": ["Red"],
        "Seafood 🦪": ["Rosé", "White"],
        "Salad or light dishes 🥗": ["Rosé", "White"],
        "Dessert 🍰": ["Rosé"],
        "Appetizer 🍽️": ["White"]
    }

    selected_food = st.selectbox("", list(pairing_options.keys()))
    selected_wine_types = pairing_options[selected_food]

    if selected_food != "Select your meal type":
        st.write(f"You selected: {selected_food}")

    st.header("💰 Your budget is...")
    budget_options = ["£0-£10", "£11-£20", "£21-£30", "£31-£40", "£41-£50", "£50-£100"]
    selected_budget = st.radio("", budget_options, horizontal=True)

    price_ranges = {
        "£0-£10": (0, 10),
        "£11-£20": (11, 20),
        "£21-£30": (21, 30),
        "£31-£40": (31, 40),
        "£41-£50": (41, 50),
        "£50-£100": (50, 100)
    }
    min_price, max_price = price_ranges[selected_budget]

    st.header("🍷 Alcohol level (ABV)")
    abv_options = {
        "0.5 - 8%": (0.5, 8),
        "8 - 12%": (8, 12),
        "12 - 14%": (12, 14),
        "14 - 16%": (14, 16),
        "16 - 20%": (16, 20)
    }
    selected_abv = st.selectbox("", list(abv_options.keys()))
    min_abv, max_abv = abv_options[selected_abv]

    filtered_wines = df[
        df['Type'].str.lower().isin([t.lower() for t in selected_wine_types]) &
        df['Price'].between(min_price, max_price) &
        df['ABV'].between(min_abv, max_abv)
    ]

    st.header("🍷 Recommended Wines for You")

    if not filtered_wines.empty:
        for _, row in filtered_wines.iterrows():
            st.write(f"✅ **{row['Title']}** - £{row['Price']:.2f} - {row['Type']} - {row['ABV']}% ABV")
    else:
        st.warning("❌ No matching wines found. Try adjusting your selection.")

st.write("") 

# gift recommendation
df['Price'] = df['Price'].astype(str).str.replace("£", "").str.replace(" per bottle", "").str.replace(" each", "").astype(float)
df['Vintage'] = pd.to_numeric(df['Vintage'], errors='coerce')

st.markdown("<h2 style='text-align: center;'>🎁 Want to give a gift？</h2>", unsafe_allow_html=True)

with st.expander("Click to get gift wine suggestions 🎁"):
    st.subheader("🎯 Select gift preferences")

    gender = st.radio("Recipient's Gender", ["Male", "Female"])
    occasion = st.selectbox("Gift Occasion", ["Dinner Gathering", "Business Gift", "Birthday", "Date"])

    gender_map = {
        "Male": ["Red"],
        "Female": ["Rosé", "White"]
    }

    occasion_map = {
        "Dinner Gathering": ["Red", "White"],
        "Business Gift": ["Red", "White"],
        "Birthday": ["Rosé", "Sweet"],
        "Date": ["Rosé"]
    }

    recommended_types = list(set(gender_map[gender]) & set(occasion_map[occasion]))

    st.subheader("💰 Budget Range")
    price_range = st.slider("Select your budget (£)", 10, 110, (20, 50))

    st.subheader("🍇 Vintage")
    vintage_range = st.slider("Select vintage range", 1999, 2023, (2010, 2022))

    if occasion == "Business Gift":
        filtered_df = df[
            (df['Price'] > 60) &
            (df['Vintage'] <= 2012) &
            (df['Type'].isin(recommended_types)) &
            (df['Price'].between(*price_range)) &
            (df['Vintage'].between(*vintage_range))
        ]
    else:
        filtered_df = df[
            (df['Type'].isin(recommended_types)) &
            (df['Price'].between(*price_range)) &
            (df['Vintage'].between(*vintage_range))
        ]

    st.subheader("🍷 Recommended Wines")
    if not filtered_df.empty:
        for _, row in filtered_df.iterrows():
            st.write(f"✅ **{row['Title']}** - £{row['Price']:.2f} - {row['Type']} - {int(row['Vintage'])}")
    else:
        st.warning("❌ No matching wines found. Try adjusting your selection.")
