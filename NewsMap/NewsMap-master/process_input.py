import cgi

def getinput():
	formData = cgi.FieldStorage()
	input = []
	company = formData.getvalue('company')
	month = formData.getvalue('month')
	day = formData.getvalue('day')
	year = formData.getvalue('year')
	time = formData.getvalue('time')
	input.append(company)
	input.append(month)
	input.append(day)
	input.append(year)
	input.append(time)
	return input


if __name__ == __main__:
	print getinput()
