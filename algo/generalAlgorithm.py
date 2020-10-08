from cube.cubeClass import Cube
from algo.step1 import Step1

class GeneralAlgorithm:
	def __init__(self, cube):
		self.cube = cube
		self.solution = list()

	def run(self):
		Completed_cube = Cube()
		step1 = Step1()
# 		step2 = Step2()
# 		step3 = Step3()
# 		step4 = Step4()
# 		step5 = Step5()
# 		step6 = Step6()
# 		step7 = Step7()

		step1.run(self.cube, self.solution)
# 		self.solution = step2.run(self.solution)
# 		self.solution = step3.run(self.solution)
# 		self.solution = step4.run(self.solution)
# 		self.solution = step5.run(self.solution)
# 		self.solution = step6.run(self.solution)
# 		self.solution = step7.run(self.solution)
		return(self.solution)