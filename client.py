import rpyc
from constRPYC import *

class Client:
    conn = rpyc.connect(SERVER, PORT) 
    print(conn.root.exposed_value())
    conn.root.exposed_append(5)  
    conn.root.exposed_append(6)
    print(conn.root.exposed_value())  

    print(conn.root.exposed_search_item(5)) 
    conn.root.exposed_remove_item(5)  
    print(conn.root.exposed_value())  

    conn.root.exposed_insert_item_at_index(7, 0)  
    print(conn.root.exposed_value())  

    conn.root.exposed_sort_list()  
    print(conn.root.exposed_value())  
