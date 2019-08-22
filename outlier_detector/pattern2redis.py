import redis

class RedisOp():

    def __init__(self):
        self.__pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        self.__r = redis.Redis(connection_pool=self.__pool)

    def setHashRedis(self, user_id, pattern_dict):
        assert isinstance(user_id, str) and isinstance(pattern_dict, dict)
        # 批量增加
        # r.hmset("hash2", {"k2": "v2", "k3": "v3"})
        self.__r.hmset(user_id, pattern_dict)
        self.__r.connection_pool.disconnect()
        print('redis set finish!')
        return 'redis set finish!'

    def getHashRedis(self, user_id):
        assert isinstance(user_id, str)
        pattern_dict = self.__r.hgetall(user_id)
        self.__r.connection_pool.disconnect()
        return pattern_dict

    def delHashRedis(self, user_id, pattern_list):
        assert isinstance(user_id, str) and isinstance(pattern_list, list)
        for pattern in pattern_list:
            self.__r.hdel(user_id, pattern)
        self.__r.connection_pool.disconnect()
        print('redis del finish!')
        return 'redis del finish!'

if __name__=='__main__':
    A = RedisOp()
    A.setHashRedis('yjs', {'【事件编号】(.+?)-蓝': 'blue', '【事件编号】(.+?)-红': 'red'})
    print(A.getHashRedis('yjs'))

