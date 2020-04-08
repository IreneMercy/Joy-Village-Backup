from __future__ import unicode_literals
from django.test import TestCase
from .models import Events

class EventsTestClass(TestCase):
    def setUp(self):
        self.event=Events(date='12/03/2020',venue='Nairobi',time="2Pm",image='images/child1.jpeg', title='Event',description='About The Event', pub_date='default')
        self.event.save_event()
    def test_instance(self):
        self.assertTrue(isinstance(self.event,Events))
