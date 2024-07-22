import sys

iccid = input ("Enter ICCID: ")
print (len(iccid))
mcc = '250' # MTS MCC. change to another one
mnc = '01' # MTS MNC. change to another one
msin = iccid[9:-1:]
print (mcc+mnc+msin)
