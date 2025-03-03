from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Sample user data (for demonstration purposes)
users = {
    "user1": "password1",
    "user2": "password2",
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user_id = request.form['user_id']
    password = request.form['password']

    if user_id in users and users[user_id] == password:
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid User ID or Password')
        return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
