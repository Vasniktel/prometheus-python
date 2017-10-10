class Student(object):
	def __init__(self, name, conf):
		self.name = name
		self.exam = 0
		self.conf = dict(conf)
		self.lab_marks = [0 for i in range(self.conf['lab_num'])]
	
	def make_lab(self, m, n = None):
		mark = m if 0 < m <= self.conf['lab_max'] else self.conf['lab_max']
		
		if n is None and 0 in self.lab_marks:
			self.lab_marks[self.lab_marks.index(0)] = mark
		elif 0 <= n < self.conf['lab_num']:
			self.lab_marks[n] = mark
		
		return self
	
	def make_exam(self, m):
		self.exam = m if 0 < m <= self.conf['exam_max'] else self.conf['exam_max']
		return self
	
	def is_certified(self):
		sum_ = self.exam
		for mark in self.lab_marks:
			sum_ += mark
		
		return (sum_ * 1.0, sum_ / 100.0 >= self.conf['k'])



conf = {
'exam_max': 30,
'lab_max': 7,
'lab_num': 10,
'k': 0.61,
}
oleg = Student('Oleg', conf)
oleg.make_lab(1) \
.make_lab(8,0) \
.make_lab(1) \
.make_lab(10,7) \
.make_lab(4,1) \
.make_lab(5) \
.make_lab(6.5) \
.make_exam(32) # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 30
print(oleg.is_certified()) # (59.5, False)
oleg.make_lab(7,1) # labs: 7 7 5 6.5 0 0 0 7 0 0, exam: 30
print(oleg.is_certified()) # (62.5, True)