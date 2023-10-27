from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)

# Dictionary to store shortened URLs
url_dict = {}

# Function to generate a random string for the shortened URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Shorten URL route
@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    short_url = generate_short_url()
    url_dict[short_url] = original_url
    return render_template('success.html', short_url=short_url)

# Redirect to original URL route
@app.route('/<short_url>')
def redirect_url(short_url):
    if short_url in url_dict:
        return redirect(url_dict[short_url])
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
