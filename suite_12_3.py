import unittest
import tests_12_3


arbitrary_test = unittest.TestSuite()
arbitrary_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
arbitrary_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(arbitrary_test)

