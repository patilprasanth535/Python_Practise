__author__ = 'prasanth'
from behave import when
from pages.Numbers import Vipdatabase

@when(u'we add the vip')
def step(self):
    vip = vipdatabase()
    vip.test_add_name()

@when(u'we load the vip data')
def step(self):
    vip = vipdatabase()
    vip.test_load()

@when(u'we save the vip data')
def step(self):
    vip = vipdatabase()
    vip.test_save()
