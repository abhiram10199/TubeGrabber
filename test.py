import pytest
from project import *

def test_decorationprints():
    assert decorationPrints() == None


def test_getUserInput():
    urls = ReadURLs().readURLs()
    assert urls == ['https://www.youtube.com/watch?v=igQ83YAck6M&ab_channel=TNTSports\n', 
                    'https://www.youtube.com/watch?v=kriaFd5Sggk&ab_channel=ABCNews']
    
