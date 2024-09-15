import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_runner = runner.Runner('Elsa')
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    def test_run(self):
        test_runner = runner.Runner('Nika')
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    def test_challenge(self):
        test_runner1 = runner.Runner('Elsa')
        test_runner2 = runner.Runner('Nika')
        for _ in range(10):
            test_runner1.run()
            test_runner2.walk()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)


if __name__ == '__main__':
    unittest.main()