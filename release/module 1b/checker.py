# !pip install nose
import os, sys, re
import unittest
from unittest.mock import patch
from unittest import TestCase
from nose.tools import assert_equal, assert_true, assert_almost_equal
from importlib import reload
from io import StringIO

class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
        
def parse_dog_age(msg):
    human_age = re.findall("\d+\.\d+ in human", msg)
    human_age = human_age[0].split(' ')[0].strip()
    return float(human_age)


@patch('builtins.input', return_value='-1')
def test_negative(self, mock_input):
    f = StringIO()
    with RedirectStdStreams(stdout=f, stderr=f):
        calculator()
    return str(f.getvalue())

@patch('builtins.input', return_value='n')
def test_text_input(self, mock_input):
    f = StringIO()
    with RedirectStdStreams(stdout=f, stderr=f):
        calculator()
    return str(f.getvalue())

@patch('builtins.input', return_value='1')
def test_one(self, mock_input):
    f = StringIO()
    with RedirectStdStreams(stdout=f, stderr=f):
        calculator()
    return str(f.getvalue())

@patch('builtins.input', return_value='2')
def test_two(self, mock_input):
    f = StringIO()
    with RedirectStdStreams(stdout=f, stderr=f):
        calculator()
    return str(f.getvalue())

@patch('builtins.input', return_value='3')
def test_three(self, mock_input):
    f = StringIO()
    with RedirectStdStreams(stdout=f, stderr=f):
        calculator()
    return str(f.getvalue())

@patch('builtins.input', return_value='4')
def test_four(self, mock_input):
    f = StringIO()
    with RedirectStdStreams(stdout=f, stderr=f):
        calculator()
    return str(f.getvalue())

@patch('builtins.input', return_value='5')
def test_five(self, mock_input):
    f = StringIO()
    with RedirectStdStreams(stdout=f, stderr=f):
        calculator()
        return str(f.getvalue())

@patch('builtins.input', return_value='6')
def test_six(self, mock_input):
    f = StringIO()
    with RedirectStdStreams(stdout=f, stderr=f):
        calculator()
    return str(f.getvalue())

@patch('builtins.input', return_value='7')
def test_seven(self, mock_input):
    f = StringIO()
    with RedirectStdStreams(stdout=f, stderr=f):
        calculator()
    return str(f.getvalue())