# Save data to an AWS bucket

from typing import Dict

import aws_lib
import pymongo

def aws_upload(data: Dict):
    database = aws_lib.connect("AKIAYVP4CIPPDU52FK7E", "rfV2rjx6sibrBMcgFu+N6F/+x5EtK24H5zS4StrB")
    database.push(data)
