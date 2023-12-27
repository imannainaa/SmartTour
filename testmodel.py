from model import recommend_itinerary  # Import your function
import pandas as pd

# Sample input data
country_choice = 'Malaysia'
city_choices = 'Terengganu'
budget_choice = '3'  # Budget range 1001 - 2000
interests_choice = ['1', '3']  # Shopping and Culture

# Call the recommendation function
recommendations = recommend_itinerary(country_choice, city_choices, budget_choice, interests_choice)

# Print the recommendations
for day, recs in enumerate(recommendations, start=1):
    print(f"Day {day} Recommendations:")
    if recs:
        for i, rec in enumerate(recs, start=1):
            print(f"  Place {i}: {rec}")
    else:
        print("  No recommendations for this day")
    print()
