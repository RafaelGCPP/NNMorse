
def letters_range(prefix,init, end):
    return [prefix+chr(i) for i in range(ord(init), ord(end) + 1)]

ITU_PREFIX_DATABASE=[]
ITU_PREFIX_DATABASE+=zip(letters_range("A","A","L"),["United States"]*12)
ITU_PREFIX_DATABASE+=zip(letters_range("A","M","O"),["Spain"]*3)
ITU_PREFIX_DATABASE+=zip(letters_range("A","P","S"),["Pakistan"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("A","T","W"),["India"]*4)
ITU_PREFIX_DATABASE+=[("AX","Australia")]
ITU_PREFIX_DATABASE+=zip(letters_range("A","Y","Z"),["Argentina"]*2)
ITU_PREFIX_DATABASE+=[("A2","Botswana")]
ITU_PREFIX_DATABASE+=[("A3","Tonga")]
ITU_PREFIX_DATABASE+=[("A4","Oman")]
ITU_PREFIX_DATABASE+=[("A5","Bhutan")]
ITU_PREFIX_DATABASE+=[("A6","United Arab Emirates")]
ITU_PREFIX_DATABASE+=[("A7","Qatar")]
ITU_PREFIX_DATABASE+=[("A8","Liberia")]
ITU_PREFIX_DATABASE+=[("A9","Bahrain")]
ITU_PREFIX_DATABASE+=[("B","China")]
ITU_PREFIX_DATABASE+=zip(letters_range("B","A","L"),["China"]*12)
ITU_PREFIX_DATABASE+=zip(letters_range("B","M","Q"),["Taiwan"]*5)
ITU_PREFIX_DATABASE+=zip(letters_range("B","R","T"),["China"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("B","U","X"),["Taiwan"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("B","Y","Z"),["China"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("C","A","E"),["Chile"]*5)
ITU_PREFIX_DATABASE+=zip(letters_range("C","F","K"),["Canada"]*6)
ITU_PREFIX_DATABASE+=zip(letters_range("C","L","M"),["Cuba"]*2)
ITU_PREFIX_DATABASE+=[("CN","Morocco")]
ITU_PREFIX_DATABASE+=[("CO","Cuba")]
ITU_PREFIX_DATABASE+=zip(letters_range("C","P","U"),["Portugal"]*5)
ITU_PREFIX_DATABASE+=zip(letters_range("C","V","X"),["Uruguay"]*3)  
ITU_PREFIX_DATABASE+=zip(letters_range("C","Y","Z"),["Canada"]*2)
ITU_PREFIX_DATABASE+=[("C2","Nauru")]
ITU_PREFIX_DATABASE+=[("C3","Andorra")]
ITU_PREFIX_DATABASE+=[("C4","Cyprus")]
ITU_PREFIX_DATABASE+=[("C5","The Gambia")]
ITU_PREFIX_DATABASE+=[("C6","The Bahamas")]
ITU_PREFIX_DATABASE+=[("C7","World Meteorological Organization")]
ITU_PREFIX_DATABASE+=zip(letters_range("C","8","9"),["Mozambique"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("D","A","R"),["Germany"]*18)
ITU_PREFIX_DATABASE+=zip(letters_range("D","S","T"),["South Korea"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("D","U","Z"),["Philippines"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("D","2","3"),["Angola"]*2)
ITU_PREFIX_DATABASE+=[("D4","Cape Verde")]
ITU_PREFIX_DATABASE+=[("D5","Liberia")]
ITU_PREFIX_DATABASE+=[("D6","Comoros")]
ITU_PREFIX_DATABASE+=zip(letters_range("D","7","9"),["South Korea"]*3)
ITU_PREFIX_DATABASE+=zip(letters_range("E","A","H"),["Spain"]*8)
ITU_PREFIX_DATABASE+=zip(letters_range("E","I","J"),["Ireland"]*2)
ITU_PREFIX_DATABASE+=[("EK","Armenia")]
ITU_PREFIX_DATABASE+=[("EL","Liberia")]
ITU_PREFIX_DATABASE+=zip(letters_range("E","M","O"),["Ukraine"]*3)
ITU_PREFIX_DATABASE+=zip(letters_range("E","P","Q"),["Iran"]*2)
ITU_PREFIX_DATABASE+=[("ER","Moldova")]
ITU_PREFIX_DATABASE+=[("ES","Estonia")]
ITU_PREFIX_DATABASE+=[("ET","Ethiopia")]
ITU_PREFIX_DATABASE+=zip(letters_range("E","U","W"),["Belarus"]*3)
ITU_PREFIX_DATABASE+=[("EX","Kyrgyzstan")]
ITU_PREFIX_DATABASE+=[("EY","Tajikistan")]
ITU_PREFIX_DATABASE+=[("EZ","Turkmenistan")]
ITU_PREFIX_DATABASE+=[("E2","Thailand")]
ITU_PREFIX_DATABASE+=[("E3","Eritrea")]
ITU_PREFIX_DATABASE+=[("E4","Palestinian Authority")]
ITU_PREFIX_DATABASE+=[("E5","Cook Islands")]
ITU_PREFIX_DATABASE+=[("E6","Niue")]
ITU_PREFIX_DATABASE+=[("E7","Bosnia and Herzegovina")]
ITU_PREFIX_DATABASE+=[("F","France")]
ITU_PREFIX_DATABASE+=zip(letters_range("F","A","Z"),["France"]*26)
ITU_PREFIX_DATABASE+=[("G","United Kingdom")]
ITU_PREFIX_DATABASE+=zip(letters_range("G","A","Z"),["United Kingdom"]*26)
ITU_PREFIX_DATABASE+=[("HA","Hungary")]
ITU_PREFIX_DATABASE+=[("HB","Switzerland")]
"""HB (HB0, HB3Y, HBL)	Liechtenstein (uses prefixes allocated to Switzerland)"""
ITU_PREFIX_DATABASE+=zip(letters_range("H","C","D"),["Ecuador"]*2)
ITU_PREFIX_DATABASE+=[("HE","Switzerland")]
ITU_PREFIX_DATABASE+=[("HF","Poland")]
ITU_PREFIX_DATABASE+=[("HG","Hungary")]
ITU_PREFIX_DATABASE+=[("HH","Haiti")]
ITU_PREFIX_DATABASE+=[("HI","Dominican Republic")]
ITU_PREFIX_DATABASE+=zip(letters_range("H","J","K"),["Colombia"]*2)
ITU_PREFIX_DATABASE+=[("HL","South Korea")]
ITU_PREFIX_DATABASE+=[("HM","North Korea")]
ITU_PREFIX_DATABASE+=[("HN","Iraq")]
ITU_PREFIX_DATABASE+=zip(letters_range("H","O","P"),["Panama"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("H","Q","R"),["Honduras"]*2)
ITU_PREFIX_DATABASE+=[("HS","Thailand")]
ITU_PREFIX_DATABASE+=[("HT","Nicaragua")]
ITU_PREFIX_DATABASE+=[("HU","El Salvador")]
ITU_PREFIX_DATABASE+=[("HV","Vatican City")]
ITU_PREFIX_DATABASE+=zip(letters_range("H","W","Y"),["France"]*3)
ITU_PREFIX_DATABASE+=[("HZ","Saudi Arabia")]
ITU_PREFIX_DATABASE+=[("H2","Cyprus")]
ITU_PREFIX_DATABASE+=[("H3","Panama")]
ITU_PREFIX_DATABASE+=[("H4","Solomon Islands")]
ITU_PREFIX_DATABASE+=zip(letters_range("H","6","7"),["Nicaragua"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("H","8","9"),["Panama"]*2)
ITU_PREFIX_DATABASE+=[("I","Italy")]
ITU_PREFIX_DATABASE+=zip(letters_range("I","A","Z"),["Italy"]*26)
ITU_PREFIX_DATABASE+=zip(letters_range("J","A","S"),["Japan"]*10)
ITU_PREFIX_DATABASE+=zip(letters_range("J","T","V"),["Mongolia"]*3)
ITU_PREFIX_DATABASE+=[("JY","Jordan")]
ITU_PREFIX_DATABASE+=[("JZ","Indonesia")]
ITU_PREFIX_DATABASE+=[("J2","Djibouti")]
ITU_PREFIX_DATABASE+=[("J3","Grenada")]
ITU_PREFIX_DATABASE+=[("J4","Greece")]
ITU_PREFIX_DATABASE+=[("J5","Guinea-Bissau")]
ITU_PREFIX_DATABASE+=[("J6","Saint Lucia")]
ITU_PREFIX_DATABASE+=[("J7","Dominica")]
ITU_PREFIX_DATABASE+=[("J8","Saint Vincent and the Grenadines")]
ITU_PREFIX_DATABASE+=[("K","United States")]
ITU_PREFIX_DATABASE+=zip(letters_range("K","A","Z"),["United States"]*26)
ITU_PREFIX_DATABASE+=zip(letters_range("L","A","N"),["Norway"]*13)
ITU_PREFIX_DATABASE+=zip(letters_range("L","O","W"),["Argentina"]*12)
ITU_PREFIX_DATABASE+=[("LX","Luxembourg")]
ITU_PREFIX_DATABASE+=[("LY","Lithuania")]
ITU_PREFIX_DATABASE+=[("LZ","Bulgaria")]
ITU_PREFIX_DATABASE+=zip(letters_range("L","2","9"),["Argentina"]*8)
ITU_PREFIX_DATABASE+=[("M","United Kingdom")]
ITU_PREFIX_DATABASE+=zip(letters_range("M","A","Z"),["United Kingdom"]*26)
ITU_PREFIX_DATABASE+=[("N","United States")]
ITU_PREFIX_DATABASE+=zip(letters_range("N","A","Z"),["United States"]*26)
ITU_PREFIX_DATABASE+=zip(letters_range("O","A","C"),["Peru"]*3)
ITU_PREFIX_DATABASE+=[("OD","Lebanon")]
ITU_PREFIX_DATABASE+=[("OE","Austria")]
ITU_PREFIX_DATABASE+=zip(letters_range("O","F","J"),["Finland"]*5)
ITU_PREFIX_DATABASE+=zip(letters_range("O","K","L"),["Czech Republic"]*2)
ITU_PREFIX_DATABASE+=[("OM","Slovakia")]
ITU_PREFIX_DATABASE+=zip(letters_range("O","N","T"),["Belgium"]*5)
ITU_PREFIX_DATABASE+=zip(letters_range("O","U","Z"),["Denmark"]*6)
ITU_PREFIX_DATABASE+=zip(letters_range("P","A","I"),["Netherlands"]*9)
ITU_PREFIX_DATABASE+=[("PJ","Netherlands – Former Netherlands Antilles")]
ITU_PREFIX_DATABASE+=zip(letters_range("P","K","O"),["Indonesia"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("P","P","Y"),["Brazil"]*10)
ITU_PREFIX_DATABASE+=[("PZ","Suriname")]
ITU_PREFIX_DATABASE+=[("P2","Papua New Guinea")]
ITU_PREFIX_DATABASE+=[("P3","Cyprus")]
ITU_PREFIX_DATABASE+=[("P4","Aruba")]
ITU_PREFIX_DATABASE+=zip(letters_range("P","5","9"),["North Korea"]*5)
ITU_PREFIX_DATABASE+=[("R","Russia")]
ITU_PREFIX_DATABASE+=zip(letters_range("R","A","Z"),["Russia"]*26)
ITU_PREFIX_DATABASE+=zip(letters_range("S","A","M"),["Sweden"]*13)
ITU_PREFIX_DATABASE+=zip(letters_range("S","N","R"),["Poland"]*5)
ITU_PREFIX_DATABASE+=zip(letters_range("SS","A","M"),["Egypt"]*13)
ITU_PREFIX_DATABASE+=zip(letters_range("SS","N","Z"),["Sudan"]*13)
ITU_PREFIX_DATABASE+=[("SU","Egypt")]
ITU_PREFIX_DATABASE+=zip(letters_range("S","V","Z"),["Greece"]*5)
ITU_PREFIX_DATABASE+=zip(letters_range("S","2","3"),["Bangladesh"]*2)
ITU_PREFIX_DATABASE+=[("S5","Slovenia")]
ITU_PREFIX_DATABASE+=[("S6","Singapore")]
ITU_PREFIX_DATABASE+=[("S7","Seychelles")]
ITU_PREFIX_DATABASE+=[("S8","South Africa")]
ITU_PREFIX_DATABASE+=[("S9","São Tomé and Príncipe")]
ITU_PREFIX_DATABASE+=zip(letters_range("T","A","C"),["Turkey"]*3)
ITU_PREFIX_DATABASE+=[("TD","Guatemala")]
ITU_PREFIX_DATABASE+=[("TE","Costa Rica")]
ITU_PREFIX_DATABASE+=[("TF","Iceland")]
ITU_PREFIX_DATABASE+=[("TG","Guatemala")]
ITU_PREFIX_DATABASE+=[("TH","France (and its Overseas departments/territories)")]
ITU_PREFIX_DATABASE+=[("TI","Costa Rica")]
ITU_PREFIX_DATABASE+=[("TJ","Cameroon")]
ITU_PREFIX_DATABASE+=[("TK","France (and its Overseas departments/territories)")]
ITU_PREFIX_DATABASE+=[("TL","Central African Republic")]
ITU_PREFIX_DATABASE+=[("TM","France (and its Overseas departments/territories)")]
ITU_PREFIX_DATABASE+=[("TN","Republic of the Congo")]
ITU_PREFIX_DATABASE+=zip(letters_range("T","O","Q"),["France (and its Overseas departments/territories)"]*3)
ITU_PREFIX_DATABASE+=[("TR","Gabon")]
ITU_PREFIX_DATABASE+=[("TS","Tunisia")]
ITU_PREFIX_DATABASE+=[("TT","Chad")]
ITU_PREFIX_DATABASE+=[("TU","Ivory Coast")]
ITU_PREFIX_DATABASE+=zip(letters_range("T","V","X"),["France (and its Overseas departments/territories)"]*3)
ITU_PREFIX_DATABASE+=[("TY","Benin")]
ITU_PREFIX_DATABASE+=[("TZ","Mali")]
ITU_PREFIX_DATABASE+=[("T2","Tuvalu")]
ITU_PREFIX_DATABASE+=[("T3","Kiribati")]
ITU_PREFIX_DATABASE+=[("T4","Cuba")]
ITU_PREFIX_DATABASE+=[("T5","Somalia")]
ITU_PREFIX_DATABASE+=[("T6","Afghanistan")]
ITU_PREFIX_DATABASE+=[("T7","San Marino")]
ITU_PREFIX_DATABASE+=[("T8","Palau")]
ITU_PREFIX_DATABASE+=zip(letters_range("U","A","I"),["Russia"]*9)
ITU_PREFIX_DATABASE+=zip(letters_range("U","J","M"),["Uzbekistan"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("U","N","Q"),["Kazakhstan"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("U","R","Z"),["Ukraine"]*6)
ITU_PREFIX_DATABASE+=zip(letters_range("V","A","G"),["Canada"]*7)
ITU_PREFIX_DATABASE+=zip(letters_range("V","H","N"),["Australia"]*7)
ITU_PREFIX_DATABASE+=[("VO","Canada (formerly Dominion of Newfoundland)")]
ITU_PREFIX_DATABASE+=zip(letters_range("V","P","Q"),["United Kingdom"]*2)
ITU_PREFIX_DATABASE+=[("VR","Hong Kong (Special administrative regions of China)")]
ITU_PREFIX_DATABASE+=[("VS","United Kingdom")]
ITU_PREFIX_DATABASE+=zip(letters_range("V","T","W"),["India"]*3)
ITU_PREFIX_DATABASE+=zip(letters_range("V","X","Y"),["Canada"]*2)
ITU_PREFIX_DATABASE+=[("VZ","Australia")]
ITU_PREFIX_DATABASE+=[("V2","Antigua and Barbuda")]
ITU_PREFIX_DATABASE+=[("V3","Belize")]
ITU_PREFIX_DATABASE+=[("V4","Saint Kitts and Nevis")]
ITU_PREFIX_DATABASE+=[("V5","Namibia")]
ITU_PREFIX_DATABASE+=[("V6","Federated States of Micronesia")]
ITU_PREFIX_DATABASE+=[("V7","Marshall Islands")]
ITU_PREFIX_DATABASE+=[("V8","Brunei")]
ITU_PREFIX_DATABASE+=[("W","United States")]
ITU_PREFIX_DATABASE+=zip(letters_range("W","A","Z"),["United States"]*26)
ITU_PREFIX_DATABASE+=zip(letters_range("X","A","I"),["Mexico"]*9)
ITU_PREFIX_DATABASE+=zip(letters_range("X","J","O"),["Canada"]*6)
ITU_PREFIX_DATABASE+=[("XP","Denmark")]
ITU_PREFIX_DATABASE+=zip(letters_range("X","Q","R"),["Chile"]*2)
ITU_PREFIX_DATABASE+=[("XS","China")]
ITU_PREFIX_DATABASE+=[("XT","Burkina Faso")]
ITU_PREFIX_DATABASE+=[("XU","Cambodia")]
ITU_PREFIX_DATABASE+=[("XV","Vietnam")]
ITU_PREFIX_DATABASE+=[("XW","Laos")]
ITU_PREFIX_DATABASE+=[("XX","Macao (Special administrative regions of China)")]
ITU_PREFIX_DATABASE+=zip(letters_range("X","Y","Z"),["Burma"]*3)
ITU_PREFIX_DATABASE+=[("YA","Afghanistan")]
ITU_PREFIX_DATABASE+=zip(letters_range("Y","B","H"),["Indonesia"]*8)
ITU_PREFIX_DATABASE+=[("YI","Iraq")]
ITU_PREFIX_DATABASE+=[("YJ","Vanuatu")]
ITU_PREFIX_DATABASE+=[("YK","Syria")]
ITU_PREFIX_DATABASE+=[("YL","Latvia")]
ITU_PREFIX_DATABASE+=[("YM","Turkey")]
ITU_PREFIX_DATABASE+=[("YN","Nicaragua")]
ITU_PREFIX_DATABASE+=zip(letters_range("Y","O","R"),["Romania"]*4)
ITU_PREFIX_DATABASE+=[("YS","El Salvador")]
ITU_PREFIX_DATABASE+=zip(letters_range("Y","T","U"),["Serbia"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("Y","V","Y"),["Venezuela"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("Y","2","9"),["Germany"]*8)
ITU_PREFIX_DATABASE+=[("ZA","Albania")]
ITU_PREFIX_DATABASE+=zip(letters_range("Z","B","J"),["United Kingdom"]*10)
ITU_PREFIX_DATABASE+=zip(letters_range("Z","K","M"),["New Zealand"]*3)
ITU_PREFIX_DATABASE+=zip(letters_range("Z","N","O"),["United Kingdom"]*2)
ITU_PREFIX_DATABASE+=[("ZP","Paraguay")]
ITU_PREFIX_DATABASE+=[("ZQ","United Kingdom")]
ITU_PREFIX_DATABASE+=zip(letters_range("Z","R","U"),["South Africa"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("Z","V","Z"),["Brazil"]*6)
ITU_PREFIX_DATABASE+=[("Z2","Zimbabwe")]
ITU_PREFIX_DATABASE+=[("Z3","North Macedonia")]
ITU_PREFIX_DATABASE+=[("Z8","South Sudan")]
ITU_PREFIX_DATABASE+=[("2","United Kingdom")]
ITU_PREFIX_DATABASE+=zip(letters_range("2","A","Z"),["United Kingdom"]*26)
ITU_PREFIX_DATABASE+=[("3A","Monaco")]
ITU_PREFIX_DATABASE+=zip(letters_range("3","B","D"),["Mauritius"]*3)
ITU_PREFIX_DATABASE+=zip(letters_range("3","D","M"),["Eswatini"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("3","D","Z"),["Fiji"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("3","E","F"),["Panama"]*2)
ITU_PREFIX_DATABASE+=[("3G","Chile")]
ITU_PREFIX_DATABASE+=zip(letters_range("3","H","U"),["China"]*6)
ITU_PREFIX_DATABASE+=[("3V","Tunisia")]
ITU_PREFIX_DATABASE+=[("3W","Vietnam")]
ITU_PREFIX_DATABASE+=[("3X","Guinea")]
ITU_PREFIX_DATABASE+=[("3Y","Norway")]
ITU_PREFIX_DATABASE+=[("3Z","Poland")]
ITU_PREFIX_DATABASE+=zip(letters_range("4","A","C"),["Mexico"]*3)
ITU_PREFIX_DATABASE+=zip(letters_range("4","D","I"),["Philippines"]*6)
ITU_PREFIX_DATABASE+=zip(letters_range("4","J","K"),["Azerbaijan"]*2)
ITU_PREFIX_DATABASE+=[("4L","Georgia")]
ITU_PREFIX_DATABASE+=[("4M","Venezuela")]
ITU_PREFIX_DATABASE+=[("4O","Montenegro")]
ITU_PREFIX_DATABASE+=zip(letters_range("4","P","S"),["Sri Lanka"]*4)
ITU_PREFIX_DATABASE+=[("4T","Peru")]
ITU_PREFIX_DATABASE+=[("4U","United Nations")]
ITU_PREFIX_DATABASE+=[("4V","Haiti")]
ITU_PREFIX_DATABASE+=[("4W","Timor-Leste")]
ITU_PREFIX_DATABASE+=[("4X","Israel")]
ITU_PREFIX_DATABASE+=[("4Y","International Civil Aviation Organization")]
ITU_PREFIX_DATABASE+=[("4Z","Israel")]
ITU_PREFIX_DATABASE+=[("5A","Libya")]
ITU_PREFIX_DATABASE+=[("5B","Cyprus")]
ITU_PREFIX_DATABASE+=zip(letters_range("5","C","G"),["Morocco"]*5)
ITU_PREFIX_DATABASE+=zip(letters_range("5","H","I"),["Tanzania"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("5","J","K"),["Colombia"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("5","L","M"),["Liberia"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("5","N","O"),["Nigeria"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("5","P","Q"),["Denmark"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("5","R","S"),["Madagascar"]*2)
ITU_PREFIX_DATABASE+=[("5T","Mauritania")]
ITU_PREFIX_DATABASE+=[("5U","Niger")]
ITU_PREFIX_DATABASE+=[("5V","Togo")]
ITU_PREFIX_DATABASE+=[("5W","Western Samoa")]
ITU_PREFIX_DATABASE+=[("5X","Uganda")]
ITU_PREFIX_DATABASE+=zip(letters_range("5","Y","Z"),["Kenya"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("6","A","B"),["Egypt"]*2)
ITU_PREFIX_DATABASE+=[("6C","Syria")]
ITU_PREFIX_DATABASE+=zip(letters_range("6","D","J"),["Mexico"]*9)
ITU_PREFIX_DATABASE+=zip(letters_range("6","K","N"),["South Korea"]*4)
ITU_PREFIX_DATABASE+=[("6O","Somalia")]
ITU_PREFIX_DATABASE+=zip(letters_range("6","P","S"),["Pakistan"]*4)
ITU_PREFIX_DATABASE+=zip(letters_range("6","T","U"),["Sudan"]*2)
ITU_PREFIX_DATABASE+=zip(letters_range("6","V","W"),["Senegal"]*2)
ITU_PREFIX_DATABASE+=[("6X","Madagascar")]
ITU_PREFIX_DATABASE+=[("6Y","Jamaica")]
ITU_PREFIX_DATABASE+=[("6Z","Liberia")]
ITU_PREFIX_DATABASE+=zip(letters_range("7","A","I"),["Indonesia"]*9)
ITU_PREFIX_DATABASE+=zip(letters_range("7","J","N"),["Japan"]*5)
ITU_PREFIX_DATABASE+=[("7O","Yemen")]
ITU_PREFIX_DATABASE+=[("7P","Lesotho")]
ITU_PREFIX_DATABASE+=[("7Q","Malawi")]
ITU_PREFIX_DATABASE+=[("7R","Algeria")]
ITU_PREFIX_DATABASE+=[("7S","Sweden")]
ITU_PREFIX_DATABASE+=zip(letters_range("7","T","Y"),["Algeria"]*5)
ITU_PREFIX_DATABASE+=[("7Z","Saudi Arabia")]
ITU_PREFIX_DATABASE+=zip(letters_range("8","A","I"),["Indonesia"]*9)
ITU_PREFIX_DATABASE+=zip(letters_range("8","J","N"),["Japan"]*5)
ITU_PREFIX_DATABASE+=[("8O","Botswana")]
ITU_PREFIX_DATABASE+=[("8P","Barbados")]
ITU_PREFIX_DATABASE+=[("8Q","Maldives")]
ITU_PREFIX_DATABASE+=[("8R","Guyana")]
ITU_PREFIX_DATABASE+=[("8S","Sweden")]
ITU_PREFIX_DATABASE+=zip(letters_range("8","T","Y"),["India"]*5)
ITU_PREFIX_DATABASE+=[("8Z","Saudi Arabia")]
ITU_PREFIX_DATABASE+=[("9A","Croatia")]
ITU_PREFIX_DATABASE+=zip(letters_range("9","B","D"),["Iran"]*3) 
ITU_PREFIX_DATABASE+=zip(letters_range("9","E","F"),["Ethiopia"]*2)
ITU_PREFIX_DATABASE+=[("9G","Ghana")]
ITU_PREFIX_DATABASE+=[("9H","Malta")]
ITU_PREFIX_DATABASE+=zip(letters_range("9","I","J"),["Zambia"]*2)
ITU_PREFIX_DATABASE+=[("9K","Kuwait")]
ITU_PREFIX_DATABASE+=[("9L","Sierra Leone")]
ITU_PREFIX_DATABASE+=[("9M","Malaysia")]
ITU_PREFIX_DATABASE+=[("9N","Nepal")]
ITU_PREFIX_DATABASE+=zip(letters_range("9","O","T"),["Democratic Republic of the Congo"]*6)
ITU_PREFIX_DATABASE+=[("9U","Burundi")]
ITU_PREFIX_DATABASE+=[("9V","Singapore")]
ITU_PREFIX_DATABASE+=[("9W","Malaysia")]
ITU_PREFIX_DATABASE+=[("9X","Rwanda")]
ITU_PREFIX_DATABASE+=zip(letters_range("9","Y","Z"),["Trinidad and Tobago"]*2)
