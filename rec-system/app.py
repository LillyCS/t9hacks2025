import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
from typing import List
# from streamlit_extras.switch_page_button import switch_page


LOGO_PINK = "../resources/img/logo_pink.png"
LOGO_DARK = "../resources/img/logo_dark.png"
LOGO_WHITE = "../resources/img/logo_main.png"

BENEFITS_MAP = {
    'Hyaluronic Acid': ['hydration', 'anti-aging'],
    'Lactic Acid': ['hydration'],
    'Squalane': ['hydration', 'anti-aging'],
    'Shea Butter': ['hydration'],
    'Vitamin E': ['hydration'],
    'Niacinamide': ['redness reduction'],
    'Aloe Vera': ['redness reduction'],
    'Centella': ['redness reduction'],
    'Antioxidants': ['redness reduction'],
    'Chamomile': ['redness reduction'],
    'Vitamin C': ['brightening', 'anti-aging'],
    'Licorice': ['brightening'],
    'Liquorice': ['brightening'],
    'Ascorbic Acid': ['brightening'],
    'Arbutin': ['brightening'],
    'Retinol': ['anti-aging'],
    'Vitamin A': ['anti-aging'],
    'Green tea': ['anti-aging'],
    'Jojoba Oil': ['anti-aging'],
    'Salicylic Acid': ['acne'],
    'Benzoyl Peroxide': ['acne'],
    'Tea Tree Oil': ['acne'],
    'Sulfur': ['acne'],
    'Mulberry': ['acne']
}


def get_ingredient_benefits(ingredients: str) -> List[str]:
    """Map ingredients to their benefits."""
    benefits = []
    for ingredient_name, benefit_list in BENEFITS_MAP.items():
        if ingredient_name.lower() in ingredients.lower():
            benefits.extend(benefit_list)
    return list(set(benefits))


st.set_page_config(
    page_title="Skincare Recommender",
    page_icon="✨"
)

if 'page' not in st.session_state:
    st.session_state.page = 'register'

st.logo(
    LOGO_DARK,
    icon_image=LOGO_DARK,
)

st.sidebar.image(LOGO_WHITE, use_column_width=True)

def registration_page():
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
                st.session_state.page = 'questionnaire'
                st.rerun()
                # st.switch_page('questionnaire')
            else:
                st.error("Passwords do not match!")


def questionnaire_page():
    st.title("Complete Your Skin Profile")

    # Skin type selection
    skin_type = st.selectbox(
        "What's your skin type?",
        ['Dry', 'Oily', 'Combination', 'Normal']
    )

    # Skin concerns selection based on available benefits
    all_benefits = set()
    for benefits in BENEFITS_MAP.values():
        all_benefits.update(benefits)
    
    concerns = st.multiselect(
        "What are your skin concerns?",
        sorted(list(all_benefits))
    )

    st.write("Select your budget range:")
    budget = st.radio(
        "Budget Range",
        ["1", "2", "3", "4"],
        format_func=lambda x: {
            "1": "$0 - $25",
            "2": "$25 - $50",
            "3": "$50 - $100",
            "4": "$100+"
        }[x]
    )

    if st.button("Get Recommendations"):
        st.session_state.user_profile = {
            'skin_type': skin_type,
            'concerns': concerns,
            'budget': budget
        }
        st.success("Skin profile successful! Proceeding to your personalized skincare routine...")

        # st.session_state.page = 'recommendations'
        # st.experimental_rerun()


def main():
    if st.session_state.page == 'register':
        registration_page()
    elif st.session_state.page == 'questionnaire':
        questionnaire_page()


if __name__ == '__main__':
    main()