import math

class Sphere(object):
	def __init__(self, radius = 1.0, x = 0.0, y = 0.0, z = 0.0):
		self.radius = radius
		self.x = x
		self.y = y
		self.z = z
	
	def get_volume(self):
		return 4.0 / 3.0 * math.pi * self.radius ** 3
	
	def get_square(self):
		return 4 * math.pi * self.radius ** 2
	
	def get_radius(self):
		return self.radius
	
	def get_center(self):
		return (self.x, self.y, self.z)
	
	def set_radius(self, radius):
		self.radius = radius
	
	def set_center(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def is_point_inside(self, x, y, z):
		return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2) <= self.radius





s0 = Sphere(0.5) # test sphere creation with radius and default center
print(s0.get_center()) # (0.0, 0.0, 0.0)
print(s0.get_volume()) # 0.523598775598
print(s0.is_point_inside(0, -1.5, 0)) # False
s0.set_radius(1.6) 
print(s0.is_point_inside(0, -1.5, 0)) # True
print(s0.get_radius()) # 1.6