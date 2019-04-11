from reportlab.lib.pagesizes import letter # US Letter size (default is A4)
from reportlab.pdfgen import canvas


width, height = letter # 612 x 792


invoice = canvas.Canvas("invoice.pdf")

comp_pos = []
bill_to_comp_pos = []
issue_date_pos = []
due_date_pos = []
balance_due_pos = []
column_titles_pos = []

invoice.setFont('Courier', 11, leading=None)
invoice.drawString(72, 792, "Nathaniel Lee")
invoice.drawString(520, 792, "Invoice #1")

invoice.save()


# print(width,height)

# from reportlab.lib import colors
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
 
# doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
# # container for the 'Flowable' objects
# elements = []
 
# data= [['00', '01', '02', '03', '04'],
#        ['10', '11', '12', '13', '14'],
#        ['20', '21', '22', '23', '24'],
#        ['30', '31', '32', '33', '34']]
# t=Table(data)
# t.setStyle(TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),
#                        ('TEXTCOLOR',(0,0),(1,-1),colors.red)]))
# elements.append(t)
# # write the document to disk
# doc.build(elements)



# Example code below from: https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/

# import time
# from reportlab.lib.enums import TA_JUSTIFY
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.units import inch
 
# doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
#                         rightMargin=72,leftMargin=72,
#                         topMargin=72,bottomMargin=18)
# Story=[]
# magName = "Pythonista"
# issueNum = 12
# subPrice = "99.00"
# limitedDate = "03/05/2010"
# freeGift = "tin foil hat"
 
# formatted_time = time.ctime()
# full_name = "Mike Driscoll"
# address_parts = ["411 State St.", "Marshalltown, IA 50158"]
  
# styles=getSampleStyleSheet()
# styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
# ptext = '<font size=12>%s</font>' % formatted_time
 
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
 
# # Create return address
# ptext = '<font size=12>%s</font>' % full_name
# Story.append(Paragraph(ptext, styles["Normal"]))       
# for part in address_parts:
#     ptext = '<font size=12>%s</font>' % part.strip()
#     Story.append(Paragraph(ptext, styles["Normal"]))   
 
# Story.append(Spacer(1, 12))
# ptext = '<font size=12>Dear %s:</font>' % full_name.split()[0].strip()
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
 
# ptext = '<font size=12>We would like to welcome you to our subscriber base for %s Magazine! \
#         You will receive %s issues at the excellent introductory price of $%s. Please respond by\
#         %s to start receiving your subscription and get the following free gift: %s.</font>' % (magName, 
#                                                                                                 issueNum,
#                                                                                                 subPrice,
#                                                                                                 limitedDate,
#                                                                                                 freeGift)
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 12))
 
 
# ptext = '<font size=12>Thank you very much and we look forward to serving you.</font>'
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 12))
# ptext = '<font size=12>Sincerely,</font>'
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 48))
# ptext = '<font size=12>Ima Sucker</font>'
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
# doc.build(Story)