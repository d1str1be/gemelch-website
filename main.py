from flask import Flask, render_template
import tools
app = Flask("gemelch-website")

@app.route("/")
def base():
    return render_template("base.html")
    
@app.route("/maps/")
def maps():
    return render_template("maps.html")
    
@app.route("/rules/")
def rules():
    return render_template("rules.html")

@app.route("/turns/")
@app.route("/turns/<turn_number>")
def turns(turn_number=None):
    turns_list = tools.get_turns_files_list()
    if turn_number is None:
        turn_number = turns_list[-1][-6:-4]
        print(turn_number)
    else:
        turn_number = turn_number[-2:]   
    turns_list = turns_list[-1::-1]
    return render_template("turns.html", number=turn_number, turns_list=turns_list)
    
@app.route("/players/")
def players():
    return render_template("players.html")

@app.route("/tables/")
def tables():
    tables_list = tools.get_tables_files_list()
    return render_template("tables.html")
    
@app.route("/about/")
def about():
    return render_template("about.html")
app.run(debug = True)

