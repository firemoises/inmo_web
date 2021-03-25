def scrape_data_corotos(url,tipo_neg,metodo,chrome_drv,loads=20,solo_agentes=0,no_dupli=1):
    """
    metodo: 1 = Selenium
    metodo: 2 = requests y lxml
    """
    
    import random
    from time import sleep
    from selenium import webdriver
    from pymongo import MongoClient
    import requests
    from lxml import html
    import pandas as pd
    
    props = {}
    
    ## Funcion para ver si un doc existe
    def existe_doc(obj):
        try:
            obj[0]
        except:
            var_exists = False
        else:
            var_exists = True

        return var_exists


    # Instanciar un cliente de Mongo
    #client = MongoClient('localhost')
    #db = client['inmo_oport']
    #col = db["propiedades"]

    #driver = webdriver.Chrome(chrome_drv)
    driver = webdriver.Firefox()
    driver.get(url)
    
        
    ############# BLOQUE PARA CLICKEAR EN LOAD MORE
    
    for n in range(loads):
        try:
            name_boton_load_more = "//a[@id='load-more-listings']"
            boton = driver.find_element_by_xpath(name_boton_load_more)
            boton.click()
            print("Se clickeo cargar mas ",n)
            sleep(random.uniform(2,4))
            boton = driver.find_element_by_xpath(name_boton_load_more)
        except:
            print("problem con el boton load more")

    #################
    
    if solo_agentes == 1:
        cant_ads = driver.find_elements_by_xpath(f"/html/body/main/div[3]/div[3]/div[2]/div//div[@data-seller-type='Agente']")
    else:
        cant_ads = driver.find_elements_by_xpath(f"/html/body/main/div[3]/div[3]/div[2]/div")
    
    cant_ads = len(cant_ads)
    print("Se extraera de ",cant_ads," propiedades")
    
    for n_link in range(1,cant_ads): #La cantidad de propiedades a recoger
        
        caracs = []
        ##Si ya esta en la BD no guardar la prop
        """
        if no_dupli == 1:
            
            try:
                url_prop = driver.find_elements_by_xpath(f"/html/body/main/div[3]/div[3]/div[2]/div[{n_link}]//a[@class='item__image']")[0].get_attribute("href")
                
                obj = col.find({"url":url_prop})
                if existe_doc(obj):
                    print("Ya la prop ",n_link," existe, pasaremos a la siguiente propiedad")
                    continue #Si ya existe pasa a la siguiente prop
            except:
                print("Parece hubo algun error revisando si habia duplicados, pasaremos a la siguiente propiedad")
                continue
    
        """
    
        #####SI SOLO QUEREMOS SCRAPEAR AGENTES        
        if solo_agentes == 1:
            check_agente = driver.find_elements_by_xpath(f"/html/body/main/div[3]/div[3]/div[2]/div[{n_link}]//div[@data-seller-type='Agente']")
            if len(check_agente)>0:
                ads = driver.find_elements_by_xpath(f"/html/body/main/div[3]/div[3]/div[2]/div[{n_link}]/div/h3/a")
        else:
            ads = driver.find_elements_by_xpath(f"/html/body/main/div[3]/div[3]/div[2]/div[{n_link}]/div/h3/a")

        
        ## Confirmar si es agente
        agente_confirmar = driver.find_elements_by_xpath(f"/html/body/main/div[3]/div[3]/div[2]/div[{n_link}]//div[@data-seller-type='Agente']") 
        if len(agente_confirmar) > 0:
            es_agente = 1
        else:
            es_agente = 0
            
        
        for ad in ads:
            try:
                ad_text = ad.text

                if ad_text == None or ad_text == "None" or ad_text == "" or ad_text == "\n" or ad_text == "\n\n":
                    pass
                else:
                    link = ad.get_attribute("href")

                    if metodo == 1: ##Selenium 

                        sleep(random.uniform(3,6))
                        #driver.get(link)
                        driver.execute_script(f"window.open('{link}');")
                        driver.switch_to.window(driver.window_handles[1]) #Nos vamos al new tab
                        
                        titulo = driver.find_element_by_xpath(".//h1[@class='post__title']").text
                        precio_raw = driver.find_element_by_xpath(".//h2[@class='post__price']").text
                        fecha_post_raw = driver.find_element_by_xpath(".//p[@class='post__date']").text
                        location_and_tipo = driver.find_elements_by_xpath(".//ul[@class='post__category-and-location']/li")
                        location = location_and_tipo[0].text.replace("location_on","").replace("\n","")
                        tipo_name = location_and_tipo[1].text.replace("local_offer","").replace("\n","")
                        author = driver.find_element_by_xpath(".//h3[@class='author__name']").text
                        age_account_raw = driver.find_element_by_xpath(".//h3[@class='author__name']/following-sibling::p").text


                        #### Bloque para recoger los features de habs, banos, etc

                        features = driver.find_elements_by_xpath(".//span[@class='specs__label']")
                        features = [f.text for f in features]

                        feats = {} 
                        for i,f in enumerate(features):

                            try:
                                feats[f] = driver.find_element_by_xpath(f".//span[@class='specs__label'][contains(text(),'{f}')]//following-sibling::span")
                            except:
                                pass

                        feats = {k:feats[k].text for k in feats}

                        ###############################


                        #### Bloque para recoger la desc

                        desc = driver.find_elements_by_xpath(".//h3[contains(text(),'Descripción')]//following-sibling::p")
                        desc = [d.text for d in desc]

                        ###############################


                        #### Bloque para recoger el tel

                        try:
                            tel_button = driver.find_element_by_xpath(".//a[@id='show-phone-number']")
                        except:
                            tel = "NA"

                        try:
                            tel_button.click()
                            sleep(random.uniform(1,3))
                            tel = driver.find_elements_by_xpath(".//div[@id='the-actual-phone']/a")
                            tel = [t.text for t in tel][0]
                        except:
                            tel = "NA"

                        ###############################


                        #print(titulo,precio_raw,fecha_post_raw,location,tipo_name,feats,desc,author,age_account_raw,tel,"\n\n\n")
                        
                        
                        
                        ##Si ya esta en la BD no entrar en la prop 2
                        """
                        if no_dupli == 1:
                            try:
                                obj = col.find({'precio_raw':precio_raw,'titulo':titulo})
                                if existe_doc(obj):
                                        print("Ya la prop ",i," existe, pasaremos a la siguiente propiedad")
                                        continue #Si ya existe pasa a la siguiente prop
                            except:
                                print("Parece hubo algun error revisando si habia duplicados, pasaremos a la siguiente propiedad")
                                continue
                                
                        """

                        #Insertar propiedad
                        """
                        col.insert_one({
                            'titulo': titulo,
                            'precio_raw': precio_raw,
                            'fecha_post_raw': fecha_post_raw,
                            'location': location,
                            'tipo_name': tipo_name,
                            'author': author,
                            'age_account_raw': age_account_raw,
                            'feats': feats,
                            'desc': desc,
                            'tel': tel,
                            'tipo_neg': tipo_neg,
                            'origen': "corotos",
                            'metodo': metodo,
                            'url': link,
                            'agente': es_agente
                        })
                        print("Agregada ",n_link,titulo)
                        """
                        caracs.append(titulo)
                        caracs.append(precio_raw)
                        caracs.append(fecha_post_raw)
                        caracs.append(location)
                        props[n_link] = caracs

                        sleep(random.uniform(3,6))
                        #driver.back()
                        driver.close() #Para cerrar el tab
                        driver.switch_to.window(driver.window_handles[0]) #Nos regresamos a nuestro tab


                    elif metodo == 2: #Request y lxml

                        encabezados = {
                                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36"
                        }

                        url = link
                        respuesta = requests.get(url, headers=encabezados)
                        parser = html.fromstring(respuesta.text)
                        try:
                            titulo = parser.xpath(".//h1[@class='post__title']/text()")
                            precio_raw = parser.xpath(".//h2[@class='post__price']/text()")
                            fecha_post_raw = parser.xpath(".//p[@class='post__date']/text()")
                            location_and_tipo = parser.xpath(".//ul[@class='post__category-and-location']/li")
                            location = location_and_tipo[0].text.replace("location_on","").replace("\n","")
                            tipo_name = location_and_tipo[1].text.replace("local_offer","").replace("\n","")
                            author = parser.xpath(".//h3[@class='author__name']/text()")
                            age_account_raw = parser.xpath(".//h3[@class='author__name']/following-sibling::p/text()")
                        except Exception as e:
                            print("Hubo algun problema al analizar los features, seguira con la siguiente ",e)
                            continue


                        #### Bloque para recoger los features de habs, banos, etc

                        features = parser.xpath(".//span[@class='specs__label']")
                        features = [f.text for f in features]

                        feats = {}
                        feats2 = {} #Para tomar los que tienen otro xpath
                        for i,f in enumerate(features):

                            try:
                                feats[f] = parser.xpath(f".//span[@class='specs__label'][contains(text(),'{f}')]//following-sibling::span/span/text()")
                            except:
                                pass

                            try:
                                feats2[f] = parser.xpath(f".//span[@class='specs__label'][contains(text(),'{f}')]//following-sibling::span/text()")
                            except:
                                pass

                        feats = {k:feats[k] for k in feats if len(feats[k]) > 0}
                        feats2 = {k:feats2[k] for k in feats2 if len(feats2[k]) > 0}

                        feats.update(feats2)

                        ###############################


                        #### Bloque para recoger la desc

                        desc = parser.xpath(".//h3[contains(text(),'Descripción')]//following-sibling::p")
                        desc = [d.text for d in desc]

                        ###############################


                        #print(titulo,precio_raw,fecha_post_raw,location,tipo_name,feats,desc,author,age_account_raw,"\n\n\n")


                        #Insertar propiedad
                        """
                        col.insert_one({
                            'titulo': titulo,
                            'precio_raw': precio_raw,
                            'fecha_post_raw': fecha_post_raw,
                            'location': location,
                            'tipo_name': tipo_name,
                            'author': author,
                            'age_account_raw': age_account_raw,
                            'feats': feats,
                            'desc': desc,
                            'tel': "NA",
                            'tipo_neg': tipo_neg,
                            'origen': "corotos",
                            'metodo': metodo,
                            'url': link,
                            'agente': es_agente
                        })
                        print("Agregada ",n_link,titulo)
                        """

                        caracs.append(titulo)
                        caracs.append(precio_raw)
                        caracs.append(fecha_post_raw)
                        caracs.append(location)
                        props[n_link] = caracs
            except:
                print("No se pudo cargar esta prop")
                #driver.back()
                driver.close() #Para cerrar el tab
                driver.switch_to.window(driver.window_handles[0]) #Nos regresamos a nuestro tab

    #Cuando hayamos terminado
    driver.close()
    driver.quit()

    #df = pd.DataFrame(list(col.find()))
    #return df

    return props
