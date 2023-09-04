from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

archivos_png = ['resources/out/CV1.png', 'resources/out/CV2.png']

# Output
pdf_output = 'resources/output.pdf'
c = canvas.Canvas(pdf_output, pagesize=letter)

# Iteration sheep
for archivo_png in archivos_png:
    c.drawImage(archivo_png, 0, 0, width=letter[0], height=letter[1])
    c.showPage()
# save
c.save()

print(f'Se ha creado {pdf_output} con éxito.')
