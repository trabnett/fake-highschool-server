from app import app

@app.route('/')
def welcome():
    return "Welcome! We are doing something now"