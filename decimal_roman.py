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