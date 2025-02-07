import streamlit as st
import time

# Initialize session state correctly
if "no_count" not in st.session_state:
    st.session_state.no_count = 0  # Ensures persistence across reruns
if "gif_index" not in st.session_state:
    st.session_state.gif_index = 0  # For rotating cute GIFs
if "hidden_button" not in st.session_state:
    st.session_state.hidden_button = False  # Secret button appears after 3 "No" clicks

# List of cute reaction GIFs
gif_list = [
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3M5bG1kMXE5eDU4d3RiYnl2NW1keTNlZTYwc2o4NDduMng3bDdtYSZlcD12MV9pbnRlcm5naWZfYnlfaWQmY3Q9Zw/I1nwVpCaB4k36/giphy.gif",
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3E5NGpsc3QwYnQxN29tc294Z3M1YnFndDhzbmh6ODRlZjJvN3pvdyZlcD12MV9pbnRlcm5naWZfYnlfaWQmY3Q9Zw/GwskZm1jXg8cDvuZJ6/giphy.gif",
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXMxZndiNnJhcTNmcno3aTc5cndhOGFnbWQxYzB0c3g5emxma2F4dSZlcD12MV9pbnRlcm5naWZfYnlfaWQmY3Q9Zw/OjiSLBg7s27kaIGS8o/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTN6OXVqODY3b3NkM3NtZjZzaHMyOHBpNzlzeDZwYTQ1bzJxM3V4ayZlcD12MV9pbnRlcm5naWZfYnlfaWQmY3Q9Zw/OPU6wzx8JrHna/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHdlbzQ2d3hldnpxbzJsOTY3cHRxZmc3YXk3bm0xdHlqbjZtb3R5NCZlcD12MV9pbnRlcm5naWZfYnlfaWQmY3Q9Zw/L95W4wv8nnb9K/giphy.gif",
]

# Define no responses
no_responses = [
    "Please... 🥺",
    "Pretty please? 🥺👉👈",
    "Come on, say yes! 😚",
    "Don't break my heart 💔",
    "This is your last chance... 😢",
    "You have no choice, YOU are my valentine 😾"
]

# Custom CSS for styling
st.markdown(
    """
    <style>
    .big-font {
        font-size:24px !important;
        font-weight: bold;
    }
    .heart {
        color: red;
        font-size: 36px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💖 A Special Question for You 💖")

st.markdown("Hey there, gorgeous! 🌹 There's something I've been meaning to ask you...")
st.subheader("Will you be my Valentine? 😘")

# Buttons layout
col1, col2 = st.columns(2)

with col1:
    yes_clicked = st.button("Yes! ❤️", key="yes_button")

with col2:
    if st.session_state.no_count < len(no_responses) - 1:
        no_clicked = st.button("No 💔", key="no_button")
    else:
        no_clicked = False  # Hide the No button at the end

# Handle button clicks
if yes_clicked:
    st.balloons()
    st.success("Yay! I knew you'd say yes! 🎉💖 Can't wait for our special day! 😍")
    time.sleep(2)
    st.markdown("<h2 style='color: red;'>🎆Yayyyyy you my Valentine! 🎆</h2>", unsafe_allow_html=True)
    st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXc4enBmdzd1ZTFiNDYxbGw4ejN6ZnV1NTBqNDVrb3NuaXJzdzhtdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LTcau7EnQLhHkxxG2u/giphy.gif", use_container_width=True)
elif no_clicked:
    st.session_state.no_count += 1
    if st.session_state.no_count < len(no_responses) - 1:
        st.session_state.gif_index = (st.session_state.gif_index + 1) % len(gif_list)  # Rotate GIFs
    if st.session_state.no_count == 3:
        st.session_state.hidden_button = True  # Show secret button after 3 rejections

# Love Meter Progress Bar
st.progress(st.session_state.no_count / len(no_responses))

# Display progressive text based on "No" clicks
if st.session_state.no_count > 0:
    st.markdown(
        f'<p class="big-font">{no_responses[min(st.session_state.no_count, len(no_responses) - 1)]}</p>',
        unsafe_allow_html=True
    )

    # ✅ **Fixed Issue: Stop showing GIFs after the last "No"**
    if st.session_state.no_count < len(no_responses) - 1:
        st.image(gif_list[st.session_state.gif_index], use_container_width=True)

# Fun dynamic message if taking too long
if st.session_state.no_count == 2:
    st.warning("You're making me nervous... 😳")

if st.session_state.no_count == 4:
    st.error("Okay, now you're just being mean... 💔")

# Secret hidden button appears after 3 rejections
if st.session_state.hidden_button:
    if st.button("Secret Message 💌", key="secret_button"):
        st.success("Even if you keep saying no... I'll always like you! 💕😊")

# Final step: Show only "Yes" with cat image
if st.session_state.no_count >= len(no_responses) - 1:
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTq6Gof65yYHfeDkedkm_Fbg033Hy-qgGrn2A&s",
        caption="You have no choice, YOU are Valentine 😼🔪",
        use_container_width=True
    )
    st.button("Yes! ❤️", key="final_yes_button")  # Unique key to prevent duplication errors

# Reset button to restart the process manually
if st.button("Reset App 🔄", key="reset_button"):
    st.session_state.clear()  # Clears all session state variables
    st.rerun()  # Forces a rerun of the app
