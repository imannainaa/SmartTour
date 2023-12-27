from flask import Flask, redirect, url_for, request, render_template
from model import recommend_itinerary
import pandas as pd
import csv

# Load the recommendation function from the pickled file
#with open('recommend_itinerary.pickle', 'rb') as f:
    #recommend_itinerary = pickle.load(f)

app = Flask(__name__, static_folder='static')

@app.route('/success/<country>/<city_choices>/<budget>/<interest>')
def success(country, city_choices, budget, interest):
   country = country
   city_choices = city_choices
   budget = budget
   interest = interest

   recommendation = recommend_itinerary(country, city_choices, budget, interest)

   print(f"Country: {country}")
   print(f"City Choices: {city_choices}")
   print(f"Budget: {budget}")
   print(f"Interests: {interest}")

   # Print the recommendation to the console
   print(f"Recommendation: {recommendation}")
   
   #return recommend_itinerary(country, city_choices, budget, interest)
   #return recommendation
   return render_template('recommendations.html', recommendations=recommendation)
  
@app.route('/consumer',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      country = request.form['country']
      city = request.form['cities']
      budget = request.form['budget']
      interest = request.form.getlist('interest')
      return redirect(url_for('success',country = country, city_choices = city, budget = budget, interest=interest))
   else:
      return render_template('consumer.html')
   

@app.route('/producer', methods=['POST'])
def submit_place():
    if request.method == 'POST':
        country = request.form['country']
        city = request.form['city']
        place_name = request.form['placeName']
        category = request.form['category']
        rating = request.form['rating']
        priceMYR = request.form['priceMYR']
        long = request.form['longitude']
        lat = request.form['latitude']

        # Create a dictionary with the new data
        new_data = {
            'Place_Name': place_name,
            'Category': category,
            'Country': country,
            'City': city,
            'PriceMYR': priceMYR,
            'Rating': rating,
            'Lat': lat,
            'Long': long
        }

        # Specify the CSV file path
        csv_file = 'tourism.csv'

        # Open the CSV file in append mode
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)

            # Write the new data as a row in the CSV file
            writer.writerow([new_data['Place_Name'], new_data['Category'], new_data['Country'], 
                             new_data['City'], new_data['PriceMYR'], new_data['Rating'], new_data['Lat'], new_data['Long']])

        return render_template('thankyou.html', country=country, city=city, place_name=place_name, 
                               category=category, rating=rating, priceMYR=priceMYR, long=long, lat=lat)

if __name__ == '__main__':
   app.run(debug = True)