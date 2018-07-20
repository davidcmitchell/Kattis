import sys
def get_alien_num_sys(alien_language):
    alien_language = list(alien_language)
    alien_num_sys = {}
    for i in range(len(alien_language)):
        alien_num_sys[alien_language[i]] = i
    return alien_num_sys

def translate_alien_to_dec(alien_number, alien_num_sys):
    alien_number = list(alien_number)
    dec = 0
    for i in range(len(alien_number)):
        dec += alien_num_sys[alien_number[len(alien_number)-1-i]]*pow(len(alien_num_sys),i)
    return dec

def translate_dec_to_alien(dec_number,alien_num_sys,alien_language):
    alien_number = []
    while dec_number != 0:
        alien_char_pos = dec_number % len(alien_num_sys)
        alien_number.insert(0,alien_language[alien_char_pos])
        dec_number = int(dec_number / len(alien_num_sys))
    return ''.join(alien_number)

nc = int(sys.stdin.readline().rstrip())
for i in range(nc):
    line = sys.stdin.readline().rstrip().split()
    alien_lang1 = line[1]
    alien_lang2 = line[2]
    alsys1 = get_alien_num_sys(alien_lang1)
    alsys2 = get_alien_num_sys(alien_lang2)
    dec = translate_alien_to_dec(line[0],alsys1)
    res = translate_dec_to_alien(dec,alsys2,alien_lang2)
    print("Case #",i+1,": ",res,sep="")
