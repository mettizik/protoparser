class BasicProtoType:
    def __init__(self, fn):
        self.field = fn


class UnknownType(BasicProtoType):
    _typeid = -1
    _typename = 'Unknown'
    _protoVer = 0

    def __init__(self, fn):
        BasicProtoType.__init__(self, fn)
        raise RuntimeError("Unknown type field initializing - possibly non protobuf data")


class Varint(BasicProtoType):
    _typeid = 0
    _typename = 'Varint'

    def __init__(self, fn):
        BasicProtoType.__init__(self, fn)


class Fixed64(BasicProtoType):
    _typeid = 1
    _typename = '64-bit'

    def __init__(self, fn):
        BasicProtoType.__init__(self, fn)


class LengthDelimited(BasicProtoType):
    _typeid = 2
    _typename = 'Length-Delimited'

    def __init__(self, fn):
        BasicProtoType.__init__(self, fn)


class StartGroup(BasicProtoType):
    _typeid = 3
    _typename = 'Start group'

    def __init__(self, fn):
        BasicProtoType.__init__(self, fn)


class EndGroup(BasicProtoType):
    _typeid = 4
    _typename = 'End group'

    def __init__(self, fn):
        BasicProtoType.__init__(self, fn)


class Fixed32(BasicProtoType):
    _typeid = 5
    _typename = '32-bit'

    def __init__(self, fn):
        BasicProtoType.__init__(self, fn)


g_alltypes = [UnknownType, Varint, Fixed32, Fixed64, LengthDelimited, StartGroup, EndGroup]
