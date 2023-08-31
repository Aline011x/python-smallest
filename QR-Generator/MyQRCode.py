import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=1)
qr.add_data("https://www.youtube.com/watch?v=2YlElORNC40")
qr.make(fit=True)

img= qr.make_image(fill_color="orange", back_color='white')  
img.save("resources/image.png")  

'''
img = qrcode.make("Hello Word! From QR")
img.save("mycode.png")

'''
