import pytest
from project import *

def test_decorationprints():
    assert print_decorative_lines() == None


def test_getUserInput():
    urls = URLReader().read_urls()
    assert urls == ['https://www.youtube.com/watch?v=igQ83YAck6M&ab_channel=TNTSports\n', 
                    'https://www.youtube.com/watch?v=kriaFd5Sggk&ab_channel=ABCNews']
    

def test_choose_type():
    video = VideoType()
    # Testing default value
    video.type = 1
    assert video.get_type() == 1
    # Testing out of range 
    video.type = 10
    with pytest.raises(TypeNotInRangeException):
        video.validate_type()


def test_filer():
    assert str(filter(1, "https://www.youtube.com/watch?v=jNQXAC9IVRw&ab_channel=jawed")) \
        == ('<Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">')


