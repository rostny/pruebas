<<<<<<< HEAD
'''
FILE    funciones.py
FUNCION funciones de uso particular para este proceso
AUTOR   Antonio Araujo
FECHA   Set 2022
'''

# funcion tipo left
def left(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[:amount]
    else:
        if (len(substring) > amount):
            substring = substring[:amount]
        return substring + s[:-amount]
# funcion tipo right 
def right(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[-amount:]
    else:
        if (len(substring) > amount):
            substring = substring[:amount]
        return s[:-amount] + substring
# funcion tipo mid
def mid(s, startChar, howMany):
    if howMany < 1:
        return ''
    else:
        return s[(startChar-1):(startChar+howMany-1)]

def filtrar(cadena):
    # eliminar caracteres especiales
    if ("   " in cadena):cadena = cadena.replace("   "," ")    
    if ("  " in cadena):cadena = cadena.replace("  "," ")    
    if ("'" in cadena):cadena = cadena.replace("'","")
    if ("&" in cadena):cadena = cadena.replace("&"," Y ")
    if ("&apos;" in cadena):cadena = cadena.replace("&apos;","")
    if ('"' in cadena):cadena = cadena.replace('"',"'")            
    if ("&amp;" in cadena):cadena = cadena.replace("&amp;","/")   
    if ("nan" in cadena):cadena = cadena.replace("nan","0.00")     
    #reemplazar vocales
    if ("á" in cadena):cadena = cadena.replace("á","a")    
    if ("Á" in cadena):cadena = cadena.replace("Á","A")                        
    if ("é" in cadena):cadena = cadena.replace("é","e")    
    if ("É" in cadena):cadena = cadena.replace("É","E")                
    if ("í" in cadena):cadena = cadena.replace("í","i")                
    if ("Í" in cadena):cadena = cadena.replace("Í","I")                            
    if ("ó" in cadena):cadena = cadena.replace("ó","o")            
    if ("Ó" in cadena):cadena = cadena.replace("Ó","O")                        
    if ("ú" in cadena):cadena = cadena.replace("ú","u")    
    if ("Ú" in cadena):cadena = cadena.replace("Ú","U")
    cadena = cadena.strip()
    return(cadena)

#diccionario paises segun norma iso-3166-2
#argumento nombre de pais amyusculas/minusculas
def buscar_pais(xpais):
    pais = {"AFGHANISTAN":"AF","ALAND ISLANDS":"AX","ALBANIA":"AL","ALGERIA":"DZ","AMERICAN SAMOA":"AS","ANDORRA":"AD","ANGOLA":"AO","ANGUILLA":"AI","ANTARCTICA":"AQ","ANTIGUA & BARBUDA":"AG","ARGENTINA":"AR","ARMENIA":"AM","ARUBA":"AW","AUSTRALIA":"AU","AUSTRIA":"AT","AZERBAIJAN":"AZ","BAHAMAS":"BS","BAHRAIN":"BH","BANGLADESH":"BD","BARBADOS":"BB","BELARUS":"BY","BELGIUM":"BE","BELIZE":"BZ","BENIN":"BJ","BONAIRE SINT EUSTATIUS AND SABA":"BQ","BOSNIA AND HERZEGOVINA":"BA","BOTSWANA":"BW","BOUVET ISLAND":"BV","BRAZIL":"BR","BRITISH INDIAN OCEAN TERRITORY":"IO","BRUNEI":"BN","BULGARIA":"BG","BURKINA FASO":"BF","BURUNDI":"BI","CABO VERDE":"CV","CAMBODIA":"KH","CAMEROON":"CM","CANADA":"CA","CAYMAN ISLANDS":"KY","CENTRAL AFRICAN REPUBLIC":"CF","CHAD":"TD","CHILE":"CL","CHINA":"CN","CHRISTMAS ISLAND":"CX","COCOS (KEELING) IS.":"CC","COLOMBIA":"CO","COMOROS":"KM","CONGO DEM. REP.":"CD","CONGO REP.":"CG","BERMUDA":"BM","BHUTAN":"BT","COSTA RICA":"CR","COTE DIVOIRE":"CI","CROATIA":"HR","CUBA":"CU","CURAÇAO":"CW","CYPRUS":"CY","CZECH REPUBLIC":"CZ","DENMARK":"DK","DJIBOUTI":"DJ","DOMINICA":"DM","DOMINICAN REPUBLIC":"DO","ECUADOR":"EC","EGYPT":"EG","EL SALVADOR":"SV","EQUATORIAL GUINEA":"GQ","ERITREA":"ER","ESTONIA":"EE","ESWATINI":"SZ","ETHIOPIA":"ET","FALKLAND ISLANDS":"FK","FAROE ISLANDS":"FO","FIJI":"FJ","FINLAND":"FI","FRANCE":"FR","FRENCH GUIANA":"GF","FRENCH SOUTHERN TERRITORIES":"TF","FRENCH POLYNESIA":"PF","GABON":"GA","GAMBIA":"GM","GEORGIA":"GE","GERMANY":"DE","COOK ISLANDS":"CK","BOLIVIA":"BO","GIBRALTAR":"GI","GREECE":"GR","GREENLAND":"GL","GRENADA":"GD","GUADELOUPE":"GP","GUAM":"GU","GUATEMALA":"GT","GUERNSEY":"GG","GUINEA":"GN","GUINEA-BISSAU":"GW","GUYANA":"GY","HAITI":"HT","HEARD ISLAND AND MCDONALD ISLANDS":"HM","HONDURAS":"HN","HONG KONG":"HK","HUNGARY":"HU","ICELAND":"IS","INDIA":"IN","INDONESIA":"ID","IRAN":"IR","IRAQ":"IQ","IRELAND":"IE","ISLE OF MAN":"IM","ISRAEL":"IL","ITALY":"IT","JAMAICA":"JM","JAPAN":"JP","JERSEY":"JE","JORDAN":"JO","KAZAKHSTAN":"KZ","KENYA":"KE","GHANA":"GH","KOREA, NORTH":"KP","KOREA, SOUTH":"KR","KUWAIT":"KW","KYRGYZSTAN":"KG","LAOS":"LA","LATVIA":"LV","LEBANON":"LB","LESOTHO":"LS","LIBERIA":"LR","LIBYA":"LY","LIECHTENSTEIN":"LI","LITHUANIA":"LT","LUXEMBOURG":"LU","MACAU":"MO","MACEDONIAi":"MK","MADAGASCAR":"MG","MALAWI":"MW","MALAYSIA":"MY","MALDIVES":"MV","MALI":"ML","MALTA":"MT","MARSHALL ISLANDS":"MH","MARTINIQUE":"MQ","MAURITANIA":"MR","MAURITIUS":"MU","MAYOTTE":"YT","MEXICO":"MX","MICRONESIA":"FM","KIRIBATI":"KI","MONACO":"MC","MONGOLIA":"MN","MONTENEGRO":"ME","MONTSERRAT":"MS","MOROCCO":"MA","MOZAMBIQUE":"MZ","MYANMAR":"MM","N. MARIANA IS.":"MP","NAMIBIA":"NA","NAURU":"NR","NEPAL":"NP","NETHERLANDS":"NL","NETHERLANDS ANTILLESiii":"AN","NEW CALEDONIA":"NC","NEW ZEALAND":"NZ","NICARAGUA":"NI","NIGER":"NE","NIGERIA":"NG","NIUE":"NU","NORFOLK ISLAND":"NF",            "NORTH MACEDONIA":"MK","NORWAY":"NO","OMAN":"OM","PAKISTAN":"PK","PALAU":"PW","PALESTINE":"PS","PANAMA":"PA","PAPUA NEW GUINEA":"PG","MOLDOVA":"MD","PERU":"PE","PHILIPPINES":"PH","PITCAIRN":"PN","POLAND":"PL","PORTUGAL":"PT","PUERTO RICO":"PR","QATAR":"QA","REUNION":"RE","ROMANIA":"RO","RUSSIAN FEDERATION":"RU","RWANDA":"RW","SAINT BARTHELEMY":"BL","SAINT HELENA ASCENSION AND TRISTAN DA CUNHA":"SH","SAINT KITTS / NEVIS":"KN","SAINT LUCIA":"LC","SAINT MARTIN (FRENCH PART)":"MF","SAMOA":"WS","SAN MARINO":"SM","SAO TOME / PRINCIPE":"ST","SAUDI ARABIA":"SA","SENEGAL":"SN","SERBIA":"RS","SERBIA / MONTENEGRO":"CS","SEYCHELLES":"SC","SIERRA LEONE":"SL","SINGAPORE":"SG","SINT MAARTEN":"SX","SLOVAKIA":"SK","PARAGUAY":"PY","SLOVENIA":"SI","SOLOMON ISLANDS":"SB","SOMALIA":"SO","SOUTH AFRICA":"ZA","SOUTH SUDAN":"SS","SPAIN":"ES","SRI LANKA":"LK","ST VINCENT / GRENADINES":"VC","ST. PIERRE & MIQUELON":"PM","SUDAN":"SD","SURINAME":"SR","SVALBARD":"SJ","SWAZILANDv":"SZ","SWEDEN":"SE","SWITZERLAND":"CH","SYRIA":"SY","TAIWAN":"TW","TAJIKISTAN":"TJ","TANZANIA":"TZ","THAILAND":"TH","TIMOR-LESTE":"TL","TOGO":"TG","TOKELAU":"TK","TONGA":"TO","TRINIDAD AND TOBAGO":"TT","TUNISIA":"TN","TURKEY":"TR","TURKMENISTAN":"TM","TURKS AND CAICOS IS.":"TC","TUVALU":"TV","UGANDA":"UG","UKRAINE":"UA","UNITED ARAB EMIRATES":"AE","UNITED KINGDOM":"GB","UNITED STATES MINOR OUTLYING ISLANDS":"UM",  "URUGUAY":"UY","USA":"US","UZBEKISTAN":"UZ","VANUATU":"VU","VATICAN CITY":"VA","VENEZUELA":"VE","VIET NAM":"VN","VIRGIN ISLANDS (BRITISH)":"VG","VIRGIN ISLANDS (U.S.)":"VI","WALLIS & FUTUNA IS.":"WF","WESTERN SAHARA":"EH","YEMEN":"YE","ZAMBIA":"ZM","ZIMBABWE":"ZW"}
    xpais = xpais.upper()
    if (xpais=='UNKNOWN'):
        return('--')
    if (xpais in pais):
        return pais[xpais]
    else:
        return ('--')

def fechas(xfecha):
    xfecha = xfecha.strip()
    if (len(xfecha)<5):
        return('0001-01-01')
    xfecha = xfecha.replace("'","")
    xfecha = xfecha.replace("/","-")
    xfecha = xfecha.replace(">","")
    xfecha = xfecha.replace("<","")
    anio = left(xfecha,4)
    if (anio=='0000'):
        anio = '1901'
    mes  = mid(xfecha,6,2)
    if (mes=='00'):
        mes = '01'
    dia  = right(xfecha,2)
    if (dia=='00'):
        dia = '01'
    xfecha = anio + '-' + mes + '-' + dia    
    return (xfecha)

def f_leer(xcad:str,arg1:str,arg2:str)->str:
    xtag = {"updatecategory=":"updcat=","sub-category=":"subcat="}
    # determina posicion de cada arg1
    x = xcad.index(arg1)
    if x==0:
        x = len(arg1)
    else:
        x = x + len(arg1) + 1
    # determina posicion de cada arg2
    y = xcad.index(arg2)
    if y==0:
        xcadena = xcad[x:]
    else:
        xcadena = xcad[x:y]
    # borra espacios en blanco de la cadena
    xcadena = xcadena.strip()
    # verifica si el arg1 está en diccionario 
    if (arg1 in xtag):
        arg1 = xtag[arg1]
    # analiza los campos fecha 
    if (arg1=='entered=' or arg1=='updated=' or arg1=='<dob>'):
        xcadena = fechas(xcadena)
        xcadena = xcadena.replace('0000-00-00','null')
    # busca el codigo de pais
    if(arg1=='<country>'):
        xcadena = buscar_pais(xcadena)
    # quita simbolos <,>, =
    arg1 = arg1.lstrip("<").rstrip(">").rstrip("=")
    arg2 = arg2.lstrip("<").rstrip(">").rstrip("=")
    # arma la cadena de salida
    xcadena = '<'+left(arg1,len(arg1))+'>' + xcadena.strip() + '</'+left(arg1,len(arg1))+'>'
    xcadena = xcadena.replace("'","")    
    # retorna la cadena
=======
'''
FILE    funciones.py
FUNCION funciones de uso particular para este proceso
AUTOR   Antonio Araujo
FECHA   Set 2022
        Dic 2023 agrega f_leer
'''

# funcion tipo left
def left(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[:amount]
    else:
        if (len(substring) > amount):
            substring = substring[:amount]
        return substring + s[:-amount]
# funcion tipo right 
def right(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[-amount:]
    else:
        if (len(substring) > amount):
            substring = substring[:amount]
        return s[:-amount] + substring
# funcion tipo mid
def mid(s, startChar, howMany):
    if howMany < 1:
        return ''
    else:
        return s[(startChar-1):(startChar+howMany-1)]

def filtrar(cadena):
    # eliminar caracteres especiales
    if ("   " in cadena):cadena = cadena.replace("   "," ")    
    if ("  " in cadena):cadena = cadena.replace("  "," ")    
    if ("'" in cadena):cadena = cadena.replace("'","")
    if ("&" in cadena):cadena = cadena.replace("&"," Y ")
    if ("&apos;" in cadena):cadena = cadena.replace("&apos;","")
    if ('"' in cadena):cadena = cadena.replace('"',"'")            
    if ("&amp;" in cadena):cadena = cadena.replace("&amp;","/")   
    if ("nan" in cadena):cadena = cadena.replace("nan","0.00")     
    #reemplazar vocales
    if ("á" in cadena):cadena = cadena.replace("á","a")    
    if ("Á" in cadena):cadena = cadena.replace("Á","A")                        
    if ("é" in cadena):cadena = cadena.replace("é","e")    
    if ("É" in cadena):cadena = cadena.replace("É","E")                
    if ("í" in cadena):cadena = cadena.replace("í","i")                
    if ("Í" in cadena):cadena = cadena.replace("Í","I")                            
    if ("ó" in cadena):cadena = cadena.replace("ó","o")            
    if ("Ó" in cadena):cadena = cadena.replace("Ó","O")                        
    if ("ú" in cadena):cadena = cadena.replace("ú","u")    
    if ("Ú" in cadena):cadena = cadena.replace("Ú","U")
    cadena = cadena.strip()
    return(cadena)

#diccionario paises segun norma iso-3166-2
#argumento nombre de pais amyusculas/minusculas
def buscar_pais(xpais):
    pais = {"AFGHANISTAN":"AF","ALAND ISLANDS":"AX","ALBANIA":"AL","ALGERIA":"DZ","AMERICAN SAMOA":"AS","ANDORRA":"AD","ANGOLA":"AO","ANGUILLA":"AI","ANTARCTICA":"AQ","ANTIGUA & BARBUDA":"AG","ARGENTINA":"AR","ARMENIA":"AM","ARUBA":"AW","AUSTRALIA":"AU","AUSTRIA":"AT","AZERBAIJAN":"AZ","BAHAMAS":"BS","BAHRAIN":"BH","BANGLADESH":"BD","BARBADOS":"BB","BELARUS":"BY","BELGIUM":"BE","BELIZE":"BZ","BENIN":"BJ","BONAIRE SINT EUSTATIUS AND SABA":"BQ","BOSNIA AND HERZEGOVINA":"BA","BOTSWANA":"BW","BOUVET ISLAND":"BV","BRAZIL":"BR","BRITISH INDIAN OCEAN TERRITORY":"IO","BRUNEI":"BN","BULGARIA":"BG","BURKINA FASO":"BF","BURUNDI":"BI","CABO VERDE":"CV","CAMBODIA":"KH","CAMEROON":"CM","CANADA":"CA","CAYMAN ISLANDS":"KY","CENTRAL AFRICAN REPUBLIC":"CF","CHAD":"TD","CHILE":"CL","CHINA":"CN","CHRISTMAS ISLAND":"CX","COCOS (KEELING) IS.":"CC","COLOMBIA":"CO","COMOROS":"KM","CONGO DEM. REP.":"CD","CONGO REP.":"CG","BERMUDA":"BM","BHUTAN":"BT","COSTA RICA":"CR","COTE DIVOIRE":"CI","CROATIA":"HR","CUBA":"CU","CURAÇAO":"CW","CYPRUS":"CY","CZECH REPUBLIC":"CZ","DENMARK":"DK","DJIBOUTI":"DJ","DOMINICA":"DM","DOMINICAN REPUBLIC":"DO","ECUADOR":"EC","EGYPT":"EG","EL SALVADOR":"SV","EQUATORIAL GUINEA":"GQ","ERITREA":"ER","ESTONIA":"EE","ESWATINI":"SZ","ETHIOPIA":"ET","FALKLAND ISLANDS":"FK","FAROE ISLANDS":"FO","FIJI":"FJ","FINLAND":"FI","FRANCE":"FR","FRENCH GUIANA":"GF","FRENCH SOUTHERN TERRITORIES":"TF","FRENCH POLYNESIA":"PF","GABON":"GA","GAMBIA":"GM","GEORGIA":"GE","GERMANY":"DE","COOK ISLANDS":"CK","BOLIVIA":"BO","GIBRALTAR":"GI","GREECE":"GR","GREENLAND":"GL","GRENADA":"GD","GUADELOUPE":"GP","GUAM":"GU","GUATEMALA":"GT","GUERNSEY":"GG","GUINEA":"GN","GUINEA-BISSAU":"GW","GUYANA":"GY","HAITI":"HT","HEARD ISLAND AND MCDONALD ISLANDS":"HM","HONDURAS":"HN","HONG KONG":"HK","HUNGARY":"HU","ICELAND":"IS","INDIA":"IN","INDONESIA":"ID","IRAN":"IR","IRAQ":"IQ","IRELAND":"IE","ISLE OF MAN":"IM","ISRAEL":"IL","ITALY":"IT","JAMAICA":"JM","JAPAN":"JP","JERSEY":"JE","JORDAN":"JO","KAZAKHSTAN":"KZ","KENYA":"KE","GHANA":"GH","KOREA, NORTH":"KP","KOREA, SOUTH":"KR","KUWAIT":"KW","KYRGYZSTAN":"KG","LAOS":"LA","LATVIA":"LV","LEBANON":"LB","LESOTHO":"LS","LIBERIA":"LR","LIBYA":"LY","LIECHTENSTEIN":"LI","LITHUANIA":"LT","LUXEMBOURG":"LU","MACAU":"MO","MACEDONIAi":"MK","MADAGASCAR":"MG","MALAWI":"MW","MALAYSIA":"MY","MALDIVES":"MV","MALI":"ML","MALTA":"MT","MARSHALL ISLANDS":"MH","MARTINIQUE":"MQ","MAURITANIA":"MR","MAURITIUS":"MU","MAYOTTE":"YT","MEXICO":"MX","MICRONESIA":"FM","KIRIBATI":"KI","MONACO":"MC","MONGOLIA":"MN","MONTENEGRO":"ME","MONTSERRAT":"MS","MOROCCO":"MA","MOZAMBIQUE":"MZ","MYANMAR":"MM","N. MARIANA IS.":"MP","NAMIBIA":"NA","NAURU":"NR","NEPAL":"NP","NETHERLANDS":"NL","NETHERLANDS ANTILLESiii":"AN","NEW CALEDONIA":"NC","NEW ZEALAND":"NZ","NICARAGUA":"NI","NIGER":"NE","NIGERIA":"NG","NIUE":"NU","NORFOLK ISLAND":"NF",            "NORTH MACEDONIA":"MK","NORWAY":"NO","OMAN":"OM","PAKISTAN":"PK","PALAU":"PW","PALESTINE":"PS","PANAMA":"PA","PAPUA NEW GUINEA":"PG","MOLDOVA":"MD","PERU":"PE","PHILIPPINES":"PH","PITCAIRN":"PN","POLAND":"PL","PORTUGAL":"PT","PUERTO RICO":"PR","QATAR":"QA","REUNION":"RE","ROMANIA":"RO","RUSSIAN FEDERATION":"RU","RWANDA":"RW","SAINT BARTHELEMY":"BL","SAINT HELENA ASCENSION AND TRISTAN DA CUNHA":"SH","SAINT KITTS / NEVIS":"KN","SAINT LUCIA":"LC","SAINT MARTIN (FRENCH PART)":"MF","SAMOA":"WS","SAN MARINO":"SM","SAO TOME / PRINCIPE":"ST","SAUDI ARABIA":"SA","SENEGAL":"SN","SERBIA":"RS","SERBIA / MONTENEGRO":"CS","SEYCHELLES":"SC","SIERRA LEONE":"SL","SINGAPORE":"SG","SINT MAARTEN":"SX","SLOVAKIA":"SK","PARAGUAY":"PY","SLOVENIA":"SI","SOLOMON ISLANDS":"SB","SOMALIA":"SO","SOUTH AFRICA":"ZA","SOUTH SUDAN":"SS","SPAIN":"ES","SRI LANKA":"LK","ST VINCENT / GRENADINES":"VC","ST. PIERRE & MIQUELON":"PM","SUDAN":"SD","SURINAME":"SR","SVALBARD":"SJ","SWAZILANDv":"SZ","SWEDEN":"SE","SWITZERLAND":"CH","SYRIA":"SY","TAIWAN":"TW","TAJIKISTAN":"TJ","TANZANIA":"TZ","THAILAND":"TH","TIMOR-LESTE":"TL","TOGO":"TG","TOKELAU":"TK","TONGA":"TO","TRINIDAD AND TOBAGO":"TT","TUNISIA":"TN","TURKEY":"TR","TURKMENISTAN":"TM","TURKS AND CAICOS IS.":"TC","TUVALU":"TV","UGANDA":"UG","UKRAINE":"UA","UNITED ARAB EMIRATES":"AE","UNITED KINGDOM":"GB","UNITED STATES MINOR OUTLYING ISLANDS":"UM",  "URUGUAY":"UY","USA":"US","UZBEKISTAN":"UZ","VANUATU":"VU","VATICAN CITY":"VA","VENEZUELA":"VE","VIET NAM":"VN","VIRGIN ISLANDS (BRITISH)":"VG","VIRGIN ISLANDS (U.S.)":"VI","WALLIS & FUTUNA IS.":"WF","WESTERN SAHARA":"EH","YEMEN":"YE","ZAMBIA":"ZM","ZIMBABWE":"ZW"}
    xpais = xpais.upper()
    if (xpais=='UNKNOWN'):
        return('--')
    if (xpais in pais):
        return pais[xpais]
    else:
        return ('--')

def fechas(xfecha):
    xfecha = xfecha.strip()
    if (len(xfecha)<5):
        return('0001-01-01')
    xfecha = xfecha.replace("'","")
    xfecha = xfecha.replace("/","-")
    xfecha = xfecha.replace(">","")
    xfecha = xfecha.replace("<","")
    anio = left(xfecha,4)
    if (anio=='0000'):
        anio = '1901'
    mes  = mid(xfecha,6,2)
    if (mes=='00'):
        mes = '01'
    dia  = right(xfecha,2)
    if (dia=='00'):
        dia = '01'
    xfecha = anio + '-' + mes + '-' + dia    
    return (xfecha)

def f_leer(xcad:str,arg1:str,arg2:str)->str:
    xtag = {"updatecategory=":"updcat=","sub-category=":"subcat="}
    # determina posicion de cada arg1
    x = xcad.index(arg1)
    if x==0:
        x = len(arg1)
    else:
        x = x + len(arg1) + 1
    # determina posicion de cada arg2
    y = xcad.index(arg2)
    if y==0:
        xcadena = xcad[x:]
    else:
        xcadena = xcad[x:y]
    # borra espacios en blanco de la cadena
    xcadena = xcadena.strip()
    # verifica si el arg1 está en diccionario 
    if (arg1 in xtag):
        arg1 = xtag[arg1]
    # analiza los campos fecha 
    if (arg1=='entered=' or arg1=='updated=' or arg1=='<dob>'):
        xcadena = fechas(xcadena)
        xcadena = xcadena.replace('0000-00-00','null')
    # busca el codigo de pais
    if(arg1=='<country>'):
        xcadena = buscar_pais(xcadena)
    # quita simbolos <,>, =
    arg1 = arg1.lstrip("<").rstrip(">").rstrip("=")
    arg2 = arg2.lstrip("<").rstrip(">").rstrip("=")
    # arma la cadena de salida
    xcadena = '<'+left(arg1,len(arg1))+'>' + xcadena.strip() + '</'+left(arg1,len(arg1))+'>'
    xcadena = xcadena.replace("'","")    
    # retorna la cadena
>>>>>>> 9ab7d1ba15b08cdbd683181a9f5c127f25d6ca17
    return(xcadena)