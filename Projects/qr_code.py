# ******************************************************
#                  QR Code generator project
#                  Project by : MAMATA SHEE
#
# ******************************************************


import pyqrcode
import png


def qrcode():
    q=pyqrcode.create(input("Enter any text to generate QR code : "))
    q.png('qrcode.png',scale=6)
    print("QR code generated :) ")

if __name__ == '__main__':
    qrcode()



# ------------------------------------------------------------
#
# --> For this we need to install to module 'pyqrcode' and 'pypng'
# --> After installing these import 'pyqrcode' and 'png'
#
#  ------------------------------------------------------------