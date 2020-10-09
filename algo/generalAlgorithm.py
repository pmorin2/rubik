from cube.cubeClass import Cube
from algo.step1 import Step1
from algo.step2 import Step2

class GeneralAlgorithm:
	def __init__(self, cube):
		self.cube = cube
		self.solution = list()

	def run(self):
		Completed_cube = Cube()
		step1 = Step1()
		step2 = Step2()
# 		step3 = Step3()
# 		step4 = Step4()
# 		step5 = Step5()
# 		step6 = Step6()
# 		step7 = Step7()

		step1.run(self.cube, self.solution)
		step2.run(self.cube, self.solution)
# 		step3.run(self.cube, self.solution)
# 		step4.run(self.cube, self.solution)
# 		step5.run(self.cube, self.solution)
# 		step6.run(self.cube, self.solution)
# 		step7.run(self.cube, self.solution)
		return(self.solution)