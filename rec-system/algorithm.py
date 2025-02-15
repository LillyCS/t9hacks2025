import pandas as pd
import numpy as np
from collections import Counter
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


BENEFITS_MAP = {
    'Hyaluronic Acid': ['hydration', 'anti-aging'],
    'Lactic Acid': ['hydration'],
    'Squalane': ['hydration', 'anti-aging'],
    'Shea Butter': ['hydration'],
    'Vitamin E':['hydration'],
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


def get_top_ingredients(products_df, x):
    """
    Get the top x most common ingredients from the products DataFrame, excluding inactive ingredients.
    """
    # List of inactive and commonly used ingredients - exclude these
    inactive_ingredients = ["Water", "Glycerin", "Phenoxyethanol","Xanthan Gum","Alcohol Denat", "Carbomer"]
    ingredients_list = products_df['Ingredients'].str.split(',').tolist()

    # Flatten the list of lists
    all_ingredients = [ingredient.strip() for sublist in ingredients_list for ingredient in sublist]

    # Filter out inactive ingredients
    active_ingredients = [ingredient for ingredient in all_ingredients if ingredient.lower() not in [inactive.lower() for inactive in inactive_ingredients]]
    ingredient_counts = Counter(active_ingredients)
    most_common_ingredients = ingredient_counts.most_common(x)

    for ingredient, count in most_common_ingredients:
        print(f"{ingredient}: {count}")


def get_ingredient_benefits(products_df, ingredient_name):
    """
    Map common ingredients to their benefits.
    """
    benefits = []
    for ingredient, benefit in BENEFITS_MAP.items():
        if ingredient_name.lower() in ingredient.lower():
            benefits.extend(benefit)
    
    return list(set(benefits))
    

def search_for_ingredient(products_df, ingredient_names):
    """
    Search the ingredients column to find any ingredients that match the list of ingredient names and print out their count.
    """
    ingredients_list = products_df['Ingredients'].str.split(',').tolist()

    # Flatten the list of lists
    all_ingredients = [ingredient.strip() for sublist in ingredients_list for ingredient in sublist]

    # Filter ingredients that match any of the ingredient names
    matching_ingredients = [ingredient for ingredient in all_ingredients if any(name.lower() in ingredient.lower() for name in ingredient_names)]
    ingredient_counts = Counter(matching_ingredients)

    for ingredient, count in ingredient_counts.items():
        print(f"{ingredient}: {count}")


def main():
    products_df = pd.read_csv('../resources/data/cosmetics.csv')

    skin_type = input("Enter your skin type (Dry, Oily, Combination, Normal): ")
    concerns = input("Enter your skin concerns (comma-separated): ").split(',')
    print("Enter your budget from the following options (1-4):\n")
    print("1. $0 - $25\n")
    print("2. $25 - $50\n")
    print("3. $50 - $100\n")
    print("4. $100+\n")
    budget = input("")

    print("Generating recommendations...\n")
    print('------------------------------------------------------------------------------------------------------------')
    
    scores = []

    for _, product in products_df.iterrows():
        score = 0
        if product[skin_type] == 1:
            score += 3

        score += product["Rank"]

        product_benefits = get_ingredient_benefits(products_df, product['Ingredients'])

        matching_goals = set(concerns).intersection(set(product_benefits))

        score += len(matching_goals) * 1.5

        if budget == '1':
            comp_price = 25
            if product['Price'] <= float(comp_price):
                score += 1
        elif budget == '2':
            comp_price = 50
            if product['Price'] <= float(comp_price) and product['Price'] > 25:
                score += 1
        elif budget == '3':
            comp_price = 100
            if product['Price'] <= float(comp_price) and product['Price'] > 50:
                score += 1
        else:
            comp_price = 500
            if product['Price'] <= float(comp_price) and product['Price'] > 100:
                score += 1

        scores.append(score)

    products_df['score'] = scores

    # Display top recommendations by Label group
    grouped = products_df.groupby('Label').apply(lambda x: x.sort_values('score', ascending=False)).reset_index(drop=True)
    top_products = grouped.loc[:,['Label', 'Name', 'Brand', 'Price', 'score']].groupby('Label').first().reset_index()
    print(top_products)

if __name__ == '__main__':
    main()