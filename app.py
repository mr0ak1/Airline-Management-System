import streamlit as st
from avl_tree import AVLTree
from flights_data import get_flights
from datetime import date

# Initialize the AVL Tree and insert sample flight data
avl_tree = AVLTree()
flights = get_flights()
for flight in flights:
    avl_tree.insert(flight)

# Set the page configuration
st.set_page_config(page_title="Airline Management System", layout="wide")

# Main title
st.title("Airline Management System")

# --- Flight Search Bar ---
st.markdown("### Plan Your Travel")

# Trip type selection
trip_type = st.radio("Trip Type", ('Round Trip', 'One Way'), horizontal=True)

# Flight search form
with st.form("search_flights"):
    st.write("**Search Flights**")
    
    # Origin and Destination cities
    col1, col2 = st.columns(2)
    with col1:
        origin = st.selectbox('Origin', ['Select Departure City', 'New York', 'London', 'Delhi', 'Sydney'])
    with col2:
        destination = st.selectbox('Destination', ['Select Arrival City', 'New York', 'London', 'Delhi', 'Sydney'])
    
    # Travel Dates
    col3, col4 = st.columns(2)
    with col3:
        departure_date = st.date_input('Departure', date.today())
    with col4:
        if trip_type == 'Round Trip':
            return_date = st.date_input('Return', date.today())
    
    # Passengers and Class selection
    passengers = st.selectbox('Passengers', [1, 2, 3, 4, 5])
    travel_class = st.selectbox('Class', ['Economy', 'Business', 'First'])

    # Submit button for search
    search = st.form_submit_button("Search Flights")

    if search:
        # Search for flights using the AVL Tree
        search_results = avl_tree.search_by_route(origin, destination)
        if search_results:
            st.write(f"Available flights from {origin} to {destination}:")
            for flight in search_results:
                st.write(flight)
        else:
            st.write("No flights found for the selected route.")

# --- Benefits Section ---
st.markdown("---")
st.markdown("### Enjoy exclusive benefits when booking directly with us!")
col7, col8, col9 = st.columns(3)

with col7:
    st.image("https://img.icons8.com/ios/50/free-cancellation.png", width=50)
    st.write("**Free Cancellation**")

with col8:
    st.image("https://img.icons8.com/ios/50/points.png", width=50)
    st.write("**100 Loyalty Bonus Points**")

with col9:
    st.image("https://img.icons8.com/ios/50/low-fee.png", width=50)
    st.write("**Low Platform Fee**")

# --- Additional Feature Section Placeholder ---
st.markdown("### Why Book with Us?")
st.write("Include details about features, loyalty programs, customer support, etc.")

# --- Footer ---
st.markdown("---")
st.markdown("#### Airline Management System © 2024")
