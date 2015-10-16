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


### debug helper START
def stat():
    print "key variables\n\tdec_address: %d\n\tbin_address: %s\n\tstr_dec: %s\n\tstr_bin: %s" % (dec_address, bin_address, str_dec, str_bnr)
    sleep(1)

stat()
### debug helper END
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

### dec_address add, subtract, and set methods ###
# add
def dec_add(num):
    global dec_address
    dec_address+=num
    all_dec()
# subtract
def dec_sub(num):
    global dec_address
    dec_address-=num
    all_dec()
# set
def dec_set(val):
    global dec_address
    if val >= 0 and val <= 511:
        dec_address = val
        all_dec()
    else:
        print "dec_set() function was passed an invalid value"

### str_dec add subtract methods ###
# add
def str_dec_add(num):
    global str_dec
    str_dec=str_int(int(str_dec)+num)
    all_str_dec()

# subtract
def str_dec_sub(num):
    global str_dec
    str_dec=str_int(int(str_dec)-num)
    all_str_dec()

### str_bnr add subtract methods ###
# add
def str_bnr_add(num):
    global str_bnr
    str_bnr=str_bin(bin(int_bnr(str_bnr)+num))
    all_str_bnr()

# subtract
def str_bnr_sub(num):
    global str_bnr
    str_bnr=str_bin(bin(int_bnr(str_bnr)-num))
    all_str_bnr()


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


dec_add(1)
stat()


################### GUI starts here #############################

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

### ### ### C
# C4-C12 these are 9 SingleDip objects for each of the 9 dipswitch switches
# each one containing DipVal, BinSwitch, and DipNum objects in this order.
# this totals to 27 objects marked D4-D30 in the dipswitch.kv file
class SingleDip(BoxLayout):
    pass

### ### ### ### D
# D4, D7, D10, D13, D16, D19, D22, D25, and D28, a total of 9 DipVal objects.
# each marks the binary digit value of the switch blow it.
class DipVal(Label):
    pass
# D5, D8, D11, D14, D17, D20, D23, D26, and D29, a total of 9 BinSwitch objects.
class BinSwitch(Switch):
    pass
# D6, D9, D12, D15, D18, D21, D24, D27, and D30, a total of 9 DipNum objects.
class DipNum(Label):
    pass





####### main #######
class DipSwitch(App):
    # address holders
    decimal=StringProperty(str_dec)
    binary=StringProperty(str_bnr)

    # called on start
    def build(self):
        self.str_bnr_dip()
        return MainView()

    # updates the address holders
    def refresh(self):
        if str_dec != '000':
            self.decimal=str_dec
        else:
            self.decimal='512'
        self.binary=str_bnr
        self.str_bnr_dip()

    #def out_str_dec(self):
        #if str_dec == '000':
            #return '512'
        #elif dec_address < 512 and dec_address > 0:
            #return str_dec
        #else:
            #return 'error'

######## different button functions for the DecimalView object

    # raises the whole address by one
    def all_up(self):
        if dec_address < 511:
            dec_add(1)
        elif dec_address == 511:
            dec_set(0)
        self.refresh()

    # lowers the whole address by one
    def all_down(self):
        if dec_address > 0:
            dec_sub(1)
        elif dec_address == 0:
            dec_set(511)
        self.refresh()

    ### specific digit changes
    
    # raises the hundreds digit by one
    def hund_up(self):
        if dec_address < 412 and dec_address != 0:
            dec_add(100)
        elif dec_address == 412:
            dec_set(0)
        elif dec_address == 500:
            dec_set(1)
        elif dec_address > 500:
            dec_sub(500)
        elif dec_address == 0:
            dec_set(1)
        else: # what do i do with this?
            dec_set(511)
        self.refresh()

    # raise the tens digit by one
    def ten_up(self):
        tens=int(str_dec[1])
        if dec_address == 90:
            dec_set(1)
        elif dec_address < 500 and dec_address != 0:
            if tens != 9:
                dec_add(10)
            else:
                dec_sub(90)
        elif dec_address >= 500 and dec_address < 502:
            if tens == 0:
                dec_add(10)
            if tens == 1:
                dec_sub(10)
        elif dec_address >= 502 and dec_address < 510:
            dec_set(0)
        elif dec_address == 510 or dec_address == 511:
            dec_sub(10)
        else:
            dec_set(502)
        self.refresh()

    # raise the ones digit by one
    def one_up(self):
        ones=int(str_dec[2])
        if dec_address <= 510 and dec_address > 9:
            if ones != 9:
                dec_add(1)
            else:
                dec_sub(9)
        elif dec_address == 511:
            dec_set(0)
        elif dec_address <= 8 and dec_address != 0:
            dec_add(1)
        elif dec_address == 9:
            dec_set(1)
        else:
            dec_set(510)
        self.refresh()

    # lower the hundreds digit by one
    def hund_down(self):
        if dec_address > 100:
            dec_sub(100)
        elif dec_address == 100:
            dec_set(1)
        elif dec_address < 100 and dec_address >= 12:
            dec_set(0)
        elif dec_address < 12 and dec_address != 0:
            dec_add(500)
        else:
            dec_set(412)
        self.refresh()

    # lower the tens digit by one
    def ten_down(self):
        tens=int(str_dec[1])
        if dec_address == 0:
            dec_set(502)
        elif dec_address >= 502 and dec_address < 510:
            dec_set(0)
        elif dec_address == 500 or dec_address == 501:
            dec_add(10)
        elif dec_address == 511 or dec_address == 510:
            dec_sub(10)
        elif dec_address < 500 and dec_address != 0 and dec_address != 10:
            if tens != 0:
                dec_sub(10)
            else:
                dec_add(90)
        elif dec_address == 10:
            dec_set(90)

        self.refresh()

    # lower the ones digit by one
    def one_down(self):
        ones=int(str_dec[2])
        if dec_address == 0:
            dec_set(511)
        elif dec_address == 510:
            dec_set(0)
        elif dec_address > 1 and dec_address != 510:
            if ones != 0:
                dec_sub(1)
            else:
                dec_add(9)
        elif dec_address == 1:
            dec_set(9)
        self.refresh()


############### BinaryView switch related functions

# a list of 9 True/False values to represent the different active states of the switches
            

    state9=BooleanProperty(False)
    state8=BooleanProperty(False)
    state7=BooleanProperty(False)
    state6=BooleanProperty(False)
    state5=BooleanProperty(False)
    state4=BooleanProperty(False)
    state3=BooleanProperty(False)
    state2=BooleanProperty(False)
    state1=BooleanProperty(False)

    dips=[state9, state8, state7, state6, state5, state4, state3, state2, state1]
    def str_bnr_dip(self):
        for i in range(0,9):
            if str_bnr[i] == '0':
                self.dips[i].set(self,False)
            else:
                self.dips[i].set(self,True)


        

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
print "\nALL DONE!"
