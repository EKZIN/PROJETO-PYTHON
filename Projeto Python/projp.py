import os
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

pdf.set_font('Times', '', 15)
titulo = "PROJETO DE PYTHON"
texto = "Pra quem não sabe o Corona Vírus surgiu em 2019, em Dezembro (por isso o '19' no nome) na China, e rapidamente se espalhou pelo mundo todo, chegando no Brasil em no final de Fevereiro de 2020 e dai pra frente as coisas começam a andar para trás, milhões de pessoas morreram no mundo todo, principalmente no Brasil onde foram 628 mil mortes!"
texto2 = "Análisando o gráfico, vimos que 11,88% de todo o Brasil foi infectado, ou seja a cada 100 pessoas 12 já foram infectadas pelo Covid-19, porem 87% se recuperaram e conseguiram retomar as suas ao normal de volta!\n\n\n                                                           Mais vai com calma...\n                                                       O vírus ainda não acabou!"
texto3 = "Esses são os registros de casos confirmados de covid entre os dias 24 a 28 de Janeiro desse ano, a pandemia não acabou, sei que as coisas precisam voltar ao normal o mais rápido possível, mais se cuidem e se guardem, pense nas pessoas a sua volta. Tudo isso vai passar!     -     Fica aqui meus pêsames pelas 628 mil mortes!"

pdf.multi_cell(w=0, h=6, txt=titulo, align='J')
pdf.ln()
pdf.multi_cell(w=0, h=6, txt=texto, align='J')
pdf.ln()
pdf.image(name='grafico_bi.png', x=25, y=50, w=150)
pdf.ln(95)
pdf.multi_cell(w=0, h=6, txt=texto2, align='J')
pdf.ln()
pdf.image(name='atencao_cd19.png', x=25, y=200, w=150)
pdf.ln(100)
pdf.multi_cell(w=0, h=6, txt=texto3, align='J')

pdf.output('projp.pdf')

print("O PDF foi criado com sucesso!")
os.system("pause")