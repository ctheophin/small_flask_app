from flask import Flask, render_template
from modules import convert_to_dict
app = Flask(__name__)

players_list = convert_to_dict('players2.csv')



@app.route('/')
def index():
    ids_list = []
    name_list = []
# fill one list with the number of each presidency and
# fill the other with the name of each president
    for player in players_list:
        ids_list.append(player['Nbr'])
        name_list.append(player['Player'])
    # players_list[0]['Player']
    # players_list[0]['Place of Birth']
    pairs_list = zip(ids_list, name_list)
    return render_template('index.html', pairs=pairs_list, the_title="Players Index")
# your code here
@app.route('/player/<num>')
def detail(num):
    for player in players_list:
        if player['Nbr'] == num:
            players_dict = player
            break
    return render_template('players.html', play=players_dict, the_title=players_dict['Player'])




# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
