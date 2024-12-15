import img2pdf

with open("TVH.png", "rb") as image:
    pdf_bytes = img2pdf.convert(image.read())

with open("TVM.pdf", "wb") as pdf:
    pdf.write(pdf_bytes)

print("Image has been converted to pdf succesfully.")