# Fase 1: conceptos clave, estructuras de control, memoria y tiempo

Este documento resume lo esencial de la primera etapa del [programa de aprendizaje](../../README.md#objetivos-por-fase) y conecta cada idea con **coste de memoria** (modelo mental de CPython) y **coste en tiempo** (complejidad y factores constantes).

---

## 1. Variables y nombres

En Python, un **nombre** (`x`, `total`, `nombre_usuario`) es una **referencia** a un objeto en memoria. La asignación (`x = 42`) enlaza el nombre con el objeto; no “reserva una caja tipada” como en C.

- **Implicación de memoria:** el nombre en el marco local ocupa poco; el “peso” real está en el **objeto** al que apunta.
- **Implicación de tiempo:** leer o reasignar una variable local es muy barato frente a operaciones de E/S o algoritmos con bucles grandes.

---

## 2. Tipos de datos fundamentales

### 2.1 Enteros (`int`)

CPython representa enteros como objetos de tamaño variable: cuantos más dígitos tengas en valor absoluto, más memoria suele ocupar la representación interna.

| Idea | Memoria (orden de magnitud) | Notas |
|------|-----------------------------|--------|
| Pequeños enteros `-5…256` | A menudo **reutilizados** (caché interna) | Múltiples nombres pueden apuntar al mismo objeto |
| `int` típico | decenas de bytes de encabezado + dígitos | `sys.getsizeof` muestra solo el objeto `int` |
| Entero enorme | crece con el número de “limbs” / dígitos | Tiempo de operaciones aritméticas crece con el tamaño del entero |

### 2.2 Flotantes (`float`)

En CPython suele ser un **IEEE 754 binary64** envuelto en un objeto PyObject: unas pocas decenas de bytes totales con `sys.getsizeof`, no solo 8 bytes “puros”.

### 2.3 Booleanos (`bool`)

Subclase de `int`. Los valores `True` y `False` son **singletons**: un solo objeto en memoria para cada uno en un proceso.

### 2.4 Ninguno (`None`)

También es un **singleton**: siempre el mismo objeto `None`.

### 2.5 Cadenas (`str`)

- Objetos **inmutables**: operaciones que “modifican” crean nuevas cadenas.
- **Internado** limitado: cadenas idénticas pueden o no compartir un único objeto según contexto; no dependas de ello para la lógica del programa.
- Memoria: encabezado del objeto + almacenamiento de caracteres (UTF-8 interno en CPython 3.3+ según representación compacta). Una cadena corta y una larga no escalan linealmente por un solo byte por carácter visible en `getsizeof` por optimizaciones internas; mide con `sys.getsizeof` en tu versión.

### 2.6 Objetos contenedores ligeros en Fase 1

Aunque las listas y diccionarios se profundizan en la Fase 2, en sintaxis básica ya aparecen literales:

| Tipo | `sys.getsizeof` | Cuidado |
|------|-----------------|--------|
| `list` | Objeto lista + punteros a elementos | No incluye tamaño de los elementos referenciados |
| `dict` | Tabla hash + entradas | Mismo matiz: es el “shell”, no el árbol completo |

Para **memoria total aproximada** de un grafo de objetos necesitas herramientas más avanzadas (por ejemplo `pympler`, `tracemalloc`) más adelante.

---

## 3. Operadores

### 3.1 Aritméticos y de comparación

Evalúan a nuevos objetos (o reutilizan internados en casos muy concretos). El coste temporal depende del tipo: sumar dos `int` grandes no es O(1).

### 3.2 Lógicos (`and`, `or`, `not`)

- **Cortocircuito:** `a and b` no evalúa `b` si `a` es falsy; `a or b` no evalúa `b` si `a` es truthy.
- **Tiempo:** puede ahorrar trabajo; **memoria:** típicamente irrelevante frente al resto del programa.

---

## 4. Estructuras de control: semántica y coste

### 4.1 Condicionales `if` / `elif` / `else`

- **Semántica:** se evalúa la condición de la primera rama verdadera y se ejecuta ese bloque; si ninguna coincide y hay `else`, se ejecuta `else`.
- **Tiempo (notación asintótica):** una sola cadena `if/elif` es O(k) en el peor caso respecto al **número de ramas** k si cada condición es O(1)—es decir, recorres hasta la primera cierta. No confundir con O(1) “mágico”: las condiciones pueden ser caras (`x in lista_grande`).
- **Memoria:** suele ser despreciable (marcos de pila locales); el coste viene del trabajo **dentro** de cada rama.

### 4.2 Bucle `for`

- En Python, `for x in iterable:` delega en el **protocolo de iteración** (`__iter__` / `__next__`).
- **Tiempo:** para `n` iteraciones sobre un iterable con paso O(1) por elemento, el bucle es **O(n)** más el coste de crear/recorrer el iterable (por ejemplo `range(n)` es eficiente en espacio).
- **Memoria:** `range` no materializa la lista completa; iterar sobre una **lista** de longitud `n` ya tiene esa lista en memoria.

### 4.3 Bucle `while`

- Repite mientras la condición sea verdadera.
- **Tiempo:** depende del número de vueltas y del coste de la condición y del cuerpo; riesgo de **bucle infinito** si la condición o el estado no avanzan.
- **Frente a `for`:** `while` suele tener más **overhead por vuelta** en microbenchmarks (incremento manual, comprobación en Python puro), pero la diferencia es irrelevante si el cuerpo del bucle hace trabajo real.

### 4.4 Control de flujo auxiliar

- `break` / `continue`: alteran el flujo dentro del bucle actual; coste O(1) respecto al tamaño del iterable.
- Bucle `else` en `for`/`while`: se ejecuta si el bucle **termina sin** `break`. Útil y a veces olvidado; no cambia el orden de magnitud del tiempo.

---

## 5. Métricas: cómo medir en tu máquina

### 5.1 Memoria visible con `sys.getsizeof`

```python
import sys

print(sys.getsizeof(42))
print(sys.getsizeof("hola"))
```

Interpretación: devuelve el tamaño **del objeto que pasas**, no siempre la memoria de todo lo que cuelga de él (listas, diccionarios, instancias).

### 5.2 Tiempo con `timeit`

Mide intervalos muy pequeños con calentamiento y repetición; ideal para comparar **micro**diferencias entre patrones de bucles o condiciones.

En este repositorio puedes ejecutar:

```bash
python phases/01-fundamentos-y-sintaxis/mediciones_fase1.py
```

### 5.3 Ejemplo de salida (referencia, no garantizada entre versiones)

Medido en una ejecución con **Python 3.14** en Windows 64-bit (valores orientativos):

**`sys.getsizeof` (bytes, objeto solo)**

| Objeto | Bytes aprox. |
|--------|----------------|
| `True` / `False` | 28 |
| `None` | 16 |
| `0`, `1`, `42` | 28 |
| `2**30` | 32 |
| `10**100` | 72 |
| `3.14` | 24 |
| `""` | 41 |
| `"hola"` | 45 |
| `"x" * 1000` | 1041 |
| `[]` | 56 |
| `[1, 2, 3]` | 88 |
| `{}` | 64 |
| `{1: 2}` | 224 |

**`timeit` (segundos por ejecución del fragmento, ~5e5 repeticiones)**

| Fragmento | Orden de magnitud |
|-----------|-------------------|
| `for _ in range(10): pass` | ~1.1e-7 s por bucle de 10 vueltas |
| `while` 10 incrementos | ~2.4e-7 s por bucle de 10 vueltas |
| `if True: pass` / `if False: pass` | ~6e-9 s |

La comparación `for` vs `while` aquí refleja sobre todo **overhead del protocolo** del bucle, no el trabajo útil dentro del cuerpo. En programas reales, **optimiza el algoritmo y las estructuras**, no el tipo de bucle.

---

## 6. Implicaciones prácticas (Fase 1)

1. **Priorizar la claridad** (`for` sobre un iterable bien definido) frente a microoptimizar el tipo de bucle.
2. **No confundir** referencia y copia: asignar comparte objeto; mutar afecta a todas las referencias si el objeto es mutable (listas y diccionarios, al estudiarlos en profundidad).
3. **Mide** cuando el rendimiento importe: intuiciones sobre “ahorro de memoria” sin números suelen equivocarse en CPython.

---

## 7. Hitos sugeridos (Fase 1)

- «Hola mundo» y scripts mínimos por consola.
- Calculadora por terminal o juego de adivinanzas.
- Resolver errores de **indentación** y de sintaxis de forma sistemática.

Al pasar a la Fase 2, el mismo enfoque (objeto + referencia + complejidad) se extiende a estructuras más ricas y a funciones.
