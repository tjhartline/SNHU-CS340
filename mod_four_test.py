import module_four
import os

# Get environment variables
host = os.getenv('MONGO_HOST', 'localhost')
port = int(os.getenv('MONGO_PORT', 27017))

# Instantiate the animal shelter class with appropriate credentials and collection details
shelter = module_four.AnimalShelter('aacuser', 'adminPassword', host, port, 'AAC', 'animals')

# Test create method
insertion_data = {'name': 'Test', 'type': 'Dog', 'age': 2, 'breed': 'Blue PitBull'}
insertion_result = shelter.create(insertion_data)
print(f'Insertion was successful: {insertion_data}')

# Fetch and print all docs in collection for debug
all_docs = shelter.read({})
print(f'All documents in this collection: {all_docs}')

# Test read method
query = {'type': 'Dog'}
read_result = shelter.read(query)
print(f'Read results: {read_result}')