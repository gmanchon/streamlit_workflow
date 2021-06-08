import streamlit as st


@st.cache
def get_coordinates(address):
    return f"coordinates for {address}"


@st.cache
def get_satellite(coordinates):
    return f"satellite for {coordinates}"


# address input
address = st.text_input("address")

# coordinates result stored as input in order to be transmitted
# from one page to the next
coords_placeholder = st.empty()

coordinates = coords_placeholder.text_input("coordinates")
click_address = st.button("resolve address", key=1)
if click_address:
    coordinates = coords_placeholder.text_input("coordinates", value=get_coordinates(address), key=1)

# satellite result stored as input in order to be transmitted
# from one page to the next
satellite_placeholder = st.empty()

satellite = satellite_placeholder.text_input("satellite")
click_coords = st.button("resolve satellite", key=2)
if click_coords:
    coordinates = coords_placeholder.text_input("coordinates", value=get_coordinates(address), key=1)
    satellite = satellite_placeholder.text_input("satellite", value=get_satellite(coordinates), key=2)
