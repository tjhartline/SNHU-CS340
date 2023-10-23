import module
import os


# Get environment variables
host = os.getenv('MONGO_HOST', 'localhost')
port = int(os.getenv('MONGO_PORT', 27017))


# Instantiate the animal shelter class with appropriate credentials and collection details
shelter = module.AnimalShelter('aacuser', 'adminPassword', host, port, 'AAC', 'animals')

# Test create method
insertion_data = {'name': 'BuddyHartline', 'type': 'Pup', 'age': 2, 'breed': 'Blue PitBull'}
insertion_result = shelter.createOne(insertion_data)
if insertion_result:
	print(f'\nInsertion of 1 was successful: Inserted Data:\n{insertion_data}\n\nTest passed!')
else:
	print(f'\nInsertion of 1 failed. Record was not created.\nTest Failed!') 

# Insert many to test update and delete many later
insertion_datas = [{'name': 'Test1', 'type': 'NewDog', 'age': 4, 'breed': 'Poodle'}, {'name': 'Test2', 'type': 'NewPup', 'age': 1, 'breed': 'German Sheppard'}, {'name': 'Test1', 'type': 'NewDog', 'age': 4, 'breed': 'Poodle'}, {'name': 'Test2', 'type': 'NewPup', 'age': 1, 'breed': 'German Sheppard'}, {'name': 'Test1', 'type': 'NewDog', 'age': 4, 'breed': 'Poodle'}, {'name': 'Test2', 'type': 'NewPup', 'age': 1, 'breed': 'German Sheppard'}, {'name': 'Test1', 'type': 'NewDog', 'age': 4, 'breed': 'Poodle'}, {'name': 'Test2', 'type': 'NewPup', 'age': 1, 'breed': 'German Sheppard'}]
insertion_results = shelter.createMany(insertion_datas)
if insertion_results:
	print(f'\nInsertion of many was successful: Inserted Data:\n{insertion_datas}\n\nTest passed!')
else:
	print(f'\nInsertion of many failed. Records were not created.\nTest failed!') 


# Fetch and print all docs in collection for debug
#all_docs = shelter.read({})
#print(f'All documents in this collection: {all_docs}')

# Test read method
query = {'type': 'NewDog', 'type': 'NewPup', 'type': 'Pup'}
read_result = shelter.read(query)
print(f'\nRead results: \n{read_result}\n')


# Test update one method
update_query = {'name': 'BuddyHartline'}
update_data = {'type': 'Puppy', 'age': 1}
updated_count = shelter.update(update_query, update_data, multi=False)
read_update = shelter.read(update_query)
if updated_count > 0 and updated_count < 2:
	print(f'\n{updated_count} document(s) successfully updated.\n')
	print(f'Previous data:\n{insertion_data}\nUpdated data:\n{read_update}\n\nTest passed!!')
else:
	print('Record did not update. Test failed!\n')


# Test update many method
# Find matching info
update_querys = {'name': 'Test1'}
# Update with:
update_datas = {'type': 'Dog', 'age': 12, 'breed': 'Dogfish'}
updated_counts = shelter.update(update_querys, update_datas, multi=True)
read_updates = shelter.read(update_querys)
if updated_counts > 1:
	print(f'\n{updated_counts} documents updated successfully.\n')
	print(f'Previous data:\n{insertion_datas}\nUpdated data:\n{read_updates}\n\nTest passed!!\n')
	if updated_counts > 0 and updated_counts < 2:
		print(f'\n{updated_counts} document updated instead of many.\nTest failed.\n')
else:
	print(f'\nNo records were updated. Test failed!\n')
# Test delete one method
delete_query = {'name': 'BuddyHartline'}
deleted_count = shelter.delete(delete_query, multi=False)
# Verify that it did delete the record
if deleted_count > 0:
	print(f'\n{deleted_count} document deleted successfully. \nTest passed')
	if deleted_count > 1:
		print(f'\nDeleted {deleted_count} documents. Test to delete only one failed.')
else:
	print(f'\nFailed to delete document.')

# Test delete many method
delete_querys = {'breed': 'Dogfish'}
deleted_counts = shelter.delete(delete_querys, multi=True)
if deleted_counts > 0:
	print(f'\n{deleted_counts} documents deleted successfully.\nTest passed.')
elif deleted_counts < 2:
		print(f'\nDeleted {deleted_counts} document. Test to delete many failed.') 
else:
	print(f'\nFailed to delete documents.')
# --------------------------------------------------------------------
delete_querys2 = {'name': 'Test2'}
deleted_counts2 = shelter.delete(delete_querys2, multi=True)
if deleted_counts2 > 0:
	print(f'\n{deleted_counts2} documents deleted successfully.\nTest passed.')
elif deleted_counts2 < 2:
		print(f'\nDeleted {deleted_counts2} document. Test to delete many failed.') 
else:
	print(f'\nFailed to delete documents.')
