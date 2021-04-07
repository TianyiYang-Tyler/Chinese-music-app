import unittest
from trial_function import cambridge_student
class NameTestCase(unittest.TestCase):
	def test_cambridge_student(self):
		cam_student=cambridge_student(0,'African')
		self.assertEqual(cam_student,False)
if __name__=='__main__':
	unittest.main()     