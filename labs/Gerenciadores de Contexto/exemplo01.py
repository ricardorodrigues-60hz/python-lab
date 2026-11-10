from itertools import count
"""
>>> c = count(0)
>>> c
0
>>> c
1
>>> c
2
"""
from os.path import exists

import logging
logger = logging.getLogger(__name__)

class SaveAnother:
    counter = count(0)

    def __init__(self, file: str):
        self.file = file
        self.mode = 'w'
        self.obj = None

    def __enter__(self):
        if exists(self.file):
            file_name = f'{self.file}{next(self.counter)}'
            # file_name = '{}{}'.format(self.file, next(self.counter))
            self.obj = open(file_name, self.mode)
            return self.obj
        self.obj = open(self.file, self.mode)
        return self.obj

    def __exit__(self, type, value, traceback):
        logger.info(f'{type}, {value}, {traceback}')
        self.obj.close()