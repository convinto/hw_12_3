import unittest

import tests_12_1
import tests_12_2

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(condition=is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_w = tests_12_1.Runner('Name_w')             #создаем объект класса Runner
        for i in range(10):                     #вызываем метод 10 раз
            runner_w.walk()
        self.assertEqual(runner_w.distance, 50)       #сравнение distance с ожидаемым значением

    @unittest.skipIf(condition=is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_r = tests_12_1.Runner('Name_r')
        for i in range(10):
            runner_r.run()
        self.assertEqual(runner_r.distance, 100)

    @unittest.skipIf(condition=is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_chal1 = tests_12_1.Runner('Name_ch1')
        run_chal2 = tests_12_1.Runner('Name_ch2')
        for i in range(10):
            run_chal1.run()
            run_chal2.walk()
        self.assertNotEqual(run_chal1.distance, run_chal2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(condition=is_frozen, reason='Тесты в этом кейсе заморожены')
    def setUp(self):        #производится перед каждым тестированием
        self.runer1 = tests_12_2.Runner('Усэйн', 10)
        self.runer2 = tests_12_2.Runner('Андрей', 9)
        self.runer3 = tests_12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            print_result = {}
            for key, value in i.items():
                print_result[key] = value.name
            print(print_result)

    @unittest.skipIf(condition=is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_run1(self):
        self.sprint1 = tests_12_2.Tournament(90, self.runer1, self.runer3)
        self.all_results = self.sprint1.start()
        max_place_sprint = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(max_place_sprint == 'Ник')

        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(condition=is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_run2(self):
        self.sprint2 = tests_12_2.Tournament(90, self.runer2, self.runer3)
        self.all_results = self.sprint2.start()
        max_place_sprint = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(max_place_sprint == 'Ник')

        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(condition=is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_run3(self):
        self.sprint3 = tests_12_2.Tournament(90, self.runer1, self.runer2, self.runer3)
        self.all_results = self.sprint3.start()
        max_place_sprint = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(max_place_sprint == 'Ник')

        TournamentTest.all_results[3] = self.all_results

if __name__ == '__main__':
    unittest.main()
