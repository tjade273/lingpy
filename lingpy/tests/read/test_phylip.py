"""
Basic tests for the Phylip module.
"""

from ..util import test_data
from lingpy.read.phylip import *

matrix = """4
German	0.0	0.8	0.4	0.7
English	0.8	0.0	0.5	0.8
French	0.4	0.5	0.0	0.3
Norwegian	0.7	0.8	0.3	0.0"""

def test_read_dst():

    t1,m1 = read_dst(test_data('phylip_basic.dst'))
    t2,m2 = read_dst(test_data('phylip_tabstop.dst'), taxlen=0)
    t3,m3 = read_dst(matrix, taxlen=0)
    
    assert t1 == t2 == t3

    ma0 = sum([m[0] for m in m1]) # 1.9
    ma1 = sum([m[1] for m in m1]) # 2.1
    ma2 = sum([m[2] for m in m1]) # 1.2
    ma3 = sum([m[3] for m in m1]) # 1.8
    mb0 = sum([m[0] for m in m2]) # 1.9
    mb1 = sum([m[1] for m in m2]) # 2.1
    mb2 = sum([m[2] for m in m2]) # 1.2
    mb3 = sum([m[3] for m in m2]) # 1.8

    assert round(ma0,2) == round(mb0,2) == 1.9
    assert round(ma1,2) == round(mb1,2) == 2.1
    assert round(ma2,2) == round(mb2,2) == 1.2
    assert round(ma3,2) == round(mb3,2) == 1.8

def test_read_scorer():

    scorer = read_scorer(test_data('dolgo.matrix'))

    assert sorted(scorer.chars2int)[0] == '+'
    for letter in 'PTKRSM':
        assert scorer[letter,'V'] == -10

    assert max(scorer.chars2int.values()) == 15


