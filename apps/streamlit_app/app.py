import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SOLUTION02_SRC = PROJECT_ROOT / "solutions" / "solution02" / "src"

sys.path.insert(0, str(SOLUTION02_SRC))

from main import (  # noqa: E402
    generate_memorable_password,
    generate_pin,
    generate_random_password,
)


st.set_page_config(
    page_title="Password Generator",
    page_icon="🔐",
    layout="centered",
)


# Clear the generated password when the password type changes.
def clear_password():
    st.session_state.password = ""


# Sidebar
with st.sidebar:
    st.title("🔐 Password Generator")
    st.write("Create secure passwords in seconds.")

    st.divider()

    st.subheader("About")
    st.write(
        "Generate PINs, random passwords, "
        "and memorable passwords."
    )

    st.caption("Built with Python and Streamlit.")


# Main page
st.title("🔐 Password Generator")
st.write("Choose a password type and customize its options.")


# Preserve the generated password across Streamlit reruns.
if "password" not in st.session_state:
    st.session_state.password = ""


# Password type selection
password_type = st.selectbox(
    "Choose password type",
    [
        "PIN",
        "Random Password",
        "Memorable Password",
    ],
    on_change=clear_password,
)


# Password options
if password_type == "PIN":
    length = st.slider(
        "PIN length",
        min_value=4,
        max_value=12,
        value=6,
    )

elif password_type == "Random Password":
    length = st.slider(
        "Password length",
        min_value=8,
        max_value=64,
        value=16,
    )

    include_numbers = st.checkbox(
        "Include numbers",
        value=True,
    )

    include_symbols = st.checkbox(
        "Include symbols",
        value=True,
    )

else:
    word_count = st.slider(
        "Number of words",
        min_value=2,
        max_value=8,
        value=4,
    )

    separator = st.text_input(
        "Word separator",
        value="-",
    )


st.divider()


# Generate password
if st.button("Generate Password", type="primary"):
    try:
        if password_type == "PIN":
            new_password = generate_pin(length)

        elif password_type == "Random Password":
            new_password = generate_random_password(
                length,
                include_numbers=include_numbers,
                include_symbols=include_symbols,
            )

        else:
            new_password = generate_memorable_password(
                word_count=word_count,
                separator=separator,
            )

        st.session_state.password = new_password

    except (ValueError, TypeError, LookupError) as error:
        st.session_state.password = ""
        st.error(str(error))


# Display generated password
if st.session_state.password:
    st.subheader("🔐 Your Generated Password")

    with st.container(border=True):
        st.code(
            st.session_state.password,
            language=None,
        )

        st.caption(
            "Hover over the password box to reveal the copy icon."
        )

        if st.button("🗑️ Clear Password"):
            st.session_state.password = ""
            st.rerun()
