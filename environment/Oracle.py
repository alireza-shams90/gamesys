import cx_Oracle

#this class is designed to log in to Oracle schmea and run the query provided
class Oracle():

	def __init__(self):
		self.connection = None

	def connect_2_db(self, schema,pw, db):
		self.connection = cx_oracle.conect(schema + '/' + pw + '@' + db)
		self.cursor = self.connection.cursor()

	def run_query(self, sql_string):
		self.cursor.execute(sql_string)
		result = self.cursor.fetchall()
		return result

	def disconnet(self):
		if self.connection:
			self.connection.close()