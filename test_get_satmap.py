#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:01:33 2023

@author: rebeccawhittingham
"""


import pytest
from codeass1 import get_satmap
from codeass1 import net



def test_get_satmap():
    
    with pytest.raises(FileNotFoundError) as exc_info:
        get_satmap('MadeUpNonsenseFileName1029384756')
        assert 'The filename provided can not be found on this computer.' in str(exc_info.value)
    
    Lirsatmap = get_satmap('aigean_lir_20230107_123152.asdf')
    assert Lirsatmap.instrument == 'Lir', 'get_satmap is not creating satmap object with metadata for Lir'

    Mansatmap = get_satmap('aigean_man_20230108_125938.hdf5')
    assert Mansatmap.instrument == 'Manannan', 'get_satmap is not creating satmap object with metadata for Manannan'

    Fandsatmap = get_satmap('aigean_fan_20230108_125938.zip')
    assert Fandsatmap.instrument == 'Lir', 'get_satmap is not creating satmap object with metadata for Fand'



