from simple_ddl_parser import DDLParser

ddl =  """
DROP TABLE IF EXISTS sample
CREATE TABLE sample
(
     sid BIGINT NOT NULL,
     foo CHAR(5),
     CONSTRAINT sample_key PRIMARY KEY NONCLUSTERED (sid)
)

"""
result = DDLParser(ddl).run(group_by_type=True)
import pprint

pprint.pprint(result)
