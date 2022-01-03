from typing import Type
from node import Node
import random

class Network:
    def __init__(self, *args, **kwargs):
        self.__inp = []
        self.__out = []
        self.__nodes = []
        self.__conects = []
        self.__inp_size = 1
        self.__out_size = 1
        self.update(kwargs)
        for a in range(self.__inp_size):
            new = Node(permanent=True, deleteable=False)
            self.__nodes.append(new)
            self.__inp.append(new)
        for a in range(self.__out_size):
            new = Node(deleteable = False)
            for b in self.__inp:
                con = new.add_connection(b, 1.0)
                self.__conects.append(con)
            self.__nodes.append(new)
            self.__out.append(new)
        for con in self.__conects:
            con.value = (random.random()*2)-1
    
    def update(self, kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    @property
    def nodes(self):
        return self.__nodes

    @property
    def connections(self):
        return self.__conects
    
    @property
    def inp_size(self):
        return self.__inp_size
    
    @property
    def out_size(self):
        return self.__out_size
    
    @inp_size.setter
    def inp_size(self, value):
        if type(value) != int:
            raise TypeError('not int')
        if value <= 0:
            raise ValueError('must be > 0')
        self.__inp_size = value
    
    @out_size.setter
    def out_size(self, value):
        if type(value) != int:
            raise TypeError('not int')
        if value <= 0:
            raise ValueError('must be > 0')
        self.__out_size = value
    
    def get(self, inp):
        if type(inp) != list:
            raise TypeError('not list')
        if len(inp) != self.__inp_size:
            raise ValueError('len of input does not match inp_size')
        for a in range(self.__inp_size):
            self.__inp[a].value = inp[a]
        for node in self.__nodes:
            node.reset()
        out = []
        for a in range(self.out_size):
            out.append(self.__out[a].value)
        return out
    
    def split_conection(self, conection):
        new_node = conection.front.copy()