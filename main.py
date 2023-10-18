from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Dados que iremos utilizar para mostrar como tabelas
DATA = [
    ["Data", "Nome", "Assinatura", "Preço (R$)"],
    [
        "01/01/2023",
        "Premium",
        "Mensal",
        "100.00",
    ],
    [
        "02/01/2023",
        "Premium",
        "Anual",
        "1,000.00"
    ],
    ["Subtotal", "", "", "1,100.00"],
    ["Desconto", "", "", "300,00"],
    ["Total", "", "", "800,00"]
]

# Criando um template de uma folha A4
pdf = SimpleDocTemplate( "receita.pdf", pagesize=A4)

# Estilização padrão
styles = getSampleStyleSheet()

# Estilo do título
title_style = styles["Heading1"]
title_style.alignment = 1

# Criando o título
title = Paragraph("Receita", title_style)

# Estilo da tabela toda
style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
    ]
)

# Criando a tabela
table = Table(DATA, style = style)

# E finalmente criando o pdf
pdf.build([title, table])
