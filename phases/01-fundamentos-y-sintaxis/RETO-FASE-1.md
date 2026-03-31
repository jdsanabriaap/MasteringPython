# Reto Fase 1 — «Liga de la suma oculta»

Implementa **un único programa en consola** que integre **todo** lo trabajado en este módulo: variables y referencias, tipos básicos (`str`, `int`, `float`, `bool`), operadores aritméticos, de comparación y lógicos (incluido cortocircuito), y estructuras `if` / `elif` / `else`, `for` y `while`.

Conviene guardar la solución en un archivo dedicado (por ejemplo `liga_suma_oculta.py` o `liga-suma-oculta.py`) en esta carpeta o fuera del árbol versionado si se prefiere no publicar respuestas.

---

## Historia mínima

En cada **ronda** el programa elige **dos números enteros secretos** entre `1` y un tope `M` que depende de la dificultad. El jugador **no** ve esos números ni ve su **suma** al empezar.

El jugador **propone un entero** como suma supuesta. Tras cada propuesta incorrecta, el programa responde con una **pista comparativa** (mediante `if` / `elif` / `else`), por ejemplo:

- la suma secreta es **mayor** que lo que escribió, o  
- es **menor**, o  
- **ha acertado** (fin de la ronda con éxito).

Así el reto deja de ser trivial: hace falta acotar y afinar, como en el clásico «mayor / menor», pero el número buscado es la **suma** de dos desconocidos. Rango útil de búsqueda: como cada secreto está entre `1` y `M`, la suma está siempre entre **`2` y `2*M`** (opcional: mostrar ese rango al inicio de la ronda como ayuda).

Ejemplo: secretos `4` y `11` → suma real `15`. Si el jugador propone `10`, el programa dice que la suma es **mayor**; si propone `20`, que es **menor**; si propone `15`, gana la ronda. **Prohibido** imprimir la suma real ni los secretos **hasta** que termine la ronda (victoria o agotar intentos); al final puede mostrarse el desenlace revelando esos valores.

---

## Requisitos funcionales

1. **Bienvenida**  
   Solicitar el **nombre** (`str`) y comprobar que no esté vacío ni sea solo espacios. Si no es válido, repetir la petición (con un bucle).

2. **Menú principal** (debe repetirse hasta salir)  
   Al menos estas opciones (se pueden añadir más):
   - **Jugar una partida** (varias rondas seguidas).
   - **Ver estadísticas** (lectura solamente).
   - **Modo entrenador** (opcional pero recomendado: mostrar una medición con `sys.getsizeof` sobre una cadena construida con el nombre y un mensaje; ver apartado *Checklist técnico*).
   - **Salir**.

3. **Partida**  
   - Solicitar **dificultad** con al menos **tres** ramas distintas (`if` / `elif` / `elif` o más), por ejemplo:
     - Fácil: cada secreto en `1 … 10`, máximo **5** intentos por ronda.
     - Media: `1 … 25`, **7** intentos.
     - Difícil: `1 … 50`, **10** intentos.  
     Los números concretos pueden variar si documentas la tabla en un comentario al inicio del archivo.
   - Preguntar cuántas **rondas** se jugarán (entero `≥ 1`) y validar la entrada.
   - En **cada ronda**:
     - Generar dos secretos con **`random.randint(1, M)`** (importar `random` al inicio).
     - Calcular la **suma secreta** en una variable; **no** mostrarla mientras la ronda sigue en juego.
     - Opcional recomendado: al empezar la ronda, mostrar solo el **rango posible de sumas** (`2` … `2*M`), nunca el valor exacto.
     - En cada intento, el jugador propone un entero (supuesta suma). Si no coincide, informar si la suma real es **mayor** o **menor** que la propuesta. Si coincide, la ronda se gana.
     - Gestionar intentos hasta acertar o agotar el máximo. Debe haber al menos un **`while`** cuya condición dependa de si quedan intentos y aún no se ha acertado.
   - Al terminar la partida, actualizar estadísticas globales (siguiente apartado).

4. **Estadísticas** (variables persistentes **mientras corra el programa**)  
   Registrar al menos:
   - Partidas jugadas (`int`).
   - Rondas ganadas y rondas perdidas (`int`; una ronda se pierde si se acaban los intentos sin acertar).
   - **Promedio de intentos** por ronda jugada (`float`). Si aún no hubo rondas, mostrar `0.0` o un mensaje claro sin dividir por cero.

