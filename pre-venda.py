import time
from pymongo import MongoClient
import sqlite3

Aprovado = {
    "_t": [
        "SituacaoMovimentacao",
        "Aprovado"
    ],
    "Codigo": 8,
    "Descricao": "Aprovado",
    "Cor": "#006400",
    "DescricaoComando":"Tornar pendente"
}
Aguardando = {
    "_t": [
        "SituacaoMovimentacao",
        "Aguardando"
    ],
    "Codigo": 1,
    "Descricao": "Aguardando",
    "Cor": "#006400",
    "DescricaoComando":"Tornar pendente"
}

while 1:
    client = MongoClient('localhost', username='temp', password='123456', authSource='DigisatServer', port=12220)
    database = client["DigisatServer"]
    collection = database["Movimentacoes"]

    query = {}
    cursor = collection.find(query)
    try:
        for doc in cursor:
            if "PreVenda" in doc["_t"]:
                id = str(doc['_id'])
                codigo = str(doc['Numero'])
                conn = sqlite3.connect('db.sqlite3')
                cursor1 = conn.cursor()
                cursor1.execute("SELECT * FROM prevendas where prevenda = '"+id+"';")
                result = cursor1.fetchone()
                if result == None:
                    cursor1.execute("INSERT INTO prevendas (prevenda, status, codigo) VALUES ('"+id+"', 8,'"+codigo+"')")
                    collection.find_one_and_update({"_id": doc["_id"]},
                                                  {"$set": {"Situacao": Aprovado}})

                elif result[2] != doc['Situacao']['Codigo'] and doc['Situacao']['Codigo'] != 12:
                    if result[2] == 8:
                        collection.find_one_and_update({"_id": doc["_id"]},
                                                       {"$set": {"Situacao": Aprovado}})
                    elif result[2] == 1:
                        collection.find_one_and_update({"_id": doc["_id"]},
                                                       {"$set": {"Situacao": Aguardando}})
                    else:
                        collection.find_one_and_update({"_id": doc["_id"]},
                                                       {"$set": {"Situacao": Aprovado}})
                conn.commit()
                conn.close()
        time.sleep(10)
    finally:
        client.close()
