def generate_userID(login, password):
    bin_l = ' '.join(format(ord(x), 'b') for x in login).replace(" ", "")
    bin_p = ' '.join(format(ord(x), 'b') for x in password).replace(" ", "")
    
    int_l = int(len([1 for x in bin_l if x == '1']))
    int_p = int(len([1 for x in bin_p if x == '1']))
    
    hex_add = {
        "0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "a":10,
        "b":11,
        "c":12,
        "d":13,
        "e":14,
        "f":15,
    }
    
    hex_l = hex(int(bin_l))
    hex_ls = 0
    for h in hex_l[2:]:
        hex_ls += hex_add[h]
    hex_lss = str(hex(hex_ls))[2:]
    
    hex_p = hex(int(bin_p))
    hex_ps = 0
    for h in hex_p[2:]:
        hex_ps += hex_add[h]
    hex_pss = str(hex(hex_ps))[2:]
    
    user_id = hex_lss + str(int_l) + hex_pss + str(int_p)
    return(user_id)
