from flask import Flask, render_template, request
import pandas as pd
from collections import defaultdict

app = Flask(__name__)

# Load your CSV file into a DataFrame
df = pd.read_csv('static/shopping_trends.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        age_start = int(request.form.get('age_start', 0))
        age_end = int(request.form.get('age_end', 100))
        gender = request.form.get('gender', 'All')
        category = request.form.get('category', 'All')
        location = request.form.get('location', 'All')
        season = request.form.get('season', 'All')
        material = request.form.get('material', 'All')

        # Filter the DataFrame based on inputs
        filtered_df = df[(df['Age'] >= age_start) & (df['Age'] <= age_end)]

        if gender != 'All':
            filtered_df = filtered_df[filtered_df['Gender'] == gender]
        if category != 'All':
            filtered_df = filtered_df[filtered_df['Category'] == category]
        if location != 'All':
            filtered_df = filtered_df[filtered_df['Location'] == location]
        if season != 'All':
            filtered_df = filtered_df[filtered_df['Season'] == season]
        if material != 'All':
            filtered_df = filtered_df[filtered_df['Textile Material'] == material]

        # Create a defaultdict to aggregate ratings and purchases for each item
        item_dict = defaultdict(lambda: {'total_rating': 0, 'total_purchases': 0, 'count': 0})

        for _, row in filtered_df.iterrows():
            item = row['Item Purchased']
            rating = row['Review Rating']
            purchases = row['Previous Purchases']
            
            item_dict[item]['total_rating'] += rating
            item_dict[item]['total_purchases'] += purchases
            item_dict[item]['count'] += 1

        # Average the ratings and purchases
        for item in item_dict:
            item_dict[item]['average_rating'] = item_dict[item]['total_rating'] / item_dict[item]['count']
            item_dict[item]['total_purchases'] = item_dict[item]['total_purchases']  # Keep as total or average

        # Sort items based on average rating and total purchases
        sorted_items = sorted(item_dict.items(), key=lambda x: (x[1]['average_rating'], x[1]['total_purchases']))

        # Get top 10 and bottom 10 items
        top_10 = sorted_items[:6]
        bottom_10 = sorted_items[-6:]

        return render_template('results.html', top_10=top_10, bottom_10=bottom_10)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
