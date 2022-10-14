from http import HTTPStatus

from django.test import TestCase


class TestIndexPage(TestCase):
    def test_index_page_status_ok(self):
        res = self.client.get('/timetable/')
        self.assertEqual(res.status_code, HTTPStatus.OK)
