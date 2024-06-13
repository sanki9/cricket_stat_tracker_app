from flask import Flask, render_template # type: ignore
from data import create_table

app = Flask(__name__)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
    contestants = ['Jesse','Simran','Sankalp','Sanjay','Sumat','Akhil']
    selections = [['Head','Nortje'],['Marsh','Zampa'],['Warner','Bumrah'],['Kohli','Starc'],['Yadav','Boult'],['Pooran','Pandya']]
    res = create_table(contestants, selections)
    return render_template('webpage.html',batterData=res[0], bowlerData=res[1])

if __name__ == "__main__":
    app.run(debug=True)

