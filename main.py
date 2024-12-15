import img2pdf
import os
folderPath = input("Enter the path of the file and name it as 'input.png'")
filePath = os.path.join(folderPath, "input.png")

with open(filePath, "rb") as image:
    pdf_bytes = img2pdf.convert(image.read())

newFilePath = os.path.join(folderPath, "output.pdf")
with open(newFilePath, "wb") as pdf:
    pdf.write(pdf_bytes)

print(f"Image has been converted to pdf succesfully. Check here: {newFilePath}")
