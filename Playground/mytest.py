def gradingStudents( grades ):
    five = 5
	for i in range(len(grades)):
		r = grades[i] % five
		if grades[i] >= 38 and r >= 3 :
			grades[i] += five - r

    return grades