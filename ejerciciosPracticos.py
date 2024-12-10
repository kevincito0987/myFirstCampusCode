#Ejercicio 1 del curso de python de soy Dalto

#Parte 1: Diferencia de porcentaje entre el curso actual y: -el más rápido de otros cursos. -el más lento de otros cursos. - el promedio de los cursos.


min_curso = 2.5 
max_curso = 7
promedio_curso = 4
curso_actual = 1.5

#Haciendo la diferencia.

if curso_actual < min_curso and curso_actual < min_curso and curso_actual < promedio_curso :
    print("El curso actual es el más rápido")
elif min_curso <= curso_actual and min_curso < max_curso and min_curso <= promedio_curso :
    print("El curso de promedio minimo se encuentra entre el promedio y el curso de dalto")
else : print("Este curso es el más lento de todos")

#Parte 2: Calculando el material basura de otros cursos.

basura_cursos = promedio_curso - curso_actual

print(f"La basura que hay en otros cursos es de: {basura_cursos} horas.")

print("Opino que ver un curso con este profe nos hace la nasa xdxdxdxdxddd.")