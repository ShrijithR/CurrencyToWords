from .Dictionaries import one_nine, ten_teen, twty_nty
import re, logging

logging.basicConfig(level = logging.DEBUG, format = '%(message)s')
logging.disable(logging.DEBUG)

allowed_input = re.compile(r'[^\d.,]')
allowed_dot = re.compile(r'\.')
allowed_decimal_limit = re.compile(r'\.\d{3,}$')
allowed_Start = re.compile(r'^\d')
allowed_End = re.compile(r'\d$')

def CheckInput(amount):
    """Returns True if the input passes through the if conditions"""    
    logging.debug("Passed zero")
    if (
        allowed_input.search(amount) 
        or len(allowed_dot.findall(amount)) > 1 
        or allowed_decimal_limit.search(amount) 
        or not allowed_Start.search(amount)
        or not allowed_End.search(amount)
    ):
        return "Invalid input"
    logging.debug("Passed regex")
    if float(amount) < 0 or float(amount) > 999999.99:
        return "Number not within the limit"
    logging.debug("Passed limit")
    if float(amount) == 0:
        return "Rs. Zero"
    return True

def Str_List(amount):
    """Returns the string format, a list containing the digits, 
    and the length of the number"""
    num_str = ''.join(str(amount).split(','))
    num_list = []
    [num_list.append(int(i)) for i in num_str]
    length = len(num_list)
    return num_str, num_list, length

def return_string(func, a, paise):
    return "Rs. " + func(a) + paise + ' ONLY'

def convert(amount):
    """Returns the converted format of the amount argument """
    num_str = ''.join(str(amount).split(','))
    if CheckInput(num_str) != True:
        return CheckInput(num_str)
    split_list = num_str.split('.')
    amount = int(split_list[0])
    length = Str_List(amount)[2]
    paise = ''
    try:
        if int(split_list[1]) != 0:
            paise = ' '+ split_list[1] +'/100'
    except IndexError:
        pass
    
    if amount == 0:
        return "Rs." + paise + ' ONLY'
    if length < 3:
        return return_string(single_double, amount, paise)
    if length == 3:
        return return_string(hundreds, amount , paise)
    if length == 4 or length == 5:
        return return_string(Thousand, amount, paise)
    if length == 6:
        return return_string(Lakh, amount , paise)

def single_double(amount):
    """Converts the single and double digit numbeRs"""
    num_list, length = Str_List(amount)[1:]
    if amount == 0:
        return
    if length == 1:
        return one_nine[amount]
    if num_list[0] == 1:
        return ten_teen[amount]
    if not num_list[1] == 0:
        return ' '.join((twty_nty[num_list[0]], 
        one_nine[num_list[1]] ))
    
    return twty_nty[num_list[0]]

def hundreds(amount):
    """Converts three digit numbeRs"""
    num_str, num_list, length = Str_List(amount)
    if amount == 0:
        return    
    if length < 3:
        return single_double(amount)
    if single_double(int(''.join(num_str[1:]))):
        return (
            ' '.join((
                one_nine[num_list[0]], 'Hundred', 'and', 
                single_double(int(''.join(num_str[1:])))
            ))
        )
    return (
        ' '.join((
            one_nine[num_list[0]], 'Hundred'
        ))
    )
    
def Thousand(amount):
    """Converts four and five digit numbeRs"""
    num_str, num_list, length = Str_List(amount)
    if amount == 0:
        return    
    if length <= 3:
        return hundreds(amount)
    if length == 4:
        if hundreds(int(''.join(num_str[-3:]))):
            return (
            ' '.join((
            single_double(num_list[0]), 'Thousand', 
            hundreds(int(''.join(num_str[-3:])))
                ))
            )
        return (
            ' '.join((
            single_double(num_list[0]), 'Thousand'
            ))
        )
    if hundreds(int(''.join(num_str[-3:]))):
        return (
        ' '.join((
        single_double(int(''.join(num_str[:2]))), 'Thousand', 
        hundreds(int(''.join(num_str[-3:])))
            ))
        )
    return (
        ' '.join((
        single_double(int(''.join(num_str[:2]))), 'Thousand'
        ))
    )

def Lakh(amount):
    """Converts six digit numbeRs"""
    num_str, num_list, length = Str_List(amount)
    if amount == 0:
        return
    if length <= 5:
        return Thousand(amount)
    if Thousand(int(''.join(num_str[-5:]))):
        return (
        ' '.join((
        single_double(num_list[0]), 'Lakh', 
        Thousand(int(''.join(num_str[-5:])))
            ))
        )
    return (
        ' '.join((
        single_double(num_list[0]), 'Lakh'
        ))
    )
