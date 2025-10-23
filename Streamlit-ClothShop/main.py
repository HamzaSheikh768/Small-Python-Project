import streamlit as st

st.set_page_config(
    page_title="Clothing App",
    page_icon=":tada:",
    layout="wide",
)
st.title("Welcome to My Clothing Shop!")
st.markdown("""
    <style>
    .main {
        background-color: #b2e0a1; /* green */
        color: #333; /* Dark text for contrast */
    }
    .stApp {
        background-color: #b2e0a1; /* green */
    }
    h1,h2,h3 {
            color: #2c3e50; /* Dark blue for headings */
    }        
    .stSelectbox> div> div> div> div {
        background-color: #3498db; /* Blue background for selectbox */
        border-radius: 5px;
        border: 1px solid #2980b9; /* Darker blue border */
    }
    .stButton> button {
        background-color: #e74c3c; /* Red background for buttons */
        color: white; /* White text */
        border-radius: 5px;
        border: 1px solid #c0392b; /* Darker red border */
    }        
    .stButton > button:hover {
        background-color: #D2B48C; /* darker brown */
        color: #FFFFFF; /* white */
        border: 1px solid #441752; /* dark purple */
        border-radius: 5px;
        font-weight: bold;
    }
    .clothing-card {
        background-color: #FFFFFF; /* white */
        border: 1px solid #441752; /* dark purple */
        border-radius: 10px;
        padding: 15px;
        margin: 10px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
    }
    .clothing-card:hover {
        transform: scale(1.05);
    }
        
    </style>
""", unsafe_allow_html=True)

# Sample clothing items
clothing_items = {
    "Shirts": [
    {"name": "Shirt", "price": 49.99, "image": "assets/blue-shirt.jpeg"},
    {"name": "Shirt", "price": 39.99, "image": "assets/Classic Stripes Shirt And Trousers Set.jpeg"},
    {"name": "Shirt", "price": 19.99, "image": "assets/Dress with class shirt.jpeg"},
    {"name": "Shirt", "price": 89.99, "image": "assets/check-shirt.jpeg"},
    {"name": "Shirt", "price": 89.99, "image": "assets/check-shirt2.jpeg"},
    ],

    "T-Shirts": [
    {"name": "T-Shirt", "price": 49.99, "image": "assets/t-shirt3.jpg"},
    {"name": "T-Shirt", "price": 39.99, "image": "assets/polo-red-shirt.jpeg"},
    {"name": "T-Shirt", "price": 19.99, "image": "assets/Polo-black-shirt.jpeg"},
    {"name": "T-Shirt", "price": 89.99, "image": "assets/shirt.jpeg"},
    {"name": "T-Shirt", "price": 89.99, "image": "assets/Camiseta polo shirt.jpeg"},
    ],

    "Pants": [
    {"name": "Pants", "price": 45.99, "image": "assets/cargo pant.jpeg"},
    {"name": "Pants", "price": 50.99, "image": "assets/cargo pant2.jpeg"},
    {"name": "Pants", "price": 25.99, "image": "assets/jeans.jpeg"},
    {"name": "Pants", "price": 30.99, "image": "assets/baggy.jpeg"},
    ],

}

# Sidebar for category selection
st.sidebar.title("Cloth Menu")
page = st.sidebar.selectbox("Select Category", ["Home", "Shop"])
st.sidebar.markdown("Explore our clothing items!")

# Home Page
if page == "Home":
    # st.title("Welcome to Our Beautiful Cloth Shop!")
    st.markdown("---")

# Hero section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            """
            <div style='text-align: center;
            font-size: 2em;
            color: #441752; /* dark purple */
            background: linear-gradient(to right, #F4C2C2, #DB8DD0);
            padding: 50px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>
            <h1>Discover Your Style with Our Exclusive Clothing Collection!</h1>
            <p>Trendy. Comfortable. Affordable.</p>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("---")
    st.write(
        "Explore our wide range of clothing items. Use the sidebar to navigate through different categories and find your perfect outfit!"
    )
# Shop Page
elif page == "Shop":
    st.title("🛒 Clothing Shop")
    st.markdown("---")

# Dropdown for category selection
selected_category = st.selectbox("Select Category:", [""] + list(clothing_items.keys()))
    
if selected_category:
        clothing_list = clothing_items[selected_category]
        st.write(f"*Showing {selected_category}*")
        st.markdown("---")

# Grid for clothing items (3 columns) - Fixed size with width=250 for uniform look
        cols = st.columns(3)
        for i, clothing in enumerate(clothing_list):
            with cols[i % 3]:
                # Online image with fixed width for uniform size
                st.image(clothing["image"], width=150, caption=clothing["name"])  # width=250 for square uniform size

                # st.markdown(f"### {clothing['name']}")
                st.markdown(f"${clothing['price']}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; background-color: #441752; color: white; padding: 10px; border-radius: 5px;'>"
    "&copy; 2025 Cloth Shop | Made In Pakistan</div>",
    unsafe_allow_html=True
)