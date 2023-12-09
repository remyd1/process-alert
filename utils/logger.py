#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


#logging.basicConfig(level = logging.INFO)
# create a new logger instead of the default root logger
logger    = logging.getLogger('process-alert')

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

# create file handler which logs even warn messages
# info messages are displayed to stdout
logger.setLevel(logging.INFO)
fhw = logging.FileHandler(dir_path+'/../results/process-alert.log')
fhw.setLevel(logging.WARNING)
logger.addHandler(fhw)