#Hola Mundo
print("Hola mundo")

#Variables

my_string = 'Esto es una cadena de texto'
my_string = "Mutando cadena de texto"
print(type(my_string))

my_string= 6 #Tipado dinamico
my_string= "Hola mundo"
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

#Listas desordenadas

my_set = {my_string, my_int, my_float, my_bool, my_bool}
print(my_set) #Imprime de manera desordenada

#Tuplas

my_tuple = (my_string, my_int, my_float, my_bool, my_bool)
print(my_tuple) #No se puede modificar como los diccionarios, listas, sets

#Condicional If/else

if my_int == 10 or my_bool:
    print("El valor es 10")
elif my_int == 12:
    print("El valor es 12")
else:
    print("El valor no es 10, ni 12")

#Ciclo for in
for my_item in my_list:
    print(my_item)
for my_item in range(10):
    print(my_item)
for my_item in my_dict:
    print(my_item)
for my_item in my_set:
    print(my_item)
for my_item in my_tuple:
    print(my_item)

#Funciones
def my_function():
    print("Esto es una funcion")

my_function()

def my_function_with_return(param):
    return 10 + param
my_return = my_function_with_return(4)
print(my_return)

#Clases

class MyClass:
    def __init__(self, my_name):
        self.my_name = my_name
    
    def print_my_name(self):
        print(self.my_name)

my_class = MyClass("Jose")
my_class.print_my_name()
my_class.my_name = "JoseManuel"
my_class.print_my_name()