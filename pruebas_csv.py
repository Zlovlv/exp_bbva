import csv
#tipo_usuario=input()
lista_csv=[]
#apertura de archivo y creacion de lista de datos para guardar datos de archivo csv
with open ("synergy_logistics_database.csv","r") as base_datos:
    
     lector= csv.DictReader(base_datos)
        
     for registro in lector:
         lista_csv.append(registro)

def select_data(data_ask):
    lista_get=[]
    for item_search in lista_csv[:10]:
        lista_get.append(item_search[data_ask])
    return lista_get
print(select_data("direction")) 
""" lista_get=[]
for item in lista_csv[:8]:
    lista_get.append(item["direction"])
print(lista_get) """