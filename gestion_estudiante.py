print("=== REGISTRO DE ESTUDIANTE ===")

# Solicitar datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
carrera = input("Ingrese su carrera: ")
semestre = int(input("Ingrese su semestre: "))

# Estado de matrícula
matriculado = True

#Solicitar la primera nota
nota1 = float(input("ingrese la nota 1: "))
while nota1 < 0 or nota1 > 20:
    input("La nota debe estar entre 0  20")
    nota1 = float(input("Ingrese la nota 1: "))

    #Solicitar la segunda  nota
nota2 = float(input("ingrese la nota 2: "))
while nota2 < 0 or nota2 > 20:
    input("La nota debe estar entre 0  20")
    nota2 = float(input("Ingrese la nota 2: "))

#Solicitar la tercera  nota
nota3 = float(input("ingrese la nota 3: "))
while nota3 < 0 or nota3 > 20:
    input("La nota debe estar entre 0  20")
    nota3 = float(input("Ingrese la nota 3: "))

#Creamos lista de notas
notas = [nota1, nota2, nota3]

#Acumuladores  contadores
suma = 0
cursos_aprobados = 0 
cursos_desaprobados = 0

#Procesar notas
for nota in notas:
    suma = suma + nota
    if nota >=13:
        cursos_aprobados = cursos_aprobados + 1
    else:
        cursos_desaprobados = cursos_desaprobados + 1

# Calcular el promedio
promedio = suma / len(notas)

#clasificar al estudiante
if promedio >= 17:
    estado = "Puede acceder a la beca en URUSAYHUA"
else:
    estado = "Tiene que pagar su matricula completa"

# Cursos
cursos = [
    "Herramientas de Desarrollo de Software",
    "Base de Datos",
    "Redes"
]

# Mostrar datos
print("\n=== DATOS DEL ESTUDIANTE ===")
print("Nombre:", nombre)
print("Carrera:", carrera)
print("Semestre:", semestre)

print(" \nNotas:")

for i in range(len(notas)):
 print("Nota", i+1, ":",notas[i])

print("\nPromedio:", round(promedio, 2))
print("Notas aprobadas:", cursos_aprobados)
print("Notas desaprobadas.", cursos_desaprobados)
print("Estado:", estado)