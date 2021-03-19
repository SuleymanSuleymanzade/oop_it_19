from utils.students import StudentGroup

def main():

	group1 = StudentGroup("IT2019")
	group1.add_student("Eljan", "Abbaszade", "e.a@bhos.edu.az")
	group1.add_student("Ayaz", "Panahov", "a.p@bhos.edu.az")
	group1.add_student("Murad", "Mammadov", "m.a@bhos.edu.az")
	group1.add_student("Samad", "Mammadov", "s.m@bhos.edu.az")

	#print(group1.get_student("e.a@bhos.edu.az").surname)
	print("---------------------------------------")
	group1.remove_student("e.a@bhos.edu.az")
	
	'''
	with open("my_group.pickle", "wb") as file:
		pickle.dump(group1, file)
	'''

	for student in group1.all_students:
		print(f"{student.name} {student.surname} {student.email}")


if __name__ == "__main__":
	main()