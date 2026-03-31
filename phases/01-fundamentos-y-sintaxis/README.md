# Fase 1 — Fundamentos y sintaxis

Objetivo de la fase: dominar variables, tipos básicos, operadores y estructuras de control (`if` / `else`, `for`, `while`). Los objetivos ampliados están en el [README del repositorio](../../README.md#objetivos-por-fase).

## Material principal

- [Conceptos, estructuras de control y métricas (memoria y tiempo)](./conceptos-estructuras-y-metricas.md)
- [Reto integrador de la fase — «Liga de la suma oculta»](./RETO-FASE-1.md)

## Scripts de ejemplo

- [hola-mundo.py](./hola-mundo.py): primer script interactivo con validaciones basicas.
- [liga-suma-oculta.py](./liga-suma-oculta.py): solucion de referencia del reto integrador en consola.

## Medición reproducible

Para imprimir en consola tamaños aproximados (`sys.getsizeof`) y tiempos de referencia (`timeit`), ejecuta desde la raíz del repositorio:

```bash
python phases/01-fundamentos-y-sintaxis/mediciones_fase1.py
```

Los valores dependen de la versión de CPython y de la arquitectura (32/64 bits).
