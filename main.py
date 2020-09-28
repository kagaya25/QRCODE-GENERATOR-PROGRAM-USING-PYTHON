import qrcode
qr=qrcode.QRCode(
	version=1,
	box_size=5,
	border=2

	)
data="https://kagayajohn.com/"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("url.png")