from flask import Flask, render_template, request
import pandas as pd

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

        # Sort by Review Rating and Previous Purchases
        sorted_df = filtered_df.sort_values(by=['Review Rating', 'Previous Purchases'], ascending=[True, True])

        # Get top 10 and bottom 10
        top_10 = sorted_df.head(10)
        bottom_10 = sorted_df.tail(10)

        return render_template('results.html', top_10=top_10, bottom_10=bottom_10)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
