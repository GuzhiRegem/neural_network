class Node:
    def __init__(self, *args, **kwargs):
        self.__value = 0.0
        self.__back = []
        self.__front = []
        self.__permanent = False
        self.__gotvalue = False
        self.__deleteable = True
        self.update(kwargs)
        self.add_connection(None, 1.0)
    
    def update(self, kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    def get_value(self):
        out = 0.0
        for conection in self.__back:
            res = conection.get_value()
            out += res
        return out
    
    def vectorize(self, value):
        if value > 1.0:
            value = 1.0
        if value < -1.0:
            value = -1.0
        return value
    
    @property
    def value(self):
        if self.__gotvalue or self.__permanent:
            return self.vectorize(self.__value)
        self.__value = self.vectorize(self.get_value())
        self.__gotvalue = True
        return self.__value
    
    @value.setter
    def value(self, num):
        if type(num) != float:
            raise TypeError('not float')
        self.__value = num
    
    @property
    def permanent(self):
        return self.__permanent

    @permanent.setter
    def permanent(self, value):
        if type(value) != bool:
            raise TypeError('not bool')
        self.__permanent = value
    
    @property
    def deleteable(self):
        return self.__deleteable

    @deleteable.setter
    def deleteable(self, value):
        if type(value) != bool:
            raise TypeError('not bool')
        self.__deleteable = value
    
    @property
    def front(self):
        return list(self.__front)
    
    @property
    def back(self):
        return list(self.__back)
    
    def add_connection(self, node_o, weight):
        if type(node_o)!= Node:
            raise TypeError('not Node')
        if type(weight) != float:
            raise TypeError('not float')
        new = Connection(back=node_o, front=self, value=weight)
        self.__back.append(new)
        node_o.add_front(new)
        return new
    
    def add_front(self, conection):
        self.__front.append(conection)
    
    def reset(self):
        if not self.__permanent:
            self.__gotvalue = False
    
    def remove_back(self, conection):
        self.__back.remove(conection)
    
    def remove_front(self, conection):
        self.__front.remove(conection)
    
    def __str__(self) -> str:
        return "Node: {} (bias: {})".format(self.__value, self.__bias)

class Connection:
    def __init__(self, *args, **kwargs):
        self.__value = 0.0
        self.__back = None
        self.__front = None
        self.update(kwargs)
    
    def update(self, kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    @property
    def value(self):
        return self.__value

    @property
    def back(self):
        return self.__back

    @property
    def front(self):
        return self.__front
    
    @value.setter
    def value(self, num):
        if type(num) != float:
            raise TypeError('not float')
        self.__value = num
    
    @back.setter
    def back(self, value):
        if type(value) not in [Node, type(None)]:
            raise TypeError('not Node')
        self.__back = value
    
    @front.setter
    def front(self, value):
        if type(value) != Node:
            raise TypeError('not Node')
        self.__front = value
    
    def get_value(self):
        if self.__back == None:
            return 1.0 * self.__value
        return self.__back.value * self.__value
    
    def __str__(self) -> str:
        return "Connection: {} -- {} --> {}".format(self.back.value, self.value, self.front.value)
    
