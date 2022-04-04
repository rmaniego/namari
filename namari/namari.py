"""
    (c) 2021 Rodney Maniego Jr.
    Namari
"""

import hashlib
from arkivist import Arkivist


class Namari():
    def __init__(self, filepath=None, autosave=False):
        self.filepath = _validate_filepath(filepath)
        self.data = Arkivist(self.filepath, autosave=autosave)
    
    def insert(self, elements):
        if type(elements) not in (list, set, tuple):
            elements = [elements]
        for element in elements:
            if _validate_key(element):
                self.data.set(element, [])
        return self
    
    def set(self, parent, child):
        if _validate_key(parent) and _validate_key(child):
            self.data.appendIn(parent, child)
        return self
    
    def attach(self, parent, child, unique=False):
        if _validate_key(parent) and _validate_key(child):
            if parent in self.data:
                if (child not in self.data[parent]) or not unique:
                    self.data.appendIn(parent, child)
        return self
    
    def detach(self, parent, child):
        if _validate_key(parent) and _validate_key(child):
            if parent in self.data:
                self.data.removeIn(parent, child)
        return self
    
    def get(self, parent, fallback=None):
        if _validate_key(parent):
            return self.data.get(parent, fallback)
        return fallback
    
    def findFirst(self, search, fallback=None):
        if _validate_key(search):
            for parent, children in self.data.items():
                if search in children:
                    return parent
        return fallback
    
    def findAll(self, search):
        matches = []
        if _validate_key(search):
            for parent, children in self.data.items():
                if search in children:
                    matches.append(parent)
        return matches
    
    def items(self):
        for parent, children in self.data.items():
            yield (parent, children)
    
    def keys(self):
        return list(self.data.keys())
    
    def values(self):
        return list(self.data.values())
    
    def contains(self, search):
        if _validate_key(search):
            if (search in self.data):
                return True
            for children in self.data.values():
                if search in children:
                    return True
        return False
    
    def count(self):
        return len(self.data)
    
    def is_empty(self):
        return self.data.is_empty()

    def clear(self):
        self.data.reset()
        

def _validate_key(key):
    return type(key) in (str, int, float)

def _validate_filepath(filepath):
    if isinstance(filepath, str):
        if filepath.split(".")[-1] != "json":
            filepath += ".json"
        try:
            with open(filepath, "a+") as temp:
                return filepath
        except:
            pass
    return None