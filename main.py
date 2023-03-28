from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4') # Orientation: P = Portrait, L = Landscape.
pdf.set_auto_page_break(auto=False, margin = 0) # Set pages to stop breaking automatically.

df = pd.read_csv('topics.csv')
for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family='Times', style='B', size=24) # style='B' = Bold, All pdf cells below this will be in this font. Must declare again to change font.
    pdf.set_text_color(100, 100, 100) # RGB
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', 
            ln=1) # w=0... width=0 extends until end of page. ln=1 makes a break line. h... height should be = font size. border=1 makes a boder around the cell.
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    # pdf.line(10, 21, 200, 21) # Requires x1, y1, x2, y2 coordinates. Distance from borders: left, top, left, top respectively.

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'])

    

    for i in range(row['Pages'] -1): # Nested for loop. 
        pdf.add_page()
        # Set the footer
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'])

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output('output.pdf')