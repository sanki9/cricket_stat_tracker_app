from flask import Flask
from data import create_table

app = Flask(__name__)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
    contestants = ['Jesse','Simran','Sankalp','Sanjay','Sumat','Akhil']
    selections = [['Head','Nortje'],['Marsh','Zampa'],['Warner','Bumrah'],['Kohli','Starc'],['Yadav','Boult'],['Pooran','Pandya']]
    return create_table(contestants, selections)

if __name__ == "__main__":
    app.run(debug=True)

