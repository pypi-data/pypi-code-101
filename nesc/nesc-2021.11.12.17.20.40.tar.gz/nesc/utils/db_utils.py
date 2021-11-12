class DB(object):

    def __init__(self, is_test=True):
        self.is_test = is_test  # 10.212.3.253 通过ip判断是否是测试环境

    def redis(self, ips=None):
        password = None
        if self.is_test:
            ips = "10.211.96.32:7000,10.211.96.32:7001,10.211.96.33:7000,10.211.96.33:7001,10.211.96.34:7000,10.211.96.34:7001".split(
                ',')
            password = "PzGgrUK#eE*U305O"
        elif ips is None:
            ips = "10.210.10.88:7000,10.210.10.88:7001,10.210.10.89:7000,10.210.10.89:7001,10.210.10.90:7000,10.210.10.90:7001".split(
                ',')
            password = "DOwYjq00#YH*0VZg"

        startup_nodes = [dict(zip(['host', 'port'], ip.split(':'))) for ip in ips]

        from rediscluster import RedisCluster
        rc = RedisCluster(
            startup_nodes=startup_nodes,
            decode_responses=True,
            skip_full_coverage_check=True,
            password=password,
        )
        return rc

    def mysql(self):
        pass

    def mongodb(self):
        pass

    def hive(self):
        pass
