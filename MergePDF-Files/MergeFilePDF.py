from PyPDF2 import PdfMerger

pdfs = ['one.pdf', 'two.pdf', 'three.pdf']

merger = PdfMerger()

for pdf in pdfs: 
        merger.append(pdf)
        
        
merger.write("resources/merger.pdf")
merger.close()