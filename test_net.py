#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:28:54 2023

@author: rebeccawhittingham
"""



import pytest

from codeass1 import net
from pathlib import Path
import os





def test_Net_query_isa():
    
      
    with pytest.raises(ValueError) as exc_info:
        net.query_isa('202-01-03', '2023-01-04', 'Lir')
        #assert "Incorrect start date format, should be YYYY-MM-DD" in str(exc_info.value)
        
    with pytest.raises(ValueError) as exc_info:
        net.query_isa('2023-01-03', '2023-01-08', 'Lir')
        assert 'Date range should be 3 days or less.' in str(exc_info.value)
    
    with pytest.raises(ValueError) as exc_info:
        net.query_isa('2023-06-03', '2023-01-03', 'Lir')
        #assert "Start date must be before stop date." in str(exc_info.value)
    
    with pytest.raises(ValueError) as exc_info:
        net.query_isa('2030-01-01', '2030-01-02', 'Lir')
        #assert "The stop date must be today or earlier." in str(exc_info.value)
    
    
    with pytest.raises(ValueError) as exc_info:
        net.query_isa('2023-01-01', '2023-01-03', 'Nonsense Instrument')
        #assert "Invalid instrument, must be Lir, Manannan, Fand or Ecne" in str(exc_info.value)
        

    
    with pytest.raises(TypeError) as exc_info:
        net.query_isa(5,'2023-01-03', 'Lir')
        assert "Start date must be type string." in str(exc_info.value)
    
        
    assert net.query_isa('2023-01-05', '2023-03-07', 'Lir') == type(list), 'The query_isa method should return a list.'        
    
    assert (net.query_isa('2023-01-05', '2023-03-07', 'Lir'))[1] == type(str), 'The query_isa method should return a list of strings.'        

    assert net.query_isa('2023-01-05', '2023-03-07', 'Lir') == type(list), 'The query_isa method should return a list for instrument Lir.'        

    assert net.query_isa('2023-01-05', '2023-03-07', 'Manannan') == type(list), 'The query_isa method should return a list for instrument Manannan'   

    assert net.query_isa('2023-01-05', '2023-03-07', 'Fand') == type(list), 'The query_isa method should return a list for instrument Fand.'   




def test_net_download_isa():
    

    with pytest.raises(TypeError) as exc_info:
        net.download_isa(6)
        assert "Filename must be a string." in str(exc_info.value)

    with pytest.raises(TypeError) as exc_info:
        net.download_isa('aigean_fan_20230109_103220.zip', 6)
        assert "Save directory must be a string or Path object" in str(exc_info.value)
        
    with pytest.raises(ValueError) as exc_info:
        net.download_isa('aigean_fan_20230109_103220.zip', 'Nonsense_Filepath')
        assert "Input save directory does not exist." in str(exc_info.value)
        

    net.download_isa('aigean_fan_20230109_103220.zip')
        
    current_location = os.getcwd()
    local_str_filepath_fname = os.path.join(current_location,'aigean_fan_20230109_103220.zip')
    local_filepath_fname = Path(local_str_filepath_fname)
    assert local_filepath_fname.is_file(), 'Zip file not being downloaded into current directory for Fand'

    net.download_isa('aigean_lir_20230107_123152.asdf')

    local_str_filepath_fname = os.path.join(current_location,'aigean_lir_20230107_123152.asdf')
    local_filepath_fname = Path(local_str_filepath_fname)
    assert local_filepath_fname.is_file(), 'asdf file not being downloaded into current directory for Lir'

    net.download_isa('aigean_man_20230106_125938.hdf5')

    local_str_filepath_fname = os.path.join(current_location,'aigean_man_20230106_125938.hdf5')
    local_filepath_fname = Path(local_str_filepath_fname)
    assert local_filepath_fname.is_file(), 'hdf5 file not being downloaded into current directory for Manannan'

    
    



