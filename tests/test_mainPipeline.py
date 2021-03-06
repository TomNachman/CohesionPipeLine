from unittest import TestCase
from src.Cohesion import mainPipeline

class Test(TestCase):
    def test_calculate_cohesion_score(self):
        # Give here full path!
        bad_score, bad_topics = mainPipeline.cohesion_score('..\\resources\\tests\\bad_division.txt')
        good_score, good_topics = mainPipeline.cohesion_score('..\\resources\\tests\\good_division.txt')
        print('bad_score: ', bad_score)
        print('bad_topics: ', bad_topics)

        print('good_score: ', good_score)
        print('good_topics: ', good_topics)

        if bad_score > good_score:
            self.fail()


