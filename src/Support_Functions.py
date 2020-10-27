from .Dictionaries import one_nine, ten_teen, twty_nty

def Str_List(amount):
    """Returns the string format, a list containing the digits, 
    and the length of the number"""
    num_str = str(amount)
    num_list = []
    [num_list.append(int(i)) for i in num_str]
    length = len(num_list)
    return num_str, num_list, length

def convert(amount):
    """Returns the converted format of the amount argument """
    split_list = str(amount).split('.')
    amount = int(split_list[0])
    paise = ''
    try:
        if int(split_list[1]) != 0:
            paise = ' '+ split_list[1] +'/100'
    except IndexError:
        pass

    length = Str_List(amount)[2]

    if length < 3:
        return single_double(amount) + paise + ' Only'
    if length == 3:
        return hundreds(amount) + paise + ' Only'
    if length == 4 or length == 5:
        return Thousand(amount) + paise + ' Only'
    if length == 6:
        return Lakh(amount) + paise + ' Only'

def single_double(amount):
    """Converts the single and double digit numbers"""
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
    """Converts three digit numbers"""
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
    """Converts four and five digit numbers"""
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
    """Converts six digit numbers"""
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