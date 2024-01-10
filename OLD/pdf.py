from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject

reader = PdfReader('D&D5E - Ficha editável.pdf')
writer = PdfWriter()

page1 = reader.pages[0]
page2 = reader.pages[1]
page3 = reader.pages[2]

fields = reader.get_fields()


# 0 à 5 são modificadores dos testes de resistência (CHECKBOXES)
# 25 à 30 savethrows (CHECKBOXES)

def carimbo(j):
    writer_annot = page1['/Annots'][j].get_object()
    for field in fields:
        if writer_annot.get('/T') == field:
            writer_annot.update({
                NameObject("/V"): NameObject("/Yes"),
                    NameObject("/AS"): NameObject("/Yes")
                })



def escriba(nome,raça,ATRT,MODATRT,p1,p2,r1,r2):
    writer.add_page(page1)

    #atribuindo nome, raça e valores de atributo
    writer.update_page_form_field_values(
        writer.pages[0],{
        "Campo de Texto0":"{}".format(nome[0].upper()+nome[1:]),"Campo de Texto13":"{}".format(raça),
        "Campo de Texto29":"{}".format(ATRT[0]),"Campo de Texto27":"{}".format(MODATRT[0]),
        "Campo de Texto33":"{}".format(ATRT[1]),"Campo de Texto30":"{}".format(MODATRT[1]),
        "Campo de Texto31":"{}".format(ATRT[2]),"Campo de Texto32":"{}".format(MODATRT[2]),
        "Campo de Texto34":"{}".format(ATRT[3]),"Campo de Texto35":"{}".format(MODATRT[3]),
        "Campo de Texto39":"{}".format(ATRT[4]),"Campo de Texto36":"{}".format(MODATRT[4]),
        "Campo de Texto37":"{}".format(ATRT[5]),"Campo de Texto38":"{}".format(MODATRT[5])})

    #save throw
    for n in range (0,6):
        writer.update_page_form_field_values(
            writer.pages[0], {'Campo de Texto6{}'.format(n):'{}'.format(MODATRT[n])})

    #6 à 23 são perícias (CHECKBOXES)
    #atribuindo valor de pericias
    writer.update_page_form_field_values(
        writer.pages[0],{
        "Campo de Texto66":"{}".format(MODATRT[1]),"Campo de Texto67":"{}".format(MODATRT[3]),
        "Campo de Texto68":"{}".format(MODATRT[0]),"Campo de Texto69":"{}".format(MODATRT[5]),
        "Campo de Texto70":"{}".format(MODATRT[5]),"Campo de Texto71":"{}".format(MODATRT[1]),
        "Campo de Texto72":"{}".format(MODATRT[3]),"Campo de Texto73":"{}".format(MODATRT[5]),
        "Campo de Texto74":"{}".format(MODATRT[4]),"Campo de Texto75":"{}".format(MODATRT[3]),
        "Campo de Texto76":"{}".format(MODATRT[4]),"Campo de Texto77":"{}".format(MODATRT[4]),
        "Campo de Texto78":"{}".format(MODATRT[3]),"Campo de Texto79":"{}".format(MODATRT[4]),
        "Campo de Texto80":"{}".format(MODATRT[5]),"Campo de Texto81":"{}".format(MODATRT[1]),
        "Campo de Texto82":"{}".format(MODATRT[3]),"Campo de Texto83":"{}".format(MODATRT[4])})

    #bonus de pericia e resist que vieram da classe
    testeResist = {0:"Campo de Texto60",1:"Campo de Texto61",2:"Campo de Texto62",
    3:"Campo de Texto63",4:"Campo de Texto64",5:"Campo de Texto65"}
    carimbo(r1)
    writer.update_page_form_field_values(
    writer.pages[0],{f'{testeResist[r1]}':f'{MODATRT[r1]+2}'})
    carimbo(r2)
    writer.update_page_form_field_values(
    writer.pages[0],{f'{testeResist[r2]}':f'{MODATRT[r2]+2}'})

    testePeric = {6:"Campo de Texto66",7:"Campo de Texto67",8:"Campo de Texto68",
    9:"Campo de Texto69",10:"Campo de Texto70",11:"Campo de Texto71",12:"Campo de Texto72",
    13:"Campo de Texto73",14:"Campo de Texto74",15:"Campo de Texto75",16:"Campo de Texto76",
    17:"Campo de Texto77",18:"Campo de Texto78",19:"Campo de Texto79",20:"Campo de Texto80",
    21:"Campo de Texto81",22:"Campo de Texto82",23:"Campo de Texto83"}
    carimbo(p2)
    if p2 == 8:
        num = MODATRT[0]
        writer.update_page_form_field_values(
        writer.pages[0],{f'{testePeric[p2]}':f'{MODATRT[num]+2}'})
    elif p2 in [6,11,21]:
        num = MODATRT[1]
        writer.update_page_form_field_values(
        writer.pages[0],{f'{testePeric[p2]}':f'{MODATRT[num]+2}'})
    elif p2 in [7,12,15,18,22]:
        num = MODATRT[3]
        writer.update_page_form_field_values(
        writer.pages[0],{f'{testePeric[p2]}':f'{MODATRT[num]+2}'})
    elif p2 in [14,16,17,19,23]:
        num = MODATRT[4]
        writer.update_page_form_field_values(
        writer.pages[0],{f'{testePeric[p2]}':f'{MODATRT[num]+2}'})
    else:
        num = MODATRT[5]
        writer.update_page_form_field_values(
        writer.pages[0],{f'{testePeric[p2]}':f'{MODATRT[num]+2}'})

    carimbo(p1)
    if p1 == 8:
        num = MODATRT[0]
        writer.update_page_form_field_values(
        writer.pages[0],{f'{testePeric[p1]}':f'{MODATRT[num]+2}'})
    elif p1 in [6,11,21]:
        num = MODATRT[1]
        writer.update_page_form_field_values(
        writer.pages[0],{f'{testePeric[p1]}':f'{MODATRT[num]+2}'})
    elif p1 in [7,12,15,18,22]:
        num = MODATRT[3]
        writer.update_page_form_field_values(
        writer.pages[0],{f'{testePeric[p1]}':f'{MODATRT[num]+2}'})
    elif p1 in [14,16,17,19,23]:
        num = MODATRT[4]
        writer.update_page_form_field_values(
        writer.pages[0],{f'{testePeric[p1]}':f'{MODATRT[num]+2}'})
    else:
        num = MODATRT[5]
        writer.update_page_form_field_values(
        writer.pages[0],{f'{testePeric[p1]}':f'{MODATRT[num]+2}'})

    
    writer.add_page(page2)
    writer.add_page(page3)
    
    with open("Ficha de {}.pdf".format(nome[0].upper()+nome[1:]), "wb") as output_stream:
        writer.write(output_stream)