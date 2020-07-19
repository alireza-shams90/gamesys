import cx_Oracle

class CallOracle:
	# class is designed to connect to Oracle,
	# run a query and return the results and
	# get diconnected from the Oracle database

	def __init__(self):
		self.connection = None

	def connect_2_db(self, schema,pw, db):
		self.connection = cx_Oracle.connect(schema + '/' + pw + '@' + db)
		self.cursor = self.connection.cursor()

	def run_query(self, sql_string):
		self.cursor.execute(sql_string)
		result = self.cursor.fetchall()
		return result

	def disconnet(self):
		if self.connection:
			self.connection.close()