from django.test import TestCase

from timetable.models import StudyGroup


class TestStudyGroupModel(TestCase):
    def test_study_group_str(self):
        sg_name = 'ФИИТ-22'
        sg = StudyGroup()
        sg.name = sg_name
        self.assertEqual(str(sg), sg_name)
