from PyPDF2 import PdfReader

nazwa="GL-AR-35WDC-R01-RGB-ver_2.0"

reader = PdfReader(nazwa + ".pdf")
page = reader.pages[0]

#print(page.extract_text())
with open(nazwa+".txt","a",encoding="utf-8") as file:
  file.writelines(page.extract_text())