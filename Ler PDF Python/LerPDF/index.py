import tabula
import re
from IPython.display import display

# lista_tabelas = tabula.read_pdf("Telefones_Acarape.pdf", pages="1")
# # print(len(lista_tabelas))

# tabela = lista_tabelas[1]
# print(tabela)

def buscar_tabelas_com_telefone(pdf_path, pages="all"):

    lista_tabelas = tabula.read_pdf(pdf_path, pages=pages, multiple_tables=True)
    padrao_telefone = re.compile(r'\d{9}')

    for i, tabela in enumerate(lista_tabelas):

        tabela_str = tabela.to_string()
        telefones_encontrados = padrao_telefone.findall(tabela_str)
        
        if telefones_encontrados:
            print(f"Tabela encontrada na página {i + 1}:")
            display(tabela, "\n")
            print("Telefones encontrados:")
            print("\n".join(telefones_encontrados))
            print("-" * 40)

buscar_tabelas_com_telefone("Telefones_Acarape.pdf")