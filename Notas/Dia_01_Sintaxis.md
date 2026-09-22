# Sintaxis de Python.
Aprender la sintaxis de Python es tan facil como la cantidad e vocabulario que tenga en ingles, la mayoria de palabras usadas en el lenguaje vinen diractamente del ingles, por lo que lo hace mas facil de entender.

Aunque el ingles hace parte escencial de Python tambien tiene otras reglas importantes:

### 1. La indentacion.
Es unao e los aspectos mas relevantes del lenguaje, en otros leguages de programacion como Java se hace uso de corchetes{} para establecer los bloques de codigo, en python eso no es necesario ya que con espacion/tabulaciones se definen esos bloques de codigo.

por ejemplo:

```
if True:
    print("Este bloque esta indentado y determina que este print pertenece al if")
    print("Todo lo que pertenezca a if debe tener el mismo nivel de indentacion")
```

### 2. Fin de línea.
En otros lenguajes puede ser obligatorio el uso de ; para declarar el fin de una linea de codigo, pero en python esto no es necsario ya que cada entruccion va en una unica linea.

### 3. Comentarios.
para dejar un comentario en cualquier línea de codigo es necesario usar el simbolo (#), si quiero un comentario multiliana se puede usar triple comilla (''') o (""").

### 4. Variables.
Para las variables es necesario tener mucho cuidado con las mayusculas pues una variable (x) no es igual que (X).

Se puede usar letras y numeros y (_) para una variable pero esta no puede comenzar con un numero.

### 5. Dos puntos.
Los dos puntos (:) se usan para indicar un bloque e estructura como if, for, while, def, class, try etc.

### 6. Paréntesis, corchetes y llaves.
() → funciones, tuplas
[] → listas, indexación
{} → diccionarios, sets

### 7. Stings
Se escriben entre comillas simples o dobles ('') o ("")

### 8. Tipado dinamico.
No es necesario definir el tipo de dato que estamos usando, python reconoce utomaticamete un str, int, double, char etc.

### 9. Operadores especiales
** → Potencia.
// → Division entera (quita los decimales)
%  → Modulo.
*= → Multiplica automacicamente por la variable.
+= → Suma automacicamente por la variable.
-= → Resta automacicamente por la variable.
/= → Divide automacicamente por la variable.

### 10. Sensibilidad a mayusculas.
True, False, None van con mayúscula inicial (son palabras reservadas).
import, def, class, if, for, etc. van siempre en minúscula.

### Otros.
return  - Solamemnte puedeser usado dentro de una funcion.
f - Se usa para concatenar variales.
input() - Le puedes pedir al usuario que introduzaca un tipo de dato
