import qrcode

# Taking  UPI ID as a input

upi_id = input("Enter your UPI ID: ")

# upi://pay?pa=UPI_ID%pn=?NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defining the payment URL based on the UPI ID and the payment app.
# you can modify these URLs based on the payment apps you want to support. 

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
payment_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Create QR code for each payment app

phonepe_url = qrcode.make(phonepe_url)
payment_url = qrcode.make(payment_url)
google_pay_url = qrcode.make(google_pay_url)

# save the QR code to image file (optinal)

phonepe_url.save("phonepe_qr.png")
payment_url.save("payment_qr.png")
google_pay_url.save("google_pay_qr.png")

# Display the QR codes (You may need to install PIL/Pillow library.)

phonepe_url.show()
payment_url.show()
google_pay_url.show()