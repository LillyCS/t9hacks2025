import streamlit as st

st.set_page_config(
    page_title="Skincare Recommender",
    page_icon="✨"
)

LOGO_PINK = "../resources/img/logo_pink.png"
LOGO_DARK = "../resources/img/logo_dark.png"
LOGO_WHITE = "../resources/img/logo_main.png"

st.logo(
    LOGO_DARK,
    icon_image=LOGO_DARK,
)

st.sidebar.image(LOGO_WHITE, use_column_width=True)


def main():
    st.title("Create an Account")

    st.sidebar.header("Your Skin Profile")

    with st.form(key='registration_form'):
        first_name = st.text_input("First Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        submit_button = st.form_submit_button(label='Register')

        if submit_button:
            if password == confirm_password:
                st.success("Registration successful! Proceeding to skin profile...")
            else:
                st.error("Passwords do not match!")

if __name__ == '__main__':
    main()