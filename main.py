__version__ = '0.1'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.switch import Switch
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
#from kivy.uix.
#from kivy.uix.

from time import sleep
print "All modules loaded"
sleep(1)


dec_address=0
bin_address='0b0'
str_dec='000'
str_bnr='000000000'

def stat():
    print "key variables\n\tdec_address: %d\n\tbin_address: %s\n\tstr_dec: %s\n\tstr_bin: %s" % (dec_address, bin_address, str_dec, str_bnr)
    sleep(1)

stat()

# to turn integers to binary use python's built in bin(int) function

# to turn str_dec to integer use python's built in int(string) function

# binary to integer
def int_bin(binary):
    return int(binary, 2)

# integer to 3 digit string
def str_int(integer):
    hund=integer/100
    integer=integer%100
    tens=integer/10
    ones=integer%10
    return str(hund)+str(tens)+str(ones)

# binary to 9 digit string
def str_bin(binary):
    parts=['0','0','0','0','0','0','0','0','0']
    out=str(binary)[2:]
    for i in range(1, len(out)+1):
        parts[i*-1]=out[i*-1]
    out=''
    for i in parts:
        out+=i
    return out

# 9 digit string to integer
def int_bnr(bnr):
    vals=[256, 128, 64, 32, 16, 8, 4, 2, 1]
    out=0
    for i in range(0,9):
        out+=vals[i]*int(bnr[i])
    return out




# set str_bnr, dec_address, and bin_address by the value of str_dec
def all_str_dec():
    global dec_address
    global bin_address
    global str_bnr
    dec_address=int(str_dec)
    bin_address=bin(dec_address)
    str_bnr=str_bin(bin(dec_address))

# set str_bnr, dec_address, and str_dec by the value of bin_address
def all_bin():
    global dec_address
    global str_dec
    global str_bnr
    dec_address=int_bin(bin_address)
    str_dec=str_int(dec_address)
    str_bnr=str_bin(bin(dec_address))

# set str_bnr, bin_address, and str_dec by the value of dec_address
def all_dec():
    global bin_address
    global str_dec
    global str_bnr
    bin_address=bin(dec_address)
    str_dec=str_int(dec_address)
    str_bnr=str_bin(bin(dec_address))

# set str_dec, bin_address, and dec_address by the value of str_bnr
def all_str_bnr():
    global dec_address
    global bin_address
    global str_dec
    dec_address=int_bnr(str_bnr)
    bin_address=bin(dec_address)
    str_dec=str_int(dec_address)

### dec_address add subtract methods ###
# add
def dec_add(num):
    global dec_address
    dec_address+=num
# subtract
def dec_sub(num):
    global dec_address
    dec_address-=num

### str_dec add subtract methods ###
# add
def str_dec_add(num):
    global str_dec
    str_dec=str_int(int(str_dec)+num)

# subtract
def str_dec_sub(num):
    global str_dec
    str_dec=str_int(int(str_dec)-num)

### str_bnr add subtract methods ###
# add
def str_bnr_add(num):
    global str_bnr
    str_bnr=str_bin(bin(int_bnr(str_bnr)+num))

# subtract
def str_bnr_sub(num):
    global str_bnr
    str_bnr=str_bin(bin(int_bnr(str_bnr)-num))


### str_bnr individual digit 0/1 toggle ###
def zero_one(char):
    if char=='0':
        return '1'
    elif char=='1':
        return '0'
    else:
        return None

def togg_str_bnr(index):
    global str_bnr
    if index == 1:
        before=str_bnr[:-1]
        digit=str_bnr[-1]
        after=''
    elif index == 9:
        before = ''
        digit = str_bnr[1]
        after = str_bnr[1:]
    else:
        before=str_bnr[:index*-1]
        digit=str_bnr[index*-1]
        after=str_bnr[(index*-1)+1:]
    digit=zero_one(digit)
    str_bnr=before+digit+after

### A
# A1 the object containing the main view of the program
class MainView(BoxLayout):
    pass

### ### B
# B1 top area of the main view. used to deal with decimal address aspects
class DecimalView(BoxLayout):
    pass

### ### ### C
# C1 kivy button object in dipswitch.kv

# C2 middle area of the DecimalView object. used to display varioud buttons and decimal address text
class MidPanel(BoxLayout):
    pass

### ### ### ### D
# D1 top area of the MidPanel object. contains a few buttons in dipswitch.kv
class UpButtons(BoxLayout):
    pass

# D2 center area of the MidPanel object. contains a kivy label object in dipswitch.kv

# D3 bottom area of the MidPanel object. contains a few buttons in dipswitch.kv
class DownButtons(BoxLayout):
    pass

### ### ### C
# C3 kivy button object in dipswitch.kv

### ### B
# B2 bottom area of the main view. used to deal with binary address.
class BinaryView(BoxLayout):
    pass



####### main #######
class DipSwitch(App):
    pass

if __name__ == "__main__":
    DipSwitch().run()

#print "dec_add(1)"
#dec_add(1)
#
#stat()
#print "all_dec()"
#all_dec()
#stat()
#print "bin_address=bin(2)"
#bin_address=bin(2)
#stat()
#print "all_bin()"
#all_bin()
#stat()
#print "str_dec=str_int(3)"
#str_dec=str_int(3)
#stat()
#print "all_str_dec()"
#all_str_dec()
#stat()
#
#print "togg_str_bnr(1)"
#togg_str_bnr(1)
#stat()
#print "togg_str_bnr(2)"
#togg_str_bnr(2)
#stat()
#print "togg_str_bnr(3)"
#togg_str_bnr(3)
#stat()
#
#print "all_str_bnr()"
#all_str_bnr()
#stat()
#
#print "str_bnr_add(1)"
#str_bnr_add(1)
#stat()
#
#print "all_str_bnr()"
#all_str_bnr()
#stat()
#
print "\n\n\n\n\n\n\nALL DONE!"
