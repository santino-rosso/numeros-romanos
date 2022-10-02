import unittest


def convert_decimal_to_roman(decimal_number):
    
    rest= decimal_number % 10
    mult_10 = decimal_number // 10
    result_60= ''
    result_10= ''
    result_3= ''
    result_4= ''
    result_5=''
    result_i='' 
    result_9=''
   
    if mult_10 > 0 and mult_10 < 4:
        for digit in range(mult_10):
            result_10 += 'X'
    if mult_10 == 4:
        for digit in range(1):
            result_10 = 'XL'
    if mult_10 >= 5 and mult_10 < 9:
        for digit in range(1):
            result_10 = 'L'
        for digit in range(mult_10 - 5):
            result_60 += 'X'
    if mult_10 == 9:
        for digit in range(1):
            result_10 = 'XC'
    if mult_10 >= 10:
        for digit in range(1):
            result_10 = 'C'
    if rest < 4:
        for digit in range(rest):
            result_3 += 'I'
    if rest == 4:
        for digit in range(1):
            result_4 = 'IV'
    if rest >= 5 and rest < 9: 
        for digit in range(1):
            result_5 = 'V'
        for digit in range(rest - 5):
            result_i += 'I'
    if rest == 9:
        for digit in range(1):
            result_9 = 'IX'
   
    result = result_10 + result_60 + result_3 + result_5 + result_i + result_4 + result_9 
    return result


