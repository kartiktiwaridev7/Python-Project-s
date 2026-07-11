import qrcode;

print(" Hello Ji this is the QR Code Genrator JI ")

QR_Code = input(" Enter the Exact QR Code link that you want to genrate the link \n")

# Genrate the Img of the QR Code

img = qrcode.make(QR_Code)

# Save the Img of the QR Code

img.save("basic_qr.png")
 
print(" QR code generated successfully!")