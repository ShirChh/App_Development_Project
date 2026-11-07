class User:

	def __init__(self, user_id,  first_name, last_name, membership, gender, remarks):

		self.__user_id = user_id
		self.__first_name = first_name
		self.__last_name = last_name
		self.__membership = membership
		self.__gender = gender
		self.__remarks = remarks

	#Accessor methods
	def get_user_id(self):
		return self.__user_id
	
	def get_first_name(self):
		return self.__first_name
	
	def get_last_name(self):
		return self.__last_name

	def get_gender(self):
		return self.__gender
	
	def get_membership(self):
		return self.__membership
	
	def get_remarks(self):
		return self.__remarks
	
	# Mutator methods
	def set_user_id(self, user_id):
		self.__user_id = user_id
		
	def set_first_name(self, first_name):
		self.__first_name = first_name
		
	def set_last_name(self, last_name):
		self.__last_name = last_name
	
	def set_gender(self, gender):
		self.__gender = gender
	
	def set_membership(self, membership):
		self.__membership = membership
		
	def set_remarks(self, remarks):
		self.__remarks = remarks
	
	@classmethod
	def from_database_row(cls, row_data):
		"""Create a User object from database row data"""
		return cls(
			user_id=row_data[0],
			first_name=row_data[1],
			last_name=row_data[2],
			gender=row_data[3],
			membership=row_data[4],
			remarks=row_data[5]
		)