
import datetime
import pickle 

class Person:
	'''Class creates a person'''
	def __init__(self, name='unknown', surname='unknown'):
		self._name = name
		self._surname = surname
	
	# getters and setters
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, new_name):
		self._name = new_name

	@property
	def surname(self):
		return self._surname

	@surname.setter
	def surname(self, new_surname):
		self._surname = new_surname

class Student(Person):
	def __init__(self, name, surname, email):
		super().__init__(name, surname)
		self.__email = email
		self.__marks = []

	@property
	def email(self):
		return self.__email
	
	@email.setter
	def email(self, new_email):
		self.__email = new_email

	def add_mark(self, mark):
		self.__marks.append((mark, datetime.datetime.now()))

	def reset_marks(self):
		self.__marks = []

	@property
	def marks(self):
		return self.__marks

	def get_gpt(self):
		all_marks = [m[0] for m in self.__marks]
		return sum(self.all_marks) / len(self.all_marks)

class StudentGroup:
	def __init__(self, group_id):
		self.__students = []
		self.__group_id = group_id

	def add_student(self, name, surname, email):
		student = Student(name, surname, email)
		self.__students.append(student)

	def get_student(self, email, id = False):
		for s_id, student in enumerate(self.__students):
			if student.email == email:
				if id:
					return s_id
				else:
					return student

	def remove_student(self, email):
		searched_student = self.get_student(email, id = True)
		del self.__students[searched_student]

	def get_student_by_name_surname(self, name, surname):
		search_by = (name, surname)
		for person in self.__students:
			if person.name == search_by[0] and person.surname == search_by[1]:
					return person
	@property 
	def all_students(self):
		return self.__students

