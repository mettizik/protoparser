from unittest import TestCase

from protoparser import Type, GetWireType, GetFieldNumber, ParseHeadByte
from prototypes import UnknownType, Varint, Fixed32, Fixed64, LengthDelimited, StartGroup, EndGroup


def ExpectThrow(function, exception, tester):
    def Wrapper(arg):
        try:
            function(arg)
            tester.fail()
        except exception:
            pass

    return Wrapper


class TestProtoparser(TestCase):
    def test_Type(self):
        self.assertEqual(Type(-1), UnknownType)
        self.assertEqual(Type(0), Varint)
        self.assertEqual(Type(1), Fixed64)
        self.assertEqual(Type(2), LengthDelimited)
        self.assertEqual(Type(3), StartGroup)
        self.assertEqual(Type(4), EndGroup)
        self.assertEqual(Type(5), Fixed32)

    def CheckFunctionThrowsOnNoneByte(self, func):
        wrapped = ExpectThrow(func, RuntimeError, self)
        wrapped(-1)
        wrapped(-128)
        wrapped(256)
        wrapped(1024)

    def test_GetWireTypeNoneByte(self):
        self.CheckFunctionThrowsOnNoneByte(GetWireType)

    def test_GetFieldNumberNoneByte(self):
        self.CheckFunctionThrowsOnNoneByte(GetFieldNumber)

    def test_ParseHeadByteNoneByte(self):
        self.CheckFunctionThrowsOnNoneByte(ParseHeadByte)

    def test_GetWireType(self):
        self.assertEqual(1, GetWireType(9))
        self.assertEqual(2, GetWireType(10))
        self.assertEqual(3, GetWireType(11))
        self.assertEqual(4, GetWireType(12))
        self.assertEqual(5, GetWireType(13))
        self.assertEqual(6, GetWireType(14))
        self.assertEqual(7, GetWireType(15))

    def test_GetFieldNumber(self):
        for i in range(1, 16):
            self.assertEqual(i, GetFieldNumber(i << 3))

    def test_ParseHeadByte(self):
        self.assertEqual((1, 1), ParseHeadByte((1 << 3) | 1))
        self.assertEqual((1, 2), ParseHeadByte((1 << 3) | 2))
        self.assertEqual((1, 7), ParseHeadByte((1 << 3) | 7))
        self.assertEqual((2, 7), ParseHeadByte((2 << 3) | 7))
        self.assertEqual((15, 7), ParseHeadByte((15 << 3) | 7))
