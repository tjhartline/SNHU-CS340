from pymongo import MongoClient

class AnimalShelter(object):
	'''CRUD operations for animals collection in MongoDB'''
	
	def __init__(self, user, password, host, port, db, col):
		'''
		Initialize Connection.
		Parameters should be read from the environment or configuration, not hardcoded.
		'''
		self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
		self.database = self.client[db]
		self.collection = self.database[col]
		
	def create(self, data):
		'''
		Implement the C in CRUD.
		Insert document into the specified MongoDB collection.
		'''
		if data:
			result = self.collection.insert_one(data)
			return True if result.inserted_id else False
		else:
			print('Nothing to save, data parameter is empty.')
			return False
			
	def read(self, query):
		print(f'Query received: {query}, type: {type(query)}')  # Debugging line
		'''
		Implement the R in CRUD.
		Query documents from the specified MongoDB collection.
		'''

		if query is not None:  # This will be True for an empty dictionary
    			result = list(self.collection.find(query))
    			return result if result else []
		else:
    			print('Query parameter is empty')  
    			return []
