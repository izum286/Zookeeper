from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from animals import *

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)

animal_index = {
    '0': (camel, 'camel'),
    '1': (lion, 'lion'),
    '2': (deer, 'deer'),
    '3': (goose, 'goose'),
    '4': (bat, 'bat'),
    '5': (rabbit, 'rabbit')
}

the_end_message = '---\nThe end of the program. To check another habitat restart the watcher please.'


class Zookeeper(StageTest):
    def generate(self):
        tests = [TestCase(stdin=index, attach=(index, animal_index[index])) for index in animal_index]
        return tests

    def check(self, reply, attach):
        if attach[1][0].strip() not in reply.strip():
            return CheckResult.wrong(f'There should be a {attach[1][1]} in aviary number {attach[0]}')
        if the_end_message not in reply.strip():
            return CheckResult.wrong('You should output the message about the end of the program!')
        return CheckResult.correct()


if __name__ == '__main__':
    Zookeeper('zookeeper.zookeeper').run_tests()
