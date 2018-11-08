#imagine this is a custom string gathered from a DB
STRING_JSON_FROM_DB_EXAMPLE = "{\
	'customField1': 'Unit Number',\
	'customField2': 'Bedroom Count',\
	'customField3': 'Residents'\
}"

print(type(STRING_JSON_FROM_DB_EXAMPLE))

example = eval(STRING_JSON_FROM_DB_EXAMPLE) 	 # one line for conversion to dict

print(type(example))

print(example.get('customField1'))

