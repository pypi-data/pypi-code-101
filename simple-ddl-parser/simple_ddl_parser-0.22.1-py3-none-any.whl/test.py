from simple_ddl_parser import DDLParser

ddl =  """
 CREATE TABLE mydataset.newtable
 (
   x INT64 OPTIONS(description="An optional INTEGER field"),
 )
 OPTIONS(
   expiration_timestamp=TIMESTAMP "2023-01-01 00:00:00 UTC",
   description="a table that expires in 2023"
 )
"""
result = DDLParser(ddl).run(group_by_type=True)
import pprint

pprint.pprint(result)
