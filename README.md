# t9hacks2025
Lilly Nguyen's submission for the T9Hacks Health-a-thon 2025

## Inspiration
My journey into skincare started when I was a child, watching my mom use various skincare products on her face. I was always curious about what each product was, what it does, and when I could start using it. 

The skincare industry can be overwhelming to navigate with countless products on the market and complex ingredient lists which make it difficult for consumers to make informed decisions. Many people struggle to find products that suit their skin type, address their specific concerns, and fit their budget. Skincare is also a huge part of mental health and self-image. I was inspired to create GlowGuide to make the world of skincare accessible for everyone, regardless of your expertise in skincare.

## What it does
GlowGuide is a recommendation system that takes in user data on their skin needs in order to create a personalized skincare routine

Specifically, the website:
- Collects user information to create an account
- Gathers skin specific needs through a questionnaire
- Analyzes a database of skincare products on the market
- Provides personalized product recommendations based on skin type compatibility, ingredient benefits, price range alignment, and product ratings
- Displays detailed product information to including key benefits and full ingredient lists

## How I built it
I use Sephora skincare products listed in this Kaggle dataset [https://www.kaggle.com/datasets/dominoweir/skincare-product-ingredients](https://www.kaggle.com/datasets/dominoweir/skincare-product-ingredients) to build my simple recommendation system. 
- Wireframing: To lay out my initial lo-fi prototype for the web application
- Streamlit: For creating an interactive web application with a clean and user-friendly interface
- Pandas: Primary programming language for algorithm development
- Custom Recommendation Algorithm: Created my own scoring system that puts weights on each of the categories (skin type, ingredients, budget, rating)
- Ingredient Analysis System: Created a mapping system that analyzes key skincare ingredients and their benefits

## Challenges I ran into
- Project Scoping: I wanted to implement web scraping using a tool like Selenium to gather my own up-to-date data on skincare products, but I quickly realized that would take too long. So, I pivoted to focusing on first finding my data online and building my recommendation system based on the data.
- Recommendation System: I initially wanted to dabble with data science techniques such as collaborative and content-based filtering to built a robust recommendation engine, but without experience, I decided this was too time-consuming. I also played around with using different weights for my categories in the custom scoring.
- Web Development: I struggled connecting my algorithm with the UI until I did some more research and found Streamlit, which was a really cool and fast way to build apps using a Python framework. The documentation is well-written, so I was able to integrate it within the 24 hours.
- Ingredient Analysis: I conducted A LOT of research into what active ingredients are useful for specific skin concerns like hyperpigmentation and anti-aging. I used this knowledge and research to create my ingredients-benefits mapping system.

## Accomplishments that we're proud of
1. I'm really proud of myself for creating a functional application that works! This is a topic I'm passionate about. I felt that I proved to myself that I could pull off an idea from start to finish, while making smart decisions about pivoting and changing courses as needed in such a short period of time.
2. I learned a new web development tool, Streamlit, in 24-hours and was successful in integrating it into my own website. The user-interface is simple, yet effective and user-friendly.
3. I tried to use best coding practices along the way to keep everything organized and modular.
4. I honed in on my data analysis and programming skills to develop a simple scoring algorithm and logic on the back-end.

## What we learned
- It's ok to start over and change directions
- Read documentation and Google everything
- Plan out your time wisely and be realistic

## What's next for GlowGuide
- Create user profiles that save in a database; allow users to favorite products and store their skin profile
- Use more sophisticated machine learning algorithms like content-based and collaborative-based filtering to improve recommendations over time based on user feedback and trends
- Add product links and images to recommendations
- Flag and exclude skin allergies from user's skin profile
