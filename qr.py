import qrcode

data="https://github.com/Timalsinarabin" # Any data can be added to be encoded.
# To change size
qr=qrcode.QRCode(
    version= None,
    box_size=20,
    border=5
)
qr.add_data(data)
qr.make(fit=True)
# To change color of qrcode
img=qr.make_image(
    fill_color="black",
    back_color="white"
)
img.save("qr.png") # Save file as

'''
For basic Qrcode:
import qrcode

data="Hello to everyone" 
qr.make(data)
imq.save(data)
'''
