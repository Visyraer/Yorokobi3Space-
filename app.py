import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# This is our temporary storage room for your social posts
FEED_POSTS = []

# 🏠 Rule 1: Show your HTML layout out of the templates folder
@app.route('/')
def home():
    return render_template('index.html', posts=FEED_POSTS)

# 📬 Rule 2: Catch your typed text and save it live
@app.route('/save', methods=['POST'])
def save_post():
    message_content = request.form.get('user_message')
    if message_content:
        new_post = {
            "user": "yorokobi_dev", 
            "text": message_content,
            "likes": 0,
            "comments": 0
        }
        FEED_POSTS.append(new_post)
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
