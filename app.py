from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='.')

# This is our temporary storage room for your social posts
FEED_POSTS = [
    {"user": "retro_fan", "text": "Yo, love the new mascot design! The Frutiger Aero colors look perfect.", "likes": 12, "comments": 3},
    {"user": "miku_space", "text": "This feels so peaceful. No repetitive algorithmic recommendations, just vibes.", "likes": 24, "comments": 7}
]

# 🏠 Rule 1: When someone loads the page, show them your HTML layout
@app.route('/')
def home():
    return render_template('index.html', posts=FEED_POSTS)

# 📬 Rule 2: When someone clicks "Post Update", catch their text and save it
@app.route('/save', methods=['POST'])
def save_post():
    # Grab the text out of the form box envelope
    message_content = request.form.get('user_message')
    
    # If the user typed something, add a new card to our storage room list
    if message_content:
        new_post = {
            "user": "yorokobi_dev", 
            "text": message_content,
            "likes": 0,
            "comments": 0
        }
        FEED_POSTS.append(new_post)
    
    # Send the user right back to the homepage to see their new post
    return redirect('/')

if __name__ == '__main__':
    # Start the server engine!
    app.run(debug=True, port=5000)
