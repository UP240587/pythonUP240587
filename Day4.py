
cadena1 = "Treinta"
cadena2 = "Días"
cadena3 = "De"
cadena4 = "Python"

resultado1 = cadena1 + " " + cadena2 + " " + cadena3.lower() + " " + cadena4
print(resultado1)  


cadena5 = "Codificación"
cadena6 = "Para"
cadena7 = "Todos"

resultado2 = cadena5 + " " + cadena6 + " " + cadena7
print(resultado2)
empresa = "codificaion para todos"
print(empresa)
print(len(empresa))
print(empresa.upper()) 
print(empresa.lower()) 
print(empresa.capitalize()) 
print(empresa.title())      
print(empresa.swapcase())    
palabras = empresa.split()         
sin_primera = " ".join(palabras[1:])
print(sin_primera)
print("Codificación" in empresa)     
print(empresa.find("Codificación"))  
print(empresa.index("Codificación")) 
cadena2 = "Coding For All"
nueva_cadena = cadena2.replace("Coding", "Python")
print(nueva_cadena)
frase1 = "Python for Everyone"
frase1_modificada = frase1.replace("Everyone", "All")
print(frase1_modificada)
frase2 = "Coding For All"
dividida_espacio = frase2.split()
print(dividida_espacio)
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
divididas_coma = empresas.split(", ")
print(divididas_coma)
print(frase2[0]) 
ultimo_indice = len(frase2) - 1
print(ultimo_indice)
print(frase2[ultimo_indice])  
print(frase2[10])
palabras1 = "Python For Everyone".split()
acronimo1 = "".join([p[0] for p in palabras1])
print(acronimo1)
palabras2 = "Coding For All".split()
acronimo2 = "".join([p[0] for p in palabras2])
print(acronimo2)
print(frase2.index("C")) 
print(frase2.index("F"))
frase3 = "Coding For All People"
print(frase3.rfind("l")) 
frase3 = "No se puede terminar una oración con because porque es una conjunción"
because = frase3.find("because")
print(because) 
frase4 = "No se puede terminar una oración con because porque es una conjunción"
because2 = frase4.rindex("because")
print(because2)
palabra_a_eliminar = "because"
palabras = frase3, frase4.split()
palabras_filtradas = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
nueva_oracion = " ".join(palabras_filtradas)
print(nueva_oracion)
cadena = "Coding For All"
print("¿Empieza con 'Coding'?:", cadena.startswith("Coding"))  
print("¿Termina con 'coding'?:", cadena.endswith("coding"))  
cadena_con_espacios = "   Coding For All   "
cadena_sin_espacios = cadena_con_espacios.strip()
print("Sin espacios laterales:", cadena_sin_espacios)
print("¿'30DaysOfPython' es identificador válido?:", "30DaysOfPython".isidentifier())       
print("¿'thirteen_days_of_python' es identificador válido?:", "thirteen_days_of_python".isidentifier())  
frameworks = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
unidos = '# '.join(frameworks)
print("Librerías unidas con '# ':", unidos)
texto = "Python es un lenguaje de programación.\nEs muy popular.\nSirve para muchos propósitos."
print("Texto con saltos de línea:")
print(texto)
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}") 
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

