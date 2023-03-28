from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4') # Orientation: P = Portrait, L = Landscape.

df = pd.read_csv('topics.csv')
for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24) # style='B' = Bold, All pdf cells below this will be in this font. Must declare again to change font.
    pdf.set_text_color(100, 100, 100) # RGB
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', 
            ln=1) # w=0... width=0 extends until end of page. ln=1 makes a break line. h... height should be = font size. border=1 makes a boder around the cell.
    pdf.line(10, 21, 200, 21) # Requires x1, y1, x2, y2 coordinates. Distance from borders: left, top, left, top respectively
pdf.output('output.pdf')