5. **Validación de entradas numéricas**  
   Ante texto no numérico al pedir números: mensaje claro y **reintento** (otro bucle). `try` / `except` es opcional según el nivel alcanzado; sin ellos, conviene validar con métodos de cadena o comprobaciones — siempre **sin derribar** el menú principal.

   Sin `try`/`except`, una forma habitual en Fase 1 es leer `input()` y, en bucle, comprobar carácter a carácter o usar `.isdigit()` cuando aplique (tener en cuenta el signo `-` si se admiten negativos).

---

## Checklist técnico (lo que debe aparecer en el código)

Conviene repasar cada ítem **en el mismo programa**:

| Tema del módulo | Qué debe demostrarse |
|-----------------|---------------------|
| Variables | Varios nombres reasignados y usados a lo largo del flujo (nombre, contadores, secretos, suma, etc.). |
| `str` | Nombre, menú, mensajes; posible construcción de mensajes con concatenación o f-strings. |
| `int` | Contadores, límites, intentos, rondas, rangos de aleatorio. |
| `float` | Al menos un **promedio** calculado con división real (por ejemplo `total_intentos / rondas_jugadas` o equivalente coherente). |
| `bool` | Al menos una variable booleana explícita (p. ej. `acertado`, `salir`, `entrada_ok`) usosa en condiciones. |
| `None` | Opcional: usar `ultimo_error = None` o comprobar `if x is None` si encaja en el diseño. |
| Operadores aritméticos | Suma de secretos, medias, incrementos. |
| Operadores de comparación | Límites, fin de intentos, validación de rangos. |
| Operadores lógicos | Combinar condiciones con `and` / `or` / `not` en al menos **dos** sitios distintos (p. ej. validar rango `1 <= n <= max` y menú). |
| Cortocircuito | Al menos un uso donde se note: p. ej. `if nombre and nombre.strip():` o valor por defecto con `or`. |
| `if` / `elif` / `else` | Cadena con **≥ 3 ramas** (dificultad o menú) **y** un `else` que cubra caso residual. |
| `while` | Menú principal hasta salir **y** otro `while` (entrada válida o bucle de intentos de una ronda). |
| `for` | Al menos un **`for` con significado** distinto al `while`: por ejemplo recuento de rondas con `for numero_ronda in range(total_rondas):`, o recorrer una lista de mensajes de ayuda guardada en una **lista literal** mínima. |
| `break` o `continue` | Al menos uno usado de forma legítima (salir de bucle de entrada, saltar iteración, etc.). |
| Listas (solo sintaxis Fase 1) | Una lista literal (aunque sea pequeña) recorrida con `for` o usada para puntuaciones/historial. |
| Memoria (`sys`) | En «Modo entrenador» (o al final de estadísticas): imprimir `sys.getsizeof(...)` de **una cadena** que dependa del jugador (p. ej. nombre + estadística). Importar `sys` donde corresponda. |

No hace falta usar **todas** las APIs del script `mediciones_fase1.py`; basta con dejar claro **qué** mide `getsizeof` en un objeto concreto.

---

## Criterios de aceptación (autocomprobación)

- Ejecutar `python nombre_del_archivo.py`, completar un flujo: nombre → menú → partida de **≥ 2** rondas → estadísticas coherentes → salida sin error.
- Tras una entrada absurdamente errónea en el menú, el programa **no termina** y vuelve a mostrar opciones.
- En una ronda imposible de adivinar a propósito (agotando intentos), el contador de **rondas perdidas** sube.
- En comentarios breves puede indicarse **dónde** se usa cortocircuito y **dónde** un `for` frente a un `while`.

---

## Extensiones opcionales (más práctica)

- Límite de **partidas** por sesión o «racha» de victorias con `if` anidados.
- Dificultad «extrema» con un cuarto `elif`.
- Mini tabla ASCII generada con un `for` anidado (opcional, para práctica de formateo).

---

## Recursos

- Teoría y métricas: [conceptos-estructuras-y-metricas.md](./conceptos-estructuras-y-metricas.md).
- Ejemplo de medición: [mediciones_fase1.py](./mediciones_fase1.py).

Conviene, al terminar, poder explicar en voz alta el flujo del menú y de una sola ronda: si el relato es fluido, el módulo está asimilado.
