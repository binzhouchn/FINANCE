import six
import pprint
# 现在有个字典
conf = {'base':{'good','medium','bad'},'age':'24'}
# conf.age是不行的
定义一个class：
class p:
    def __init__(self, d=None):
        self.__dict__ = d
    def keys(self):
        return self.__dict__.keys()
    def items(self):
        return six.iteritems(self.__dict__)
    def __repr__(self):
        return pprint.pformat(self.__dict__) # 将dict转成字符串
p1 = p(conf)
这个时候就可以p1.base和p1.age
p1这个实例拥有的属性有：
p.__doc__
p.__init__
p.__module__
p.__repr__
p.age * age和base这两个是字典加载进来以后多出来的属性
p.base *
p.items
p.keys
