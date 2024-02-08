Project Description:

- SmartTour is a web application designed to revolutionize the way travelers plan their journeys by leveraging data and machine learning techniques. 
- It addresses the challenges faced by independent travelers in selecting suitable attractions according to their input (interest, budget and travel destination) and efficiently organizing their itineraries.
- The project involves understanding user pain points, constructing a dataset, developing a clustering model by Python, and crafting a user-friendly web application using HTML, JS and Python Flask.
- SmartTour accommodates two distinct user roles: 1. consumers: travelers seeking itinerary recommendations 2. producers: travellers inputting their travel recommendations
- Limitations: 1. The current geographical coverage is limited, as it solely encompasses four nations, namely Malaysia, Brunei, Singapore, and Indonesia. 2. The current system lacks the functionality to allow users to generate new travel recommendations in the event that they are unsatisfied with the initial suggestions. 3. In the event that a user's input does not align with any existing data in the system's database, SmartTour is unable to offer any recommendations. 4. Only recommend three places per day, up to a maximum of three days for travel.
- Future improvements: 1. Expanding the dataset, broadening the coverage to encompass more countries 2. Allowing users to request multiple itinerary recommendations 3. Integrating recommendations for local hotels alongside tourist attractions.

Clustering model (K-means):
- The main goal of this clustering is to categories attractions according to their geographical closeness, hence facilitating consumers' investigation of local attractions while travelling.
- First, the dataset will be filtered according to user inputs of ‘country’, ‘city’, and ‘category/interest’ and the clustering will be done on the geographical proximity denoted by ‘latitude’ and ‘longitude’.
- K=5. From the 5 clusters created, it will then iterate over the clusters and recommend 3 places from each cluster according to the user's budget.

![image](https://github.com/imannainaa/github.smarttour/assets/95207439/eb1ad3f4-0b5f-44b7-87f1-f88a024b42d6)
![image](https://github.com/imannainaa/github.smarttour/assets/95207439/1351ce5d-0600-47bf-afc0-f1c8e19c3421)
![image](https://github.com/imannainaa/github.smarttour/assets/95207439/414d5d1f-88e4-4226-8ddd-1977ee726382)


