import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
from typing import List
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


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


def get_ingredient_benefits(ingredients: str) -> List[str]:
    """Map ingredients to their benefits."""
    benefits = []
    for ingredient_name, benefit_list in BENEFITS_MAP.items():
        if ingredient_name.lower() in ingredients.lower():
            benefits.extend(benefit_list)
    return list(set(benefits))


def registration_page():
    st.title("Create an Account")

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
            else:
                st.error("Passwords do not match!")


def questionnaire_page():
    st.title("Complete Your Skin Profile")

    # Skin type selection
    skin_type = st.selectbox(
        "What's your skin type?",
        ['Dry', 'Oily', 'Combination', 'Normal']
    )

    # Skin concerns/goals selection based on available benefits
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

        st.session_state.page = 'recommendations'
        st.rerun()


def recommendations_page():
    st.title("Your Personalized Routine ✨")
    
    try:
        products_df = pd.read_csv('../resources/data/cosmetics.csv')
        
        scores = []
        for _, product in products_df.iterrows():
            score = 0
            
            # Check skin type match
            if product[st.session_state.user_profile['skin_type']] == 1:
                score += 3
            
            # Rating score
            score += product['Rank']
            
            # Check ingredients for skin concern/goals match
            product_benefits = get_ingredient_benefits(product['Ingredients'])
            matching_goals = set(st.session_state.user_profile['concerns']).intersection(set(product_benefits))
            score += len(matching_goals) * 1.5
            
            # Budget match
            budget = st.session_state.user_profile['budget']
            price = float(product['Price'])
            
            if budget == '1' and price <= 25:
                score += 1
            elif budget == '2' and 25 < price <= 50:
                score += 1
            elif budget == '3' and 50 < price <= 100:
                score += 1
            elif budget == '4' and price > 100:
                score += 1
            
            scores.append(score)
        
        products_df['score'] = scores
        
        # Gathering product recommendations to build routine
        grouped = products_df.groupby('Label').apply(lambda x: x.sort_values('score', ascending=False)).reset_index(drop=True)
        
        top_products = grouped.loc[:, ['Label', 'Name', 'Brand', 'Price', 'score', 'Ingredients']]\
            .groupby('Label').first().reset_index()
        
        # Display recommendations
        for _, product in top_products.iterrows():
            st.write("---")
            st.subheader(f"{product['Label']}")
            
            col1, col2 = st.columns([2, 3])
            
            with col1:
                st.write(f"**{product['Brand']}**") # Bolded brand name
                st.write(f"*{product['Name']}*") # Italicized name
                st.write(f"Price: ${product['Price']:.2f}") # Rounded price
            
            with col2:
                st.write("**Key Benefits:**")
                benefits = get_ingredient_benefits(product['Ingredients'])
                for benefit in benefits:
                    if benefit in st.session_state.user_profile['concerns']:
                        st.write(f"✓ {benefit}")
                
                with st.expander("See Ingredients"):
                    st.write(product['Ingredients'])
    
    except Exception as e:
        st.error("Error loading recommendations.")
        st.write(f"Error details: {str(e)}")


def main():
    if st.session_state.page == 'register':
        registration_page()
    elif st.session_state.page == 'questionnaire':
        questionnaire_page()
    elif st.session_state.page == 'recommendations':
        recommendations_page()


if __name__ == '__main__':
    main()