class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        roman_number = convert_decimal_to_roman(1)
        self.assertEqual(roman_number, 'I')

    def test_2(self):
        roman_number = convert_decimal_to_roman(2)
        self.assertEqual(roman_number, 'II')
    
    def test_3(self):
        roman_number = convert_decimal_to_roman(3)
        self.assertEqual(roman_number, 'III')

    def test_4(self):
        roman_number = convert_decimal_to_roman(4)
        self.assertEqual(roman_number, 'IV')

    def test_5(self):
        roman_number = convert_decimal_to_roman(5)
        self.assertEqual(roman_number, 'V')
    
    def test_8(self):
        roman_number = convert_decimal_to_roman(8)
        self.assertEqual(roman_number, 'VIII')
    
    def test_9(self):
        roman_number = convert_decimal_to_roman(9)
        self.assertEqual(roman_number, 'IX')
   
    def test_10(self):
        roman_number = convert_decimal_to_roman(10)
        self.assertEqual(roman_number, 'X')

    def test_11(self):
        roman_number = convert_decimal_to_roman(11)
        self.assertEqual(roman_number, 'XI')

    def test_12(self):
        roman_number = convert_decimal_to_roman(12)
        self.assertEqual(roman_number, 'XII')
    
    def test_14(self):
        roman_number = convert_decimal_to_roman(14)
        self.assertEqual(roman_number, 'XIV')

    def test_15(self):
        roman_number = convert_decimal_to_roman(15)
        self.assertEqual(roman_number, 'XV')

    def test_17(self):
        roman_number = convert_decimal_to_roman(17)
        self.assertEqual(roman_number, 'XVII')

    def test_19(self):
        roman_number = convert_decimal_to_roman(19)
        self.assertEqual(roman_number, 'XIX')

    def test_20(self):
        roman_number = convert_decimal_to_roman(20)
        self.assertEqual(roman_number, 'XX')
    
    def test_23(self):
        roman_number = convert_decimal_to_roman(23)
        self.assertEqual(roman_number, 'XXIII')

    def test_24(self):
        roman_number = convert_decimal_to_roman(24)
        self.assertEqual(roman_number, 'XXIV')
    
    def test_25(self):
       roman_number = convert_decimal_to_roman(25)
       self.assertEqual(roman_number, 'XXV')

    def test_26(self):
       roman_number = convert_decimal_to_roman(26)
       self.assertEqual(roman_number, 'XXVI')

    def test_29(self):
        roman_number = convert_decimal_to_roman(29)
        self.assertEqual(roman_number, 'XXIX')
    
    def test_30(self):
        roman_number = convert_decimal_to_roman(30)
        self.assertEqual(roman_number, 'XXX')  
     
    def test_32(self):
        roman_number = convert_decimal_to_roman(32)
        self.assertEqual(roman_number, 'XXXII')  
    
    def test_34(self):
        roman_number = convert_decimal_to_roman(34)
        self.assertEqual(roman_number, 'XXXIV')

    def test_35(self):
        roman_number = convert_decimal_to_roman(35)
        self.assertEqual(roman_number, 'XXXV')    

    def test_37(self):
        roman_number = convert_decimal_to_roman(37)
        self.assertEqual(roman_number, 'XXXVII')  
    
    def test_39(self):
        roman_number = convert_decimal_to_roman(39)
        self.assertEqual(roman_number, 'XXXIX')

    def test_40(self):
        roman_number = convert_decimal_to_roman(40)
        self.assertEqual(roman_number, 'XL')  
    
    def test_42(self):
        roman_number = convert_decimal_to_roman(42)
        self.assertEqual(roman_number, 'XLII') 
    
    def test_44(self):
        roman_number = convert_decimal_to_roman(44)
        self.assertEqual(roman_number, 'XLIV')

    def test_45(self):
        roman_number = convert_decimal_to_roman(45)
        self.assertEqual(roman_number, 'XLV')

    def test_47(self):
        roman_number = convert_decimal_to_roman(47)
        self.assertEqual(roman_number, 'XLVII')

    def test_49(self):
        roman_number = convert_decimal_to_roman(49)
        self.assertEqual(roman_number, 'XLIX')

    def test_50(self):
        roman_number = convert_decimal_to_roman(50)
        self.assertEqual(roman_number, 'L')

    def test_52(self):
        roman_number = convert_decimal_to_roman(52)
        self.assertEqual(roman_number, 'LII')
    
    def test_54(self):
        roman_number = convert_decimal_to_roman(54)
        self.assertEqual(roman_number, 'LIV')

    def test_55(self):
        roman_number = convert_decimal_to_roman(55)
        self.assertEqual(roman_number, 'LV')
    
    def test_58(self):
        roman_number = convert_decimal_to_roman(58)
        self.assertEqual(roman_number, 'LVIII')
    
    def test_59(self):
        roman_number = convert_decimal_to_roman(59)
        self.assertEqual(roman_number, 'LIX')
    
    def test_60(self):
        roman_number = convert_decimal_to_roman(60)
        self.assertEqual(roman_number, 'LX')

    def test_63(self):
        roman_number = convert_decimal_to_roman(63)
        self.assertEqual(roman_number, 'LXIII')

    def test_64(self):
        roman_number = convert_decimal_to_roman(64)
        self.assertEqual(roman_number, 'LXIV')

    def test_66(self):
        roman_number = convert_decimal_to_roman(66)
        self.assertEqual(roman_number, 'LXVI')
    
    def test_69(self):
        roman_number = convert_decimal_to_roman(69)
        self.assertEqual(roman_number, 'LXIX')
    
    def test_70(self):
        roman_number = convert_decimal_to_roman(70)
        self.assertEqual(roman_number, 'LXX')

    def test_71(self):
        roman_number = convert_decimal_to_roman(71)
        self.assertEqual(roman_number, 'LXXI')
    
    def test_74(self):
        roman_number = convert_decimal_to_roman(74)
        self.assertEqual(roman_number, 'LXXIV')

    def test_75(self):
        roman_number = convert_decimal_to_roman(75)
        self.assertEqual(roman_number, 'LXXV')

    def test_78(self):
        roman_number = convert_decimal_to_roman(78)
        self.assertEqual(roman_number, 'LXXVIII')

    def test_79(self):
        roman_number = convert_decimal_to_roman(79)
        self.assertEqual(roman_number, 'LXXIX')

    def test_80(self):
        roman_number = convert_decimal_to_roman(80)
        self.assertEqual(roman_number, 'LXXX')

    def test_83(self):
        roman_number = convert_decimal_to_roman(83)
        self.assertEqual(roman_number, 'LXXXIII')
    
    def test_84(self):
        roman_number = convert_decimal_to_roman(84)
        self.assertEqual(roman_number, 'LXXXIV')

    def test_85(self):
        roman_number = convert_decimal_to_roman(85)
        self.assertEqual(roman_number, 'LXXXV')

    def test_87(self):
        roman_number = convert_decimal_to_roman(87)
        self.assertEqual(roman_number, 'LXXXVII')

    def test_89(self):
        roman_number = convert_decimal_to_roman(89)
        self.assertEqual(roman_number, 'LXXXIX')
    
    def test_90(self):
        roman_number = convert_decimal_to_roman(90)
        self.assertEqual(roman_number, 'XC')

    def test_92(self):
        roman_number = convert_decimal_to_roman(92)
        self.assertEqual(roman_number, 'XCII')
    
    def test_94(self):
        roman_number = convert_decimal_to_roman(94)
        self.assertEqual(roman_number, 'XCIV')

    def test_95(self):
        roman_number = convert_decimal_to_roman(95)
        self.assertEqual(roman_number, 'XCV')

    def test_96(self):
        roman_number = convert_decimal_to_roman(96)
        self.assertEqual(roman_number, 'XCVI')

    def test_99(self):
        roman_number = convert_decimal_to_roman(99)
        self.assertEqual(roman_number, 'XCIX')
    
    def test_100(self):
        roman_number = convert_decimal_to_roman(100)
        self.assertEqual(roman_number, 'C')


if __name__ == '__main__':
    unittest.main()