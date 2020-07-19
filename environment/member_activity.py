"""
this is the Member class with methods to query the database and return the following
1. total win amount 2.total wager amount 3. number of wagers
above values can be returned for a member_id for all or specific
month and for all or specific game
"""

import logging
from Oracle import Oracle


class Member:

    def __init__(self, member_id, activity_year_month, game_id):
        logging.basicConfig(filename="member.log", filemode='a', format="%(asctime)s - %(message)s"
                            , datefmt="%d-%b-%y %H:%M:%S")
        self.member_id = member_id
        self.activity_year_month = activity_year_month
        self.game_id = game_id
        self.sql_string_condition = ''

        if not self.activity_year_month == 'All':
            self.sql_string_condition = ' and activity_year_month = {activity_year_month}'
            if not self.game_id == 'All':
                self.sql_string_condition = self.sql_string_condition + ' and game_id = {game_id}'
        self.sql_string_condition = self.sql_string_condition + ' group by member_id'
        try:
            self.dbquery = Oracle()
            self.dbquery.connect_2_db('SCHEMA', 'PW', 'DB')
        except Exception:
            logging.warning(f"Failed to query the total win amount for member {self.member_id}")

    def tot_win_amount(self):
        sql_string = """
                        select sum(win_amount)
                        from revenue_analysis
                        where member_id = {member_id}
                     """
        sql_string = sql_string + self.sql_string_condition
        sql_string.format(member_id=self.member_id,
                          activity_year_month=self.activity_year_month,
                          game_id=self.game_id)
        try:
            win_amount = self.dbquery.run_query(sql_string)
        except Exception:
            logging.warning(f"Failed to query the total win amount for member {self.member_id}")
        return win_amount

    def tot_wager_amount(self):
        sql_string = """
                        select sum(wager_amount)
                        from revenue_analysis
                        where member_id = {member_id}
                    """
        sql_string = sql_string + self.sql_string_condition
        sql_string.format(member_id=self.member_id,
                          activity_year_month=self.activity_year_month,
                          game_id=self.game_id)
        try:
            wager_amount = self.dbquery.run_query(sql_string)
        except Exception:
            logging.warning("Failed to query the total wager amount for"
                            "member {member_id}".format(member_id=self.member_id))
        return wager_amount

    def num_of_wagers(self):
        sql_string = """
                        select count(wager_amount)
                        from revenue_analysis
                        where member_id = {member_id}
                     """
        sql_string = sql_string + self.sql_string_condition
        sql_string.format(member_id=self.member_id,
                          activity_year_month=self.activity_year_month,
                          game_id=self.game_id)
        try:
            tot_num_of_wagers = self.dbquery.run_query(sql_string)
        except Exception:
            logging.warning(f"Failed to query the total win amount for member {self.member_id}")
        return tot_num_of_wagers
