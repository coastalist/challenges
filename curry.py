def capital_indexes(string):
	i_list = []
	count = -1
	for i in string:
		count = count + 1 
		if i.isupper():
			i_list.append(count)
	print(i_list)
	return i_list


capital_indexes("TestStringS")

