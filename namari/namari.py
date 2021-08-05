"""
    (c) 2021 Rodney Maniego Jr.
    Namari
"""

from secrets import token_hex
from arkivist import Arkivist


class Namari():
    def __init__(self, filepath=""):
        self.filepath = ""
        if isinstance(filepath, str):
            self.filepath = filepath
        self.dataset = Arkivist(self.filepath)
        self.relationships = self.dataset.get("relationships", {})
        self.pairs = self.dataset.get("pairs", {})
    
    def attach(self, old_key, new_key):
        if validate_key(old_key) and validate_key(new_key):
            found = False
            for uid, keys in self.relationships.items():
                if old_key in keys:
                    found = True
                    print(keys, old_key)
                    if new_key not in keys:
                        keys.append(new_key)
                        self.relationships.update({uid: keys})
            if not found:
                uid = gen_uid(list(self.relationships.keys()))
                keys = list(set([old_key, new_key]))
                self.relationships.update({uid: keys})
            self.dataset.set("relationships", self.relationships)
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
                    self.dataset.set("relationships", self.relationships)
                    self.dataset.set("pairs", self.pairs)
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
            self.dataset.set("relationships", self.relationships)
            self.dataset.set("pairs", self.pairs)
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
    
    def keys(self):
        return list(self.relationships.values())
    
    def values(self):
        return list(self.pairs.values())
    
    def contains(self, keyword):
        if validate_key(keyword):
            for keys in self.relationships.values():
                if keyword in keys:
                    return True
        return False
    
    def count(self):
        return len(self.pairs)
    
    def is_empty(self):
        return (len(self.pairs) == 0)

    def clear(self):
        self.dataset.clear()
        self.relationships = {}
        self.pairs = {}
        

def validate_key(key):
    return (isinstance(key, str) or isinstance(key, int) or isinstance(key, float))

def gen_uid(uids):
    uid = token_hex(16)
    if uid not in uids:
        return uid
    return gen_uid(uids)