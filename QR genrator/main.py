import qrcode

upi_id = input("Enter Your UPI ID = ")

phonepe_url = f'upi://pay?pa={upi_id}&pn= Recipient%20Name&mc = 1234'
paytm_url = f'upi://pay?pa={upi_id}&pn = Recipient%20Name&mc = 1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn = Recipient%20Name&mc = 1234'

#create QR code for each payment app 

phonepe_qr =qrcode.make(phonepe_url)
paytm_qr =qrcode.make(paytm_url)
google_pay_qr =qrcode.make(google_pay_url)



#Save the QR code to image file 

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')


#Display QR code
phonepe_qr.show()
paytm_qr.show()
