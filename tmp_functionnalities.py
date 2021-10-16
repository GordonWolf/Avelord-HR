#!/usr/bin/env python

def simple_code_generator(code_lenght:int) -> int:
    from random import randint

    low_range = 10**(code_lenght-1)
    high_range = (10**code_lenght)-1
    return randint(low_range, high_range)

def qrcode_generator(code:int):
    import qrcode

    qr = qrcode.QRCode(version=1, box_size=25, border=1)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode.png')

#qrcode_generator(simple_code_generator(5))