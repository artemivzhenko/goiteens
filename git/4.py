from re import match

def which_postcode(s):
    return 'GB' if match(r'^([A-z]){1,2}(\d){1,2} (\d){1,1}([A-z]){2,2}$',s.strip()) else 'SK' if match(r'^(\d){3,3} (\d){2,2}$',s.strip()) else 'Not valid'