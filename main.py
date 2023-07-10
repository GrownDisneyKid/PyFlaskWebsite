# Justin McQueen
# SDEV 300:6381
# 08 JULY 2023
# Lab Seven

from flask import Flask, render_template, request, redirect, url_for
import hashlib

app = Flask(__name__)

def hash_password(password):
    salt = "saltwater"
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password

def check_password(password, hashed_password):
    salt = "saltwater"
    input_hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return input_hashed_password == hashed_password

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)
        with open('users.txt', 'a') as f:
            f.write(f"{username},{hashed_password}\n")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('users.txt', 'r') as f:
            for line in f:
                stored_username, stored_hashed_password = line.strip().split(',')
                if username == stored_username:
                    if check_password(password, stored_hashed_password):
                        print(f"Welcome, {username}!")
                        return render_template('about.html')
        return "Invalid username or password"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
    app.run()