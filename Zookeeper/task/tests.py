from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from animals import *

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class Zookeeper(StageTest):
    def generate(self):
        return [TestCase(attach=camel)]

    def check(self, reply, attach):
        if attach.strip() not in reply.strip():
            return CheckResult.wrong('You should output a camel!')
        return CheckResult.correct()


if __name__ == '__main__':
    Zookeeper('zookeeper.zookeeper').run_tests()
