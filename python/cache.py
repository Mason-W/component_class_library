import datetime
import pprint
import random

class MyCache(object):
    def __init__(self):
        self.cache = {}
        self.max_cache_size = 100

    
    def __contains__(self, key):
        
        # 判断键是否在缓存中
        return key in self.cache

    
    def update(self, key, value):

        # 更新缓存字典，选择性删除最早的条目
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_oldest()
        self.cache[key] = {
            'date_accessed': datetime.datetime.now(),
            'value': value
        }


    def remove_oldest(self):

        # 删除最早访问时间的输入数据
        oldest_entry = None
        for key in self.cache:
            if not oldest_entry:
                oldest_entry = key
            elif self.cache[key]['date_accessed'] < self.cache[oldest_entry]['date_access']:
                oldest_entry = key
        self.cache.pop(oldest_entry)

    
    @property
    def size(self):
        return len(self.cache)
