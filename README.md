<div id="top"></div>

# Mastering Python

Material abierto para **profundizar en Python** de forma ordenada: desde la sintaxis básica hasta temas avanzados de arquitectura y diseño de sistemas. Cualquiera puede clonar el repositorio, seguir las fases y practicar a su ritmo.

## Objetivos por fase

### Fase 1 — Fundamentos y sintaxis

En esta etapa el foco es entender cómo expresar instrucciones claras a la máquina y habitualizarse a los errores de sintaxis como parte normal del aprendizaje.

- **Conceptos clave:** variables, tipos de datos (`str`, enteros, booleanos), operadores lógicos y aritméticos.
- **Estructuras de control:** condicionales (`if`, `else`) y bucles (`for`, `while`).
- **Hito:** primer «Hola mundo» y scripts sencillos (por ejemplo calculadora por consola o juego de adivinanzas).
- **Desafío típico:** depurar indentación y detalles de sintaxis sin frustrarse.

**Material:** [Fase 1 — conceptos y métricas](phases/01-fundamentos-y-sintaxis/conceptos-estructuras-y-metricas.md), [reto integrador](phases/01-fundamentos-y-sintaxis/RETO-FASE-1.md).

### Fase 2 — Estructura y resolución de problemas

Salir del guion lineal y organizar la lógica en piezas reutilizables.

- **Conceptos clave:** funciones, manejo de errores (`try` / `except`), lectura y escritura de archivos.
- **Estructuras de datos:** listas, diccionarios, tuplas y conjuntos; almacenar y recuperar información con criterio.
- **Paradigmas:** introducción a programación orientada a objetos (clases, herencia) o enfoque funcional.
- **Hito:** algoritmos introductorios (estilo ejercicios de plataformas de práctica) y pequeños programas útiles (organización de archivos, scraping básico, etc.).

### Fase 3 — Construcción y ecosistema

Usar Python como palanca dentro de un ecosistema real: APIs, datos y despliegue.

- **Conceptos clave:** consumo de APIs (REST/GraphQL), bases de datos SQL y NoSQL, programación asíncrona (`async` / `await`, hilos o tareas según el caso).
- **Herramientas:** Git, terminal, entornos virtuales, contenedores (por ejemplo Docker) cuando aplique.
- **Frameworks web (Python):** profundizar en al menos uno (por ejemplo Django o FastAPI) según el interés.
- **Hito:** aplicación desplegable con CRUD, autenticación y persistencia.

### Fase 4 — Calidad, mantenibilidad y arquitectura

Que el código no solo funcione, sino que sea comprensible y fácil de evolucionar.

- **Clean code:** nombres claros, funciones con una responsabilidad clara, refactorización.
- **Principios y patrones:** SOLID, DRY, patrones de diseño habituales.
- **Testing:** pruebas unitarias, de integración, enfoque TDD cuando convenga.
- **DevOps básico:** CI/CD.
- **Hito:** código cubierto por pruebas y legible para otras personas sin guión oral permanente.

### Fase 5 — Profundidad y diseño de sistemas

Entender cómo funciona el lenguaje y el runtime bajo el capó, y diseñar sistemas grandes.

- **Funcionamiento interno:** modelo de memoria, recolector de basura, ciclo de compilación/ejecución en CPython, optimización informada.
- **Arquitectura:** microservicios, sistemas distribuidos, datos a escala, alta concurrencia.
- **Comunidad y liderazgo técnico:** open source, estándares de equipo, mentoría.
- **Hito:** plantear arquitectura de sistemas complejos desde cero y elegir herramientas con criterio (qué usar y qué descartar).

## Estructura del repositorio

| Ruta | Descripción |
|------|-------------|
| [`phases/`](phases/) | Material y ejercicios por fase (`01-` … `05-`). Índice: [`phases/README.md`](phases/README.md). |
| [`CHANGELOG.md`](CHANGELOG.md) | Cambios recientes en el material. |

### Nomenclatura de carpetas

Prefijo numérico (`01-`, `02-`, …) más nombre en **kebab-case** en español:

1. `01-fundamentos-y-sintaxis`
2. `02-intermedio-estructura-y-problemas`
3. `03-avanzado-ecosistema`
4. `04-profesional-calidad-y-arquitectura`
5. `05-experto-y-master`

## Requisitos

- **Python 3** (versión reciente). Tamaños y tiempos medidos con `sys.getsizeof` / `timeit` pueden variar según versión y arquitectura.

## Uso sugerido

1. Clonar el repositorio.
2. Revisar la sección **Objetivos por fase** y abrir la carpeta correspondiente en `phases/`.
3. En Fase 1, ejecutar desde la raíz del repo:

```bash
python phases/01-fundamentos-y-sintaxis/mediciones_fase1.py
```

## Licencia

El contenido se distribuye bajo la licencia indicada en [`LICENSE.txt`](LICENSE.txt).

<p align="right">(<a href="#top">volver arriba</a>)</p>
