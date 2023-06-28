import rpyc
from constRPYC import *

class Client:
    conn = rpyc.connect(SERVER, PORT)  # Conecte-se ao servidor
    print(conn.root.exposed_value())
    conn.root.exposed_append(5)  # Chame a operação exposta e adicione dois elementos
    conn.root.exposed_append(6)
    print(conn.root.exposed_value())  # Imprima o resultado

    print(conn.root.exposed_search_item(5))  # Pesquise o item 5 na lista
    conn.root.exposed_remove_item(5)  # Remova o item 5 da lista
    print(conn.root.exposed_value())  # Imprima o resultado após a remoção

    conn.root.exposed_insert_item_at_index(7, 0)  # Insira o item 7 no índice 0 da lista
    print(conn.root.exposed_value())  # Imprima o resultado após a inserção

    conn.root.exposed_sort_list()  # Ordene a lista
    print(conn.root.exposed_value())  # Imprima o resultado após a ordenação
