from flask import Flask, render_template
import tools
app = Flask("gemelch-website")

@app.route("/")
@app.route("/about/")
def about():
    return render_template("about.html")
    
@app.route("/maps/")
@app.route("/maps/<map_name>")
def maps(map_name=None):
    print(map_name)
    maps_names, maps_images = tools.get_maps_files_list()
    if map_name is not None:
        maps = dict()
        for i in range(len(maps_names)):
            print(len(maps_names))
            print(i, maps_names[i], maps_images[i])
            maps[maps_names[i]] = maps_images[i]
        return render_template("maps.html", map_name = map_name, 
        maps_names = maps_names, map_image_name = maps[map_name])
    return render_template("maps.html", maps_names = maps_names)
    
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
    players_list = tools.get_players_list()
    return render_template("players.html", players_list = players_list)

@app.route("/tables/")
@app.route("/tables/<table_name>")
def tables(table_name=None):
    print(table_name)
    tables_names, tables_images = tools.get_tables_files_list()
    if table_name is not None:
        tables = dict()
        print(len(tables_names))
        for i in range(len(tables_names)):
            print(i, tables_names[i], tables_images[i])
            tables[tables_names[i]] = tables_images[i]
        return render_template("tables.html", tables_names = tables_names, 
        tables_images = tables_names, table_image_name = tables[table_name])
    return render_template("tables.html", tables_names = tables_names, tables_images = tables_names)
   

if __name__ == '__main__':
    app.run(debug = True)
