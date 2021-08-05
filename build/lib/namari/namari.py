"""
    (c) 2021 Rodney Maniego Jr.
    Namari
"""

from secrets import token_hex

from maguro import Maguro
from arkivist import Arkivist


class Namari():
    def __init__(self):
        self.relationships = {}
        self.pairs = {}
    
    def attach(self, old_key, new_key):
        if validate_key(old_key) and validate_key(new_key):
            for uid, keys in self.relationships.items():
                if (old_key in keys) and (new_key not in keys):
                    keys.append(new_key)
                    self.relationships.update({uid: keys})
                    return self
            uid = gen_uid(list(self.relationships.keys()))
            keys = list(set([old_key, new_key]))
            self.relationships.update({uid: keys})
            return self
    
    def detach(self, old_key, new_key):
        if validate_key(old_key) and validate_key(new_key):
            for uid, keys in self.relationships.items():
                if (old_key in keys) and (new_key in keys):
                    keys.remove(new_key)
                    if len(keys) > 0:
                        self.relationships.update({uid: keys})
                    else:
                        self.relationships.remove(uid)
                        self.pairs.pop(uid)
        return self
    
    def set(self, key, value):
        if validate_key(key):
            for uid, keys in self.relationships.items():
                if key in keys:
                    self.pairs.update({uid: value})
                    return self
            uid = gen_uid(list(self.relationships.keys()))
            self.relationships.update({uid: [key]})
            self.pairs.update({uid: value})
        return self
    
    def get(self, key, fallback=None):
        if validate_key(key):
            for uid, keys in self.relationships.items():
                if key in keys:
                    return self.pairs.get(uid, fallback)
        return fallback
    
    def items(self):
        for uid, value in self.pairs.items():
            keys = self.relationships.get(uid, [])
            yield (keys, value)

def validate_key(key):
    return (isinstance(key, str) or isinstance(key, int) or isinstance(key, float))

def gen_uid(uids):
    uid = token_hex(16)
    if uid not in uids:
        return uid
    return gen_uid(uids)