class UnknownType:
    _typeid = -1
    _typename = 'Unknown'
    _protoVer = 0


class Varint:
    _typeid = 0
    _typename = 'Varint'


class Fixed64:
    _typeid = 1
    _typename = '64-bit'


class LengthDelimited:
    _typeid = 2
    _typename = 'Length-Delimited'


class StartGroup:
    _typeid = 3
    _typename = 'Start group'


class EndGroup:
    _typeid = 4
    _typename = 'End group'


class Fixed32:
    _typeid = 5
    _typename = '32-bit'


g_alltypes = [UnknownType, Varint, Fixed32, Fixed64, LengthDelimited, StartGroup, EndGroup]
