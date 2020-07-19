"""
this app designed to return the following requests for a member:
1. total win amount 2. total wager amount 3. total number of wager made
"""

from markupsafe import escape
from flask import Flask, jsonify, request
from Oracle import Oracle
from member_activity import Member

app = Flask(__name__)


@app.route('/total_win_amount/<member_id>')
def get_total_win_amount(member_id):
    activity_year_month = request.args.get('activity_year_month') or 'All'
    game_id = request.args.get('game_id') or 'All'
    logging.info(f"Handling the tot win amount request made for Member = {member_id}" \
                 f"activity_year_months = {activity_year_month} game_types = {game_id}")
    try:
        member = Player(member_id, activity_year_month, game_id)
    except Exception:
        logging.warning(f"Failed to handle the tot win request made for Member = {member_id}" \
                        f"activity_year_months = {activity_year_month} game_types = {game_id}")
    member_report = {"member_id": member_id,
                     "activity_year_month": activity_year_month,
                     "game_id": game_id,
                     "total_win_amount": member.total_win_amount()}
    return jsonify(member_report)


@app.route('/total_wager_amount/<member_id>')
def get_total_wager_amount(member_id):
    activity_year_month = request.args.get('activity_year_month')
    game_id = request.args.get('game_id')
    logging.info(f"Handling the tot wager amount request made for Member = {member_id}" \
                 f"activity_year_months = {activity_year_month} game_id = {game_id}")
    try:
        member = Player(member_id, activity_year_month, game_id)
    except Exception:
        logging.warning(f"Failed to handle the tot wager amount request made for " \
                        f"Member = {member_id}" \
                        f"activity_year_months = {activity_year_month} game_id = {game_id}")
    member_report = {"member_id": member_id,
                     "activity_year_month": activity_year_month,
                     "game_id": game_id,
                     "total_wager_amount": member.total_wager_amount()}
    return jsonify(member_report)


@app.route('/total_number_of_wagers/<member_id>')
def get_total_number_of_wagers(member_id):
    activity_year_month = request.args.get('activity_year_month')
    game_id = request.args.get('game_id')
    logging.info(f"Handling the tot number of wagers request made for Member = {member_id}" \
                 f"activity_year_months = {activity_year_month} game_id = {game_id}")
    try:
        member = Player(member_id, activity_year_month, game_id)
    except Exception:
        logging.warning(f"Failed to handling the number of wagers request made for " \
                        f"Member = {member_id}" \
                        f"activity_year_months = {activity_year_month} game_id = {game_id}")
    member_report = {"member_id": member_id,
                     "activity_year_month": activity_year_month,
                     "game_id": game_id,
                     "total_number_of_wagers":  member.total_number_of_wagers()}
    return jsonify(member_report)


if __name__ == '__main__':

    import logging
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    app.run("0.0.0.0", 5000, True)
