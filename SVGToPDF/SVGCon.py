import cairosvg

def svg_to_formats(file_svg, out_format):
    try:
        out_file = f"output.{out_format}"
        cairosvg.svg2pdf(url=file_svg, write_to=out_file )
        print(f"¡File convert to: {out_format.upper()}!")
    except Exception as e:
        print(f"Error al convertir: {str(e)}")

# format into
archivo_svg = "resources/example.svg"

# list out formats
formats = ["pdf"] 

# convert to different out formats
for formato in formats:
    svg_to_formats(archivo_svg, formato)
