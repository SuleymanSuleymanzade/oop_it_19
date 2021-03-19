class Animal:
	def __init__(self, color):
		self.__color = color 

	def sound(self):
		pass 

class Cat(Animal):
	def __init__(self, color):
		super().__init__(color)

	def sound(self):
		return "meaw"

class Dog(Animal):
	def __init__(self, color):
		super().__init__(color)

	def sound(self):
		return "Wow Wow"
# --------------------------------------------------------


class GameCharacter:
	def __init__(self, name):
		self.__name = name
		self._coordinates = [(0, 0)]

	def moove(self, direction):
		pass

	@property
	def coordinate(self):
		return self._coordinates[-1]

class Knight(GameCharacter):
	def __init__(self, name):
		super().__init__(name)

	def moove(self, direction):
		last_coordinate = self.coordinate
		choose = (0,0)
		if direction == 'L':
			choose = (0, -1)
		if direction == "R":
			choose = (0, 1)
		if direction == "U":
			choose = (1, 0)
		if direction == "D":
			choose = (-1, 0)

		new_coordinate = (last_coordinate[0] + choose[0], last_coordinate[1] + choose[1])
		self._coordinates.append(new_coordinate)


class Wizard(GameCharacter):
	def __init__(self, name):
		super().__init__(name)

	def moove(self, direction):
		last_coordinate = self.coordinate
		choose = (0,0)
		if direction == 'L':
			choose = (0, -3)
		if direction == "R":
			choose = (0, 3)
		if direction == "U":
			choose = (3, 0)
		if direction == "D":
			choose = (-3, 0)

		new_coordinate = (last_coordinate[0] + choose[0], last_coordinate[1] + choose[1])
		self._coordinates.append(new_coordinate)




merlin = Wizard("Merlin")
merlin.moove("L")
merlin.moove("U")

dark_knight = Knight("DarkKnight")
dark_knight.moove("L")
dark_knight.moove("U")

print(merlin.coordinate)
print(dark_knight.coordinate)

