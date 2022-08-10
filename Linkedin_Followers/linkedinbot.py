
from cgitb import text
from msilib.schema import CheckBox
from selenium.webdriver.firefox.options import Options
import os,time,json
from configparser import ConfigParser
from colorama import Fore
from datetime import datetime,timedelta
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class LinkedinAPI:  
    '''Classe destinada a interação com o Linkedin'''
    
    def __init__(self):       
        self.site  ='https://www.linkedin.com/login/'
        self.site2 = 'https://www.linkedin.com/in/'
        self.site3='https://www.linkedin.com/mynetwork/'
        self.site4='https://www.linkedin.com/mynetwork/invitation-manager/sent/'
        self.seguindo_total=[]
        self.arreynomes=[]
        self.arreydominio=[]
        self.contatos_adicionados_recentemente=[]
        self.config2 = ConfigParser()
        self.config2.read('example.ini')
        self.memoria_contador = 0
            
    def banner(self):
            
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("")
        print ("")
        print (Fore.GREEN+"    __    _       __            ___        ")
        print (Fore.GREEN+"   / /   (_)___  / /_____  ____/ (_)___    ")
        print (Fore.GREEN+"  / /   / / __ \/ //_/ _ \/ __  / / __ \ ")
        print (Fore.GREEN+" / /___/ / / / / ,< /  __/ /_/ / / / / /    ")
        print (Fore.GREEN+"/_____/_/_/ /_/____|\___/\__,_/_/_/ /_/     ")
        print (Fore.GREEN+"              / __ \_________ _____ _____  (_)____   ")
        print (Fore.GREEN+"             / / / / ___/ __ `/ __ `/ __ \/ / ___/   ")
        print (Fore.GREEN+"            / /_/ / /  / /_/ / /_/ / / / / / /__   ")
        print (Fore.GREEN+"            \____/_/   \__, /\__,_/_/ /_/_/\___/   ")
        print (Fore.GREEN+"                      /____/____     ____          ")
        print (Fore.GREEN+"                        / ____/___  / / /___ _      _____  __________")
        print (Fore.GREEN+"                       / /_  / __ \/ / / __ \ | /| / / _ \/ ___/ ___/")
        print (Fore.GREEN+"                      / __/ / /_/ / / / /_/ / |/ |/ /  __/ /  (__  ) ")
        print (Fore.GREEN+"                     /_/    \____/_/_/\____/|__/|__/\___/_/  /____/  ")
        print (Fore.GREEN+"=======================================")
        print (Fore.LIGHTRED_EX+"Written by @laurocerqueira\n")
        print(Fore.LIGHTYELLOW_EX+"AUTOMAÇÃO DE CRESCIMENTO ORGÂNICO PARA O LINKEDIN\n"+Fore.RESET)
    
    def connect(self,login,password,id,headless):
        '''Insira, Login, Password e id do perfil ex:"https://www.linkedin.com/in/lauro-cerqueira-70473568/"
        o id seria: /lauro-cerqueira-70473568/'''
        self.delay=3
        self.password = password 
        self.login = login
        self.id = id
        self.site2 = self.site2 + self.id
        if  headless == 'True':
            _options=Options()
            _options.add_argument("--headless")
        else:
            _options=Options()   
        _options.add_argument("--log-level=3")
        _options.add_argument('--disable-logging')
        self._driver= webdriver.Firefox(executable_path = GeckoDriverManager().install(),options=_options)
        self.banner()
        msg = '###############################\n###INICIALIZAÇÃO DO PROGRAMA###\n###############################'
        self.log(msg)
        self._driver.implicitly_wait(30) #espera para carregamento do site
        self._driver.get(self.site)      #carrega o site
        self._driver.maximize_window()   #maximiza janela        
        #input de informações 
        WebDriverWait(self._driver,self.delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[name=session_key]')))  
        self._driver.find_element_by_css_selector('input[name=session_key]').send_keys(self.login) #insere login como input
        WebDriverWait(self._driver,self.delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[id=password]')))
        self._driver.find_element_by_css_selector('input[id=password]').send_keys(self.password) #insere passaword como input
        WebDriverWait(self._driver,self.delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type=submit]'))) #verifica se o elemento está acessível
        self._driver.find_element_by_css_selector('button[type=submit]').click() #ação de click no botão enviar 
        time.sleep(3)
        #acessa para a página de perfil do usuário
        self._driver.get(self.site2) #carrega o site
        #verificação se a página foi carregada
        try:
            Elem = WebDriverWait(self._driver,self.delay).until(EC.presence_of_element_located((By.ID,'ember28')))
            print (Fore.LIGHTGREEN_EX+'\nCONECTADO!!!\n'+Fore.RESET)
            msg = 'CONECTADO!!!'
            self.log(msg)
            msg2 = 'Id do perfil: '+self.id
            self.log(msg2)
            return msg
        except TimeoutException:
                print (Fore.LIGHTRED_EX+'\nTIME OUT!!!\n'+Fore.RESET)
                msg = 'TIME OUT!!!'
                self.log(msg)
                self.quit()
                return msg
        
    def quit(self):
        self.memoria_contador=0
        self._driver.quit()
        
    def log (self,msg):
        texto=msg
        with open('LOG_'+datetime.now().strftime('%d_%m_%Y')+'.txt','a') as arquivo:
            arquivo.write('\n'+str(texto)+' ______'+datetime.now().strftime( '%H:%M:%S'))
        arquivo.close()
        return texto
      
    def aguardando_def(self,timing):
        a=timing
        while True:
                    if a > 0:
                        data_hora2 = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                        print(data_hora2,' Aguardando...', end='\x1b[K\r')
                        a = a-1
                    if a <=0:
                        with open('LOG_'+datetime.now().strftime('%d_%m_%Y')+'.txt','a') as arquivo:
                            arquivo.write('\nAguardado...' +' ______'+datetime.now().strftime( '%H:%M:%S')+'\n')
                        arquivo.close()
                        break
                    else:
                        time.sleep(1)
    
    def aguardando(self):
        data_hora2 = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(data_hora2,' Aguardando...', end='\x1b[K\r')
        
    def remover(self,quantidade_tempo,quantidade_pessoas):
        '''Recebe a quantide de tempo ['dias','semanas','meses'] '''
        _quantidade_tempo = quantidade_tempo
        _quantidade_pessoas=quantidade_pessoas
        cont = 0
        cont2=0
        hoje = datetime.now().strftime('%d/%m/%Y')
        excluidos_mem = int(self.config2.get('executable2','excluidos'))
        memoria_qtd = int(self.config2.get('executable2','qtd'))
        self._driver.get(self.site4)
        arreynomes_op=[]
        time.sleep(3)
        for i in range(0,3,1):
            self._driver.execute_script('window.scrollTo(0,document.body.scrollHeight);') #scroll down na página para carregamento de perfis
            time.sleep(2)
        script_nome_perfil_quantidade = 'return document.getElementsByClassName("invitation-card__title t-16 t-black t-bold").length;' #quantidade de perfil por página
        script_paginas = 'return document.getElementsByClassName("artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view").length;' #verificar quantidade páginas
        paginas=int(self._driver.execute_script(script_paginas))
        quantidade_perfil_pagina = int(self._driver.execute_script(script_nome_perfil_quantidade))
        if paginas > 0: 
            for p in range(0,paginas,1): #loop com quantidade de páginas
                if p>0: # mudança de página 
                    self._driver.execute_script('document.getElementsByClassName("artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view")[0].click();')
                    time.sleep(5)
                    quantidade_perfil_pagina = int(self._driver.execute_script(script_nome_perfil_quantidade))
                    cont=0
                for q in range(0,quantidade_perfil_pagina,1): 
                    arreynomes=[]
                    script_tempo = 'return document.getElementsByClassName("time-badge t-12 t-black--light t-normal")['+str(cont)+'].innerText;' #verificação do tempo 
                    script_verificador_botao = 'return document.getElementsByClassName("artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--tertiary ember-view invitation-card__action-btn")['+str(cont)+'].innerText;'#verificação se o botão é retirar 
                    script_botao_retirar_click = 'document.getElementsByClassName("artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--tertiary ember-view invitation-card__action-btn")['+str(cont)+'].click();' #click no botão retirar 
                    script_confirmar_retirar_click = 'document.getElementsByClassName("artdeco-modal__confirm-dialog-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view")[0].click();' #botão confirmar retirar 
                    script_nome_perfil = 'return document.getElementsByClassName("invitation-card__title t-16 t-black t-bold")['+str(cont)+'].innerText;' #perfil excluido
                    try:
                        tempo = str(self._driver.execute_script(script_tempo))
                        verificador_botao = str(self._driver.execute_script(script_verificador_botao))
                        nome_perfil = str(self._driver.execute_script(script_nome_perfil))
                        if _quantidade_tempo in tempo:
                            if verificador_botao == 'Retirar':
                                self._driver.execute_script(script_botao_retirar_click)
                                time.sleep(2)
                                self._driver.execute_script(script_confirmar_retirar_click)
                                time.sleep(2)
                                memoria_qtd = memoria_qtd+1
                                self.config2.set('executable2','qtd', str(memoria_qtd))
                                with open("example.ini", "w") as configfile:
                                    self.config2.write(configfile) 
                                configfile.close()
                                with open("unfollowed.json", "r") as f:
                                    arrey = json.load(f) #atualização da lista de adicionados em arquivo json
                                f.close()
                                for contatos in range(0,len(arrey)):
                                    arreynomes.append(arrey[contatos])
                                arreynomes.append((nome_perfil,hoje))
                                with open("unfollowed.json", "w") as f:
                                    json.dump(arreynomes,f,indent='',ensure_ascii = False) #atualização da lista de adicionados em arquivo json
                                f.close()
                                print(f'{Fore.LIGHTBLUE_EX}{nome_perfil} : removida solicitação')
                                msg = nome_perfil +' : removida solicitação'
                                arreynomes_op.append(msg)
                                self.log(msg)
                                cont2=cont2+1
                                excluidos_mem=excluidos_mem+1
                                self.config2.set('executable2','excluidos', str(excluidos_mem))
                                self.config2.set('executable2','utilizado', str(hoje))
                                with open("example.ini", "w") as configfile:
                                    self.config2.write(configfile) 
                                configfile.close()      
                        cont=cont+1
                        if cont2 >= int(_quantidade_pessoas):
                            print(Fore.LIGHTGREEN_EX+'\nQuantidade de solicitações removidas: '+str(cont2) +'\nOperação finalizada com sucesso!!!\n'+Fore.RESET)
                            msg = '\nQuantidade de solicitações removidas:'+str(cont2) +'\nOperação finalizada com sucesso!!!'
                            self.log(msg)
                            msg = 'Quantidade de solicitações removidas:'+str(cont2) +'\nOperação finalizada com sucesso!!!'
                            arreynomes_op.append(msg)
                            return arreynomes_op 
                    except:
                        pass
                if cont2 >= int(_quantidade_pessoas):
                    print(Fore.LIGHTGREEN_EX+'\nQuantidade de solicitações removidas: '+str(cont2) +'\nOperação finalizada com sucesso!!!\n'+Fore.RESET)
                    msg = '\nQuantidade de solicitações removidas:'+str(cont2) +'\nOperação finalizada com sucesso!!!'
                    self.log(msg)
                    msg = 'Quantidade de solicitações removidas:'+str(cont2) +'\nOperação finalizada com sucesso!!!'
                    arreynomes_op.append(msg)
                    return arreynomes_op
                else:
                    if (p+1) >= paginas and (q+1)>=quantidade_perfil_pagina and cont2 == 0:
                        print(Fore.LIGHTRED_EX+'\nNão foi encontrado nenhum perfil que atendesse aos requisitos da busca\n'+Fore.RESET)
                        msg='\nNão foi encontrado nenhum perfil que atendesse aos requisitos da busca'
                        self.log(msg)
                        msg='Não foi encontrado nenhum perfil que atendesse aos requisitos da busca'
                        arreynomes_op.append(msg)
                        return arreynomes_op
                    if (p+1) >= paginas and (q+1)>=quantidade_perfil_pagina and cont2>0:
                        print(Fore.LIGHTGREEN_EX+'\nQuantidade de solicitações removidas: '+str(cont2) +Fore.RED+'\nOperação finalizada sem atingir o número total esperado!!!\n'+Fore.RESET)
                        msg = '\nQuantidade de solicitações removidas:'+str(cont2) +'\nOperação finalizada sem atingir o número total esperado!!!'
                        self.log(msg)
                        msg ='Quantidade de solicitações removidas:'+str(cont2) +'\nOperação finalizada sem atingir o número total esperado!!!'
                        arreynomes_op.append(msg)
                        return arreynomes_op
        else:
            for q in range(0,quantidade_perfil_pagina,1): 
                arreynomes=[]
                script_tempo = 'return document.getElementsByClassName("time-badge t-12 t-black--light t-normal")['+str(cont)+'].innerText;' #verificação do tempo 
                script_verificador_botao = 'return document.getElementsByClassName("artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--tertiary ember-view invitation-card__action-btn")['+str(cont)+'].innerText;'#verificação se o botão é retirar 
                script_botao_retirar_click = 'document.getElementsByClassName("artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--tertiary ember-view invitation-card__action-btn")['+str(cont)+'].click();' #click no botão retirar 
                script_confirmar_retirar_click = 'document.getElementsByClassName("artdeco-modal__confirm-dialog-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view")[0].click();' #botão confirmar retirar 
                script_nome_perfil = 'return document.getElementsByClassName("invitation-card__title t-16 t-black t-bold")['+str(cont)+'].innerText;' #perfil excluido
                try:
                    tempo = str(self._driver.execute_script(script_tempo))
                    verificador_botao = str(self._driver.execute_script(script_verificador_botao))
                    nome_perfil = str(self._driver.execute_script(script_nome_perfil))
                    if _quantidade_tempo in tempo:
                        if verificador_botao == 'Retirar':
                            self._driver.execute_script(script_botao_retirar_click)
                            time.sleep(2)
                            self._driver.execute_script(script_confirmar_retirar_click)
                            time.sleep(2)
                            memoria_qtd = memoria_qtd+1
                            self.config2.set('executable2','qtd', str(memoria_qtd))
                            with open("example.ini", "w") as configfile:
                                self.config2.write(configfile) 
                            configfile.close()
                            with open("unfollowed.json", "r") as f:
                                arrey = json.load(f) #atualização da lista de adicionados em arquivo json
                            f.close()
                            for contatos in range(0,len(arrey)):
                                arreynomes.append(arrey[contatos])
                            arreynomes.append((nome_perfil,hoje))
                            with open("unfollowed.json", "w") as f:
                                json.dump(arreynomes,f,indent='',ensure_ascii = False) #atualização da lista de adicionados em arquivo json
                            f.close()
                            print(f'{Fore.LIGHTBLUE_EX}{nome_perfil} : removida solicitação')
                            msg = nome_perfil +' : removida solicitação'
                            arreynomes_op.append(msg)
                            self.log(msg)
                            cont2=cont2+1
                            excluidos_mem=excluidos_mem+1
                            self.config2.set('executable2','excluidos', str(excluidos_mem))
                            self.config2.set('executable2','utilizado', str(hoje))
                            with open("example.ini", "w") as configfile:
                                self.config2.write(configfile) 
                            configfile.close()      
                    cont=cont+1
                    if cont2 >= int(_quantidade_pessoas):
                        print(Fore.LIGHTGREEN_EX+'\nQuantidade de solicitações removidas: '+str(cont2) +'\nOperação finalizada com sucesso!!!\n'+Fore.RESET)
                        msg = '\nQuantidade de solicitações removidas:'+str(cont2) +'\nOperação finalizada com sucesso!!!'
                        self.log(msg)
                        msg = 'Quantidade de solicitações removidas:'+str(cont2) +'\nOperação finalizada com sucesso!!!'
                        arreynomes_op.append(msg)
                        return arreynomes_op
                except:
                    pass
                if (q+1)>=quantidade_perfil_pagina and cont2 == 0:
                    print(Fore.LIGHTRED_EX+'\nNão foi encontrado nenhum perfil que atendesse aos requisitos da busca\n'+Fore.RESET)
                    msg='\nNão foi encontrado nenhum perfil que atendesse aos requisitos da busca'
                    self.log(msg)
                    msg='Não foi encontrado nenhum perfil que atendesse aos requisitos da busca'
                    arreynomes_op.append(msg)
                    return arreynomes_op
                if (q+1)>=quantidade_perfil_pagina and cont2>0:
                    print(Fore.LIGHTGREEN_EX+'\nQuantidade de solicitações removidas: '+str(cont2) +Fore.RED+'\nOperação finalizada sem atingir o número total esperado!!!\n'+Fore.RESET)
                    msg = '\nQuantidade de solicitações removidas:'+str(cont2) +'\nOperação finalizada sem atingir o número total esperado!!!'
                    self.log(msg)
                    msg ='Quantidade de solicitações removidas:'+str(cont2) +'\nOperação finalizada sem atingir o número total esperado!!!'
                    arreynomes_op.append(msg)
                    return arreynomes_op
            return arreynomes_op.append(msg)
                                 
    def adicionar(self,quantidade):
        quantidade_add = quantidade
        cont =8 #0 para iniciar com sua empresa atual e 9 para iniciar com outros grupos
        cont2=0 # quantidade de solcitação enviada
        cont3=0 # quantidade de vezes que pulou as solicitações 
        element='None' # elemento nome
        element2='None' # elemento botão
        arreynomes_op=[] # array de operações realizadas
        hoje = datetime.now().strftime('%d/%m/%Y')
        adicionados_mem = int(self.config2.get('executable','adicionados'))
        memoria_qtd = int(self.config2.get('executable','qtd'))
        memoria_qtd = memoria_qtd+1
        self.config2.set('executable','qtd', str(memoria_qtd))
        with open("example.ini", "w") as configfile:
            self.config2.write(configfile) 
        configfile.close()
        self._driver.get(self.site3)
        time.sleep(3)
        for i in range(0,20,1):
            self._driver.execute_script('window.scrollTo(0,document.body.scrollHeight);') #scroll down na página para carregamento de perfis
            time.sleep(2)
        while True:
            arreynomes=[]
            script1 ='return document.getElementsByClassName("discover-person-card__name t-16 t-black t-bold")['+str(cont)+'].innerText;'
            script2 ='return document.getElementsByClassName("artdeco-button artdeco-button--2 artdeco-button--secondary ember-view full-width")['+str(cont)+'].innerText;' 
            script3 ='document.getElementsByClassName("artdeco-button artdeco-button--2 artdeco-button--secondary ember-view full-width")['+str(cont)+'].click();'
            qtd_element = self._driver.execute_script('document.getElementsByClassName("discover-person-card__name t-16 t-black t-bold").length')
            if qtd_element == cont:
                for i in range(0,20,1):
                    self._driver.execute_script('window.scrollTo(0,document.body.scrollHeight);') #scroll down na página para carregamento de perfis
                    time.sleep(2)
            try:
                try:
                    element=str(self._driver.execute_script(script1))
                    element2= str(self._driver.execute_script(script2))
                except:
                    pass
                if element != 'None':
                    if element2 == 'Conectar':
                        try:
                           element3= self._driver.execute_script('return document.getElementsByClassName("ip-fuse-limit-alert__header t-20 t-black ph4")[0].innerText')
                           if str(element3) == 'Você alcançou o limite semanal de convites':
                               print(Fore.LIGHTRED_EX+'\nVocê alcançou o limite semanal de convites'+Fore.RESET)
                               msg = 'Você alcançou o limite semanal de convites'
                               self.log(msg)
                               arreynomes_op.append(msg)
                               return arreynomes_op 
                        except:
                            pass 
                        self._driver.execute_script(script3)
                        time.sleep(3.5)
                        element2= str(self._driver.execute_script(script2))
                        try:
                            if element2 =='Pendente':
                                cont3=0 #zera contador de erros 
                                # armazanenamento na lista de operações feitas
                                print(Fore.LIGHTBLUE_EX+str(element)+' : solicitação enviada')
                                cont2=cont2+1
                                msg = str(element)+' : solicitação enviada'
                                arreynomes_op.append(msg)
                                self.log(msg)
                                #atualização de banco de dados
                                with open("followed.json", "r") as f:
                                    arrey = json.load(f) #atualização da lista de adicionados em arquivo json
                                f.close()
                                for contatos in range(0,len(arrey)):
                                    arreynomes.append(arrey[contatos])
                                arreynomes.append((element,hoje))
                                with open("followed.json", "w") as f:
                                    json.dump(arreynomes,f,indent='',ensure_ascii = False) #atualização da lista de adicionados em arquivo json
                                f.close()
                                adicionados_mem=adicionados_mem+1
                                self.config2.set('executable','adicionados', str(adicionados_mem))
                                self.config2.set('executable','utilizado', str(hoje))
                                with open("example.ini", "w") as configfile:
                                    self.config2.write(configfile) 
                                configfile.close()
                                #verificação se a quantidade estipula foi atingida
                                if cont2 >= int(quantidade_add):
                                    print(Fore.LIGHTGREEN_EX+'\nQuantidade de solicitações enviadas: '+str(cont2) +'\nOperação finalizada com sucesso!!!\n'+Fore.RESET)
                                    msg = '\nQuantidade de solicitações enviadas:'+str(cont2) +'\nOperação finalizada com sucesso!!!\n'
                                    self.log(msg)
                                    arreynomes_op.append(msg)
                                     
                        except:
                            print(Fore.LIGHTRED_EX+'\nNão foi possível adicionar o usuário'+Fore.RESET)
                            msg = '\nNão foi possível adicionar o usuário'
                            self.log(msg)
                            arreynomes_op.append(msg)
                            cont3 +=1
                            #return arreynomes_op   
                    else:
                        cont3 +=1
                        print(Fore.LIGHTMAGENTA_EX+'\nPerfil Corporativo encontrado'+Fore.RESET)
                        msg = 'Perfil Corporativo encontrado'
                        self.log(msg)
                        arreynomes_op.append(msg)
                        if cont3 >=50:
                            print(Fore.LIGHTRED_EX+'\nPerfil {self.id} NÃO possui sugestões de nincho\nNecessário adicionar outros perfis manualmente'+Fore.RESET)
                            msg = f'\nPerfil {self.id} NÃO possui sugestões de nincho\nNecessário adicionar outros perfis manualmente\nNecessário conectar novamente'
                            self.log(msg)
                            arreynomes_op.append(msg)
                            return arreynomes_op
                    if self.memoria_contador <= cont:      
                        self.memoria_contador=cont=cont+1
                    else:
                        cont = self.memoria_contador    
                else:
                    cont3 +=1
                    if cont3 >=50:
                            print(Fore.LIGHTRED_EX+'\nPerfil {self.id} NÃO possui sugestões de nincho\nNecessário adicionar outros perfis manualmente'+Fore.RESET)
                            msg = f'\nPerfil {self.id} NÃO possui sugestões de nincho\nNecessário adicionar outros perfis manualmente\nNecessário conectar novamente'
                            self.log(msg)
                            arreynomes_op.append(msg)
                            return arreynomes_op    
                time.sleep(0.5)
            except:
               print(Fore.LIGHTRED_EX+'\nErro de conexão com o servidor'+'\nQuantidade de solicitações enviadas: '+str(cont2)+'\n'+Fore.RESET)
               msg = 'Erro de conexão com o servidor'+'\nQuantidade de solicitações enviadas: '+str(cont2)+'\nNecessário conectar novamente'
               self.log(msg)
               arreynomes_op.append(msg)
               self.quit()
               return arreynomes_op
        return arreynomes_op

   

       
       
        
        
    
                
        
    

    
   
    