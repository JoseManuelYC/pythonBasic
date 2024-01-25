#Hola Mundo
print("Hola mundo")

#Variables

my_string = 'Esto es una cadena de texto'
my_string = "Mutando cadena de texto"
print(type(my_string))

my_string= 6 #Tipado dinamico
print(type(my_string))

my_int = 5
my_int = my_int + 5
my_float= 2.5
print(my_int + my_float)

my_bool = True
my_false = False

#Concatenar
print("El valor de mi entero es "+ str(my_int) + " Y el de mi bool es " + str(my_bool))
print(f"El valor de mi entero es {my_int} Y el de mi bool es {my_bool}")

#Listas

my_list = [my_int, my_string, my_bool]

#Diccionarios

my_dict = {"string": my_string, "int": my_int, "float": my_float, "jose": "joseM"}
print(my_dict["jose"]) #Imprime el valor de la clave