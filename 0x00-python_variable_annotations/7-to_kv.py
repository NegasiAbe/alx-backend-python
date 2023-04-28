#!/usr/bin/python3

'''Complex types - string and 
int/float to tuple'''

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
