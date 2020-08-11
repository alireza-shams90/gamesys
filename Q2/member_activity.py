import logging
from db import CallOracle


class Member:
    """
    this is the Member class with methods to query the database and return the following
    1. total win amount 2.total wager amount 3. number of wagers
    above values can be returned for a member_id for all or specific
    month and for all or specific game
    """

    def __init__(self, member_id, activity_year_month, game_id):
        """
        Class initiation creates a log file for warnings. Then it constructs the
        sql_string_condition which will be based on the provided activity_year_month
        and game_id - if all nothing will be added to the script. Finally it creates
        an object of the class CallOracle and log into the Database. Exception logs
        the failure in connection to DB. DB details can be added in a configure file.
        :param member_id: Unique identifier for a member
        :param activity_year_month: Specific month e.g. 202007 with default value of 'All'
        :param game_id: Specific game ID e.g. 1234 with default value of all games
        """
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
            self.dbquery = CallOracle()
            self.dbquery.connect_2_db('SCHEMA', 'PW', 'DB')
        except Exception:
            logging.warning(f"Failed to query the total win amount for member {self.member_id}")

    def total_win_amount(self):
        """
        The main sql string selects from the table revenue_analysis grouped
        by the meber_id to find the total win amount. The sql_string_condition
        which was created in class initiation will be queried from the database
        to find the total win amount for specified month and game ID.
        :return: total win amount
        """
        sql_string = """
                        select sum(win_amount)
                        from revenue_analysis
                        where member_id = {member_id}
                     """
        sql_string = sql_string + self.sql_string_condition
        sql_string = sql_string.format(member_id=self.member_id,
                                       activity_year_month=self.activity_year_month,
                                       game_id=self.game_id)
        try:
            win_amount = self.dbquery.run_query(sql_string)
        except Exception:
            logging.warning(f"Failed to query the total win amount for member {self.member_id}")
        return win_amount

    def total_wager_amount(self):
        """
        The main sql string selects from the table revenue_analysis grouped
        by the meber_id to find the total wager amount. The sql_string_condition
        which was created in class initiation will be queried from the database
        to find the total wager amount for the specified month and the game ID.
        :return: total wager amount
        """
        sql_string = """
                        select sum(wager_amount)
                        from revenue_analysis
                        where member_id = {member_id}
                    """
        sql_string = sql_string + self.sql_string_condition
        sql_string = sql_string.format(member_id=self.member_id,
                                       activity_year_month=self.activity_year_month,
                                       game_id=self.game_id)
        try:
            wager_amount = self.dbquery.run_query(sql_string)
        except Exception:
            logging.warning("Failed to query the total wager amount for"
                            "member {member_id}".format(member_id=self.member_id))
        return wager_amount

    def total_number_of_wagers(self):
        """
        The main sql string selects from the table revenue_analysis grouped
        by the meber_id to count the total number of wagers. The sql_string_condition
        which was created in class initiation will be queried from the database
        to find the total number of wagers for the specified month and the game ID.
        :return: total number of wagers made
        """
        sql_string = """
                        select count(wager_amount)
                        from revenue_analysis
                        where member_id = {member_id}
                     """
        sql_string = sql_string + self.sql_string_condition
        sql_string = sql_string.format(member_id=self.member_id,
                                       activity_year_month=self.activity_year_month,
                                       game_id=self.game_id)
        try:
            tot_num_of_wagers = self.dbquery.run_query(sql_string)
        except Exception:
            logging.warning(f"Failed to query the total win amount for member {self.member_id}")
        return tot_num_of_wagers
