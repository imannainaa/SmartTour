import pandas as pd
from sklearn.cluster import KMeans
import pickle

def recommend_itinerary(country_choice, city_choices, budget_choice, interests_choice):
    print("recommend_itinerary function called")  # Add this line

    # Load the dataset (you should provide the path to your dataset)
    data = pd.read_csv('tourism.csv')

    # Mapping of country choices to country names
    country_mapping = {
        'Malaysia': 'Malaysia',
        'Indonesia': 'Indonesia',
        'Singapore': 'Singapore',
        'Brunei': 'Brunei'
    }

    # Get the selected country
    selected_country = country_mapping.get(country_choice)

    # Mapping of budget choices to budget ranges
    budget_mapping = {
        '1': (0, 500),
        '2': (501, 1000),
        '3': (1001, 2000),
        '4': (2001, 3000),
        '5': (3001, float('inf'))
    }

    # Check if budget_choice is valid and get the selected budget range
    if budget_choice in budget_mapping:
        selected_budget_range = budget_mapping[budget_choice]
    else:
        # Handle invalid budget_choice
        selected_budget_range = (0, float('inf'))

    # Mapping of interest choices to interests
    interests_mapping = {
        '1': 'Shopping',
        '2': 'Nature',
        '3': 'Culture',
        '4': 'Amusement Park'
    }

    # Get the selected interests
    selected_interests = [interests_mapping.get(choice) for choice in interests_choice]

    # Filter the dataset based on user input (one city)
    filtered_data = data[(data['Country'] == selected_country) & (data['City'] == city_choices) & (data['Category'].isin(selected_interests))]

    # Check if the filtered dataset is empty or contains fewer samples than needed for clustering
    if filtered_data.empty or len(filtered_data) < 3:
        return "Not enough data for clustering."

    # Convert 'PriceMYR' column to float
    filtered_data['PriceMYR'] = filtered_data['PriceMYR'].astype(float)

    # Select only the columns we need for clustering
    X = filtered_data[['Lat', 'Long']]

    # Choose the number of clusters
    k = 5

    # Calculate the budget based on the selected budget range
    budget = sum(selected_budget_range) / 3  # Divide budget equally for 3 days

    # Create and train the KMeans model
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X)

    # Add cluster labels to the dataset
    filtered_data['Cluster'] = kmeans.labels_

    # Initialize variables for recommendation
    recommendations = []

    # Iterate over clusters and recommend 3 places from each cluster
    for cluster in range(k):
        cluster_data = filtered_data[filtered_data['Cluster'] == cluster]
        if cluster_data.empty:
            continue  # Skip empty clusters

        cluster_data = cluster_data.sort_values(by='PriceMYR')  # Sort places by price
        daily_budget = budget  # Assign the budget for each day

        daily_recommendations = []
        daily_budget_spent = 0

        for _, place in cluster_data.iterrows():
            if daily_budget_spent + place['PriceMYR'] <= daily_budget and len(daily_recommendations) < 3:
                daily_recommendations.append(place['Place_Name'])
                daily_budget_spent += place['PriceMYR']

        recommendations.append(daily_recommendations)

    # Fill in missing recommendations for Day 1
    if len(recommendations) < 3:
        recommendations.insert(0, [])

    # Ensure a maximum of 3 recommendations for Day 3
    if len(recommendations) > 3:
        recommendations[2] = recommendations[2][:3]

    return recommendations


with open('recommend_itinerary.pickle', 'wb') as f:
    pickle.dump(recommend_itinerary, f)