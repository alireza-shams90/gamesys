from markupsafe import escape
from flask import Flask, jsonify, request
import logging
import Player, Oracle

app = Flask(__name__)

#this app designed to return the total win amount
#it has two optional variables as activity_year_month and game_id
#it logs the info in file named tot_win_amount.log
#

@app.route('/tot_win_amount/<member_id>')
def get_tot_win_amount(member_id):
	activity_year_month = request.args.get('activity_year_month') or 'All'
	game_id = request.args.get('game_id') or 'All'
	member = player(member_id, activity_year_month, game_id)
	logging.basicConfig(filename='tot_win_amount.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
	logging.info(f"Handling request made for Member = {member_id} , for activity_year_months = {activity_year_month}, and game types = {game_id}")
	member_report = {"member_id" : member_id,
					 "activity_year_month": activity_year_month,
					 "game_id": game_id,
					 "tot_win_amount" : member.tot_win_amount()}
	return jsonify(member_report)

@app.route('/tot_wager_amount/<member_id>')
def get_tot_wager_amount(member_id):
    activity_year_month = request.args.get('activity_year_month') or 'All'
    game_id = request.args.get('game_id') or 'All'
    logging.basicConfig(filename='tot_wager_amount.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.info(f"Handling request made for Member = {member_id} , for activity_year_months = {activity_year_month}, and game types = {game_id}")
    member = player(member_id,activity_year_month,game_id)
    member_report = {"member_id" : member_id,
					 "activity_year_month": activity_year_month,
					 "game_id": game_id,
	                "tot_wager_amount" : member.tot_wager_amount()}
    return jsonify(member_report)

@app.route('/num_of_wagers/<member_id>')
def get_num_of_wagers(member_id):
    activity_year_month = request.args.get('activity_year_month') or 'All'
    game_id = request.args.get('game_id') or 'All'
    logging.basicConfig(filename='num_of_wagers.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.info(f"Handling request made for Member = {member_id} , for activity_year_months = {activity_year_month}, and game types = {game_id}")
    member = player(member_id,activity_year_month,game_id)
    member_report = {"member_id" : member_id,
					 "activity_year_month": activity_year_month,
					 "game_id": game_id,
	                "num_of_wagers" :  member.num_of_wagers()}
    return jsonify(member_report)

if __name__ == '__main__':
	app.run("0.0.0.0", 5000, True)
