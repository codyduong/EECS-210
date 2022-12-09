"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-12-8
Lab: Assignment 8
Purpose: Shared Types
"""
from typing import Dict, List, TypeAlias

# key is vertex name
# value is vertex neighbors
Graph: TypeAlias = Dict[str, List[str]]
