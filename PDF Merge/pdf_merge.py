from PyPDF2 import PdfWriter
pdfs=[]
merger = PdfWriter()
n=int(input("Enter how many pdf you want to merge?\n"))
for i in range (0,n):
    name=input(f"Entar pdf name {i+1}:\n")
    merger.append(name)
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()