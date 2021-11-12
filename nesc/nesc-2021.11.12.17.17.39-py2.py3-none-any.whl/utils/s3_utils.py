import os
from pathlib import Path


if not Path('s3cmd-2.2.0').exists():
    is_test = """
    [default]
    access_key = easyaiminio
    secret_key = easyaiminio
    host_base = 10.1.42.176:32000
    host_bucket = 10.1.42.176:32000/%(dlonline)
    use_https = False
    """
    is_product = """
    [default]
    access_key = easyaiminio
    secret_key = easyaiminio
    host_base = 10.210.10.97:32000
    host_bucket = 10.210.10.97:32000/%(dlonline)
    use_https = False
    """

    cmd = f"""
    cd ~
    && hdfs dfs -get /user/bdms_yuanjie/tools/s3cmd-2.2.0.tar.gz 
    && tar -zxvf s3cmd-2.2.0.tar.gz
    && echo {is_product} > ~/.s3cfg
    """.replace('\n', '').strip()
    os.system(cmd)

# ./s3cmd-2.2.0/s3cmd get 's3://dlonline/



