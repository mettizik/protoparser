from prototypes import g_alltypes


def Type(t):
    for item in g_alltypes:
        if t == item._typeid:
            return item


def CheckInputByte(func):
    def wrapper(byte):
        if byte != (byte & 0xff) or byte < 0:
            raise RuntimeError("Not a byte(0..255) value {}".format(byte))

        return func(byte)

    return wrapper


@CheckInputByte
def GetWireType(byte):
    return byte & 7


@CheckInputByte
def GetFieldNumber(byte):
    return (byte >> 3) & 0x0f


@CheckInputByte
def ParseHeadByte(byte):
    byte = byte & 0x7f
    return GetFieldNumber(byte), GetWireType(byte)


@CheckInputByte
def CreateWireType(byte):
    fn, wt = ParseHeadByte(byte)
    return Type(wt)(fn)


obj = CreateWireType((1 << 3) | 0)
print(obj.field, obj._typeid, obj._typename)
