import os
import unittest
import pythianbot
from errbot.backends.test import testbot, push_message, pop_message
from errbot import plugin_manager

class TestPythianBot(object):
    extra_plugin_dir = '.'

    def test_weather(self, testbot):
        push_message('!weather Uranus')
        assert 'Mine is warm...What about yours?' in pop_message()

    def test_time(self, testbot):
        push_message('!time Uranus')
        assert 'Mine is well...What about in yours?' in pop_message()

#    def test_location(self, testbot):
 #       push_message('!location set Interwebs')
#        assert 'Ok, None, trying to set your location to Interwebs' in pop_message()
#        assert self['None'] == 'Interwebs'
#        assert 0