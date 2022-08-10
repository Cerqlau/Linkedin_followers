 
from pymongo import MongoClient
from getmac import get_mac_address as gma #capturar o Mac do Pc
from bson.objectid import ObjectId #transforma str em bson  para verificação de _id no MongoDB

class MongodbLinkedin:
    
    def __init__(self,login='email_de_login_no_mongo_DB',password='password',database='myFirstDatabase') -> None:
        self.password = password
        self.login = login
        self.database = database
        self.client = MongoClient(f"mongodb+srv://{self.login}:{self.password}@cluster0.3rdov.mongodb.net/{self.database}?retryWrites=true&w=majority")
        self.db =self.client['myFirstDatabase']
        self.data_status = self.db['clients']
        self.data_licensa= self.db['licensa']
            
    def verifica_database(self):
        return self.db.list_collection_names()
    
    def verifica_colecao(self,colections):
        lista =[]
        colecao_data = self.db[colections]
        for i in colecao_data.find({}):
            lista.append(i)
        return lista
        
    def obter_licensa(self,id):
        lista =[]
        lista2=[]
        result = self.data_licensa.find({})
        for x in result:
            lista.append(x)
            lista2.append(str(x))
        for i in range(len(lista)):
            if id in lista2[i]:
                return lista[i][id]      
        return 'False'
                 
    
    def verficar_mac_address(self,id):
        self.mac_adress = gma()
        lista =[]
        lista2=[]
        lista3=[]
        result = self.data_licensa.find({})
        for x in result:
            lista.append(x)
            lista2.append(str(x)) 
        for i in range(len(lista)):
            if id in lista2[i]:
                object_id=lista[i]['_id']
                if  lista[i]['Macaddress'] == '0':
                    self.data_licensa.update_one({"_id":ObjectId(object_id)},{"$set":{"Macaddress":self.mac_adress}})
                    result = self.data_licensa.find({"_id":ObjectId(object_id)})
                    for j in result:
                        lista3.append(j) 
                    return lista3[0]['Macaddress']
                else:
                    result = self.data_licensa.find({"_id":ObjectId(object_id)})
                    for j in result:
                        lista3.append(j) 
                    return lista3[0]['Macaddress']
                    
                    
    def verifica_status(self,id):
        result = self.data_status.find({})
        lista = []
        try:
            for x in result:
                lista.append(str(x))
            for i in lista:
                if str(id) in i:
                    if "Ativado" in i:
                        return "Ativado"
                    else:
                        return "desativado"
            return 'False'
        except:
            return 'False'
                    
    def modifica_status_desativado(self,id):
        result = self.data_status.find({})
        lista = []
        try:
            for x in result:
                lista.append(str(x))
            for i in lista:
                if str(id) in i:
                    if "Ativado" in i:
                        self.data_status.find_one_and_replace({str(id):"Ativado"},{str(id):"desativado"})
                        return True
                    #else:
                    #self.data.find_one_and_replace({str(id):"desativado"},{str(id):"Ativado"})
                    # return True    
        except:
            return False
        
    def modifica_status_ativado(self,id):
        result = self.data_status.find({})
        lista = []
        try:
            for x in result:
                lista.append(str(x))
            for i in lista:
                if str(id) in i:
                    if "desativado" in i:
                        self.data_status.find_one_and_replace({str(id):"desativado"},{str(id):"Ativado"})
                        return True
                    #else:
                    # #self.data.find_one_and_replace({str(id):"desativado"},{str(id):"Ativado"})
                    # return True    
        except:
            return False
     

# Testes   
'''
database = MongodbLinkedin()
print (database.verifica_status("Ms215yNTil7920gwxdNA"))
print (database.verficar_mac_address("Ms215yNTil7920gwxdNA")) # 5c:c9:d3:b1:2b:85
print ('My Macadress -> '+ str(gma()))
if  database.verficar_mac_address("Ms215yNTil7920gwxdNA") == str(gma()):
    print('Mac compatível')
else: 
    print('Mac imcompatível')'''