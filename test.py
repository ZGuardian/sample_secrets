# Save data to an AWS bucket

from typing import Dict

import aws_lib
import pymongo

def aws_upload(data: Dict):
    database = aws_lib.connect("AKIAYVP4CIPPCQW3DJOY", "l/QPPts6NCYV6zWngCdExwRWtWQFrZNpO2Z62t2f")
    database.push(data)
