import json

#imagine this is a custom string gathered from a DB
STRING_JSON_FROM_DB_EXAMPLE = "{\
	'customField1': 'Unit Number',\
	'customField2': 'Bedroom Count',\
	'customField3': 'Residents'\
}"

print(type(STRING_JSON_FROM_DB_EXAMPLE))		# oviously string

example_dict = eval(STRING_JSON_FROM_DB_EXAMPLE) 	# one line for conversion to dict

print(type(example_dict))				# now a Python Dict

print(example_dict.get('customField1'))			# will be 'Unit Number'

# ------------------------------
# now let's change the dict and turn it back to a string to save back to DB

example_dict.update({'customField1': 'Changed'})	# update field in dict

print(example_dict.get('customField1'))			# will be 'Changed'

json_string_for_db = json.dumps(example_dict)		# dump JSON back to string

print(type(json_string_for_db))				# type string

print(json_string_for_db)				# show changed JSON string from start that goes in DB
# ------------------------------

# these were all tests showing data types and conversions
# here is the real code that would be needed.

real_dict = eval(STRING_JSON_FROM_DB_EXAMPLE)

# if user wants to change a field name, it is simple
real_dict.update({'customField1': 'Apartment Number'})

# now update the db...but without a connection let's just print it out
print(json.dumps(real_dict))
