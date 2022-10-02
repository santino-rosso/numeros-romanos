import unittest


def convert_roman_to_decimal(roman_number):
    
    dic_roman = {"I":1, "V":5, "X":10, "L":50, "C":100}
    num_decimal = 0
    
    for digit in range(len(roman_number)):
        num_decimal += dic_roman[roman_number[digit]]
        if  digit > 0 and dic_roman[roman_number[digit]] > dic_roman[roman_number[digit - 1]]:
            num_decimal -=  2*dic_roman[roman_number[digit - 1]]    
    
    return num_decimal


class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        decimal_number = convert_roman_to_decimal("I")
        self.assertEqual(decimal_number, 1)
    
    def test_II(self):
        decimal_number = convert_roman_to_decimal("II")
        self.assertEqual(decimal_number, 2)
    
    def test_III(self):
        decimal_number = convert_roman_to_decimal("III")
        self.assertEqual(decimal_number, 3)

    def test_IV(self):
        decimal_number = convert_roman_to_decimal("IV")
        self.assertEqual(decimal_number, 4)
    
    def test_V(self):
        decimal_number = convert_roman_to_decimal("V")
        self.assertEqual(decimal_number, 5)

    def test_VI(self):
        decimal_number = convert_roman_to_decimal("VI")
        self.assertEqual(decimal_number, 6)

    def test_VII(self):
        decimal_number = convert_roman_to_decimal("VII")
        self.assertEqual(decimal_number, 7)

    def test_VIII(self):
        decimal_number = convert_roman_to_decimal("VIII")
        self.assertEqual(decimal_number, 8)

    def test_IX(self):
        decimal_number = convert_roman_to_decimal("IX")
        self.assertEqual(decimal_number, 9)

    def test_X(self):
        decimal_number = convert_roman_to_decimal("X")
        self.assertEqual(decimal_number, 10)

    def test_XI(self):
        decimal_number = convert_roman_to_decimal("XI")
        self.assertEqual(decimal_number, 11)   

    def test_XIV(self):
        decimal_number = convert_roman_to_decimal("XIV")
        self.assertEqual(decimal_number, 14)  

    def test_XV(self):
        decimal_number = convert_roman_to_decimal("XV")
        self.assertEqual(decimal_number, 15)  


    def test_XVII(self):
        decimal_number = convert_roman_to_decimal("XVII")
        self.assertEqual(decimal_number, 17) 

    def test_XIX(self):
        decimal_number = convert_roman_to_decimal("XIX")
        self.assertEqual(decimal_number, 19) 

    def test_XX(self):
        decimal_number = convert_roman_to_decimal("XX")
        self.assertEqual(decimal_number, 20)
    
    def test_XXII(self):
        decimal_number = convert_roman_to_decimal("XXII")
        self.assertEqual(decimal_number, 22) 

    def test_XXV(self):
        decimal_number = convert_roman_to_decimal("XXV")
        self.assertEqual(decimal_number, 25)

    def test_XXVII(self):
        decimal_number = convert_roman_to_decimal("XXVII")
        self.assertEqual(decimal_number, 27)  

    def test_XXIX(self):
        decimal_number = convert_roman_to_decimal("XXIX")
        self.assertEqual(decimal_number, 29) 

    def test_XXX(self):
        decimal_number = convert_roman_to_decimal("XXX")
        self.assertEqual(decimal_number, 30)

    def test_XXXI(self):
        decimal_number = convert_roman_to_decimal("XXXI")
        self.assertEqual(decimal_number, 31) 

    def test_XXXIV(self):
        decimal_number = convert_roman_to_decimal("XXXIV")
        self.assertEqual(decimal_number, 34) 

    def test_XXXV(self):
        decimal_number = convert_roman_to_decimal("XXXV")
        self.assertEqual(decimal_number, 35) 

    def test_XXXVII(self):
        decimal_number = convert_roman_to_decimal("XXXVII")
        self.assertEqual(decimal_number, 37) 

    def test_XXXIX(self):
        decimal_number = convert_roman_to_decimal("XXXIX")
        self.assertEqual(decimal_number, 39) 

    def test_XL(self):
        decimal_number = convert_roman_to_decimal("XL")
        self.assertEqual(decimal_number, 40)

    def test_XLI(self):
        decimal_number = convert_roman_to_decimal("XLI")
        self.assertEqual(decimal_number, 41)

    def test_XLIV(self):
        decimal_number = convert_roman_to_decimal("XLIV")
        self.assertEqual(decimal_number, 44)

    def test_XLV(self):
        decimal_number = convert_roman_to_decimal("XLV")
        self.assertEqual(decimal_number, 45)

    def test_XLVII(self):
        decimal_number = convert_roman_to_decimal("XLVII")
        self.assertEqual(decimal_number, 47)

    def test_XLIX(self):
        decimal_number = convert_roman_to_decimal("XLIX")
        self.assertEqual(decimal_number, 49)

    def test_L(self):
        decimal_number = convert_roman_to_decimal("L")
        self.assertEqual(decimal_number, 50)

    def test_LI(self):
        decimal_number = convert_roman_to_decimal("LI")
        self.assertEqual(decimal_number, 51)

    def test_LIV(self):
        decimal_number = convert_roman_to_decimal("LIV")
        self.assertEqual(decimal_number, 54)

    def test_LV(self):
        decimal_number = convert_roman_to_decimal("LV")
        self.assertEqual(decimal_number, 55)

    def test_LVII(self):
        decimal_number = convert_roman_to_decimal("LVII")
        self.assertEqual(decimal_number, 57)

    def test_LIX(self):
        decimal_number = convert_roman_to_decimal("LIX")
        self.assertEqual(decimal_number, 59)

    def test_LX(self):
        decimal_number = convert_roman_to_decimal("LX")
        self.assertEqual(decimal_number, 60)

    def test_LXI(self):
        decimal_number = convert_roman_to_decimal("LXI")
        self.assertEqual(decimal_number, 61)

    def test_LXIV(self):
        decimal_number = convert_roman_to_decimal("LXIV")
        self.assertEqual(decimal_number, 64)

    def test_LXV(self):
        decimal_number = convert_roman_to_decimal("LXV")
        self.assertEqual(decimal_number, 65)

    def test_LXVI(self):
        decimal_number = convert_roman_to_decimal("LXVI")
        self.assertEqual(decimal_number, 66)

    def test_LXIX(self):
        decimal_number = convert_roman_to_decimal("LXIX")
        self.assertEqual(decimal_number, 69)

    def test_LXX(self):
        decimal_number = convert_roman_to_decimal("LXX")
        self.assertEqual(decimal_number, 70)

    def test_LXXI(self):
        decimal_number = convert_roman_to_decimal('LXXI')
        self.assertEqual(decimal_number, 71)
    
    def test_LXXIV(self):
        decimal_number = convert_roman_to_decimal('LXXIV')
        self.assertEqual(decimal_number, 74)

    def test_LXXV(self):
        decimal_number = convert_roman_to_decimal('LXXV')
        self.assertEqual(decimal_number, 75)

    def test_LXXVIII(self):
        decimal_number = convert_roman_to_decimal('LXXVIII')
        self.assertEqual(decimal_number, 78)

    def test_LXXIX(self):
        decimal_number = convert_roman_to_decimal('LXXIX')
        self.assertEqual(decimal_number, 79)

    def test_LXXX(self):
        decimal_number = convert_roman_to_decimal('LXXX')
        self.assertEqual(decimal_number, 80)

    def test_LXXXIII(self):
        decimal_number = convert_roman_to_decimal('LXXXIII')
        self.assertEqual(decimal_number, 83)
    
    def test_LXXXIV(self):
        decimal_number = convert_roman_to_decimal('LXXXIV')
        self.assertEqual(decimal_number, 84)

    def test_LXXXV(self):
        decimal_number = convert_roman_to_decimal('LXXXV')
        self.assertEqual(decimal_number, 85)

    def test_LXXXVII(self):
        decimal_number = convert_roman_to_decimal('LXXXVII')
        self.assertEqual(decimal_number, 87)

    def test_LXXXIX(self):
        decimal_number = convert_roman_to_decimal('LXXXIX')
        self.assertEqual(decimal_number, 89)
    
    def test_XC(self):
        decimal_number = convert_roman_to_decimal('XC')
        self.assertEqual(decimal_number, 90)

    def test_XCII(self):
        decimal_number = convert_roman_to_decimal('XCII')
        self.assertEqual(decimal_number, 92)
    
    def test_XCIV(self):
        decimal_number = convert_roman_to_decimal('XCIV')
        self.assertEqual(decimal_number, 94)

    def test_XCV(self):
        decimal_number = convert_roman_to_decimal('XCV')
        self.assertEqual(decimal_number, 95)

    def test_XCVI(self):
        decimal_number = convert_roman_to_decimal('XCVI')
        self.assertEqual(decimal_number, 96)

    def test_XCIX(self):
        decimal_number = convert_roman_to_decimal('XCIX')
        self.assertEqual(decimal_number, 99)
    
    def test_C(self):
        decimal_number = convert_roman_to_decimal("C")
        self.assertEqual(decimal_number, 100)

if __name__ == '__main__':
    unittest.main()



