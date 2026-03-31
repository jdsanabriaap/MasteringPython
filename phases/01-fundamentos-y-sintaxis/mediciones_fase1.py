"""
Mediciones de referencia para la Fase 1: tamaños con sys.getsizeof y tiempos con timeit.
Ejecutar: python phases/01-fundamentos-y-sintaxis/mediciones_fase1.py
"""

from __future__ import annotations

import sys
import timeit


def report_memory() -> None:
    print("=== sys.getsizeof (objeto solo; no incluye objetos referenciados) ===\n")
    rows: list[tuple[str, object]] = [
        ("True", True),
        ("False", False),
        ("None", None),
        ("int 0", 0),
        ("int 42", 42),
        ("int 2**30", 2**30),
        ("int grande (10**100)", 10**100),
        ("float 3.14", 3.14),
        ("str ''", ""),
        ("str 'hola'", "hola"),
        ("str 1000 x 'x'", "x" * 1000),
        ("list []", []),
        ("list [1,2,3]", [1, 2, 3]),
        ("dict {}", {}),
        ("dict {1:2}", {1: 2}),
    ]
    for label, obj in rows:
        print(f"{label!s:<28} {sys.getsizeof(obj):>6} bytes")

    print("\nNota: para contenedores, getsizeof no suma elementos; usa una función recursiva")
    print("      o estima aparte si necesitas memoria total del árbol de objetos.\n")


def report_timing() -> None:
    print("=== timeit (promedio por ejecución; depende de CPU y versión de Python) ===\n")
    n = 500_000
    t_for = timeit.timeit("for _ in range(10): pass", number=n) / n
    t_while = timeit.timeit("i = 0\nwhile i < 10:\n    i += 1", number=n) / n
    n_if = n * 2
    t_if_true = timeit.timeit("if True: pass", number=n_if) / n_if
    t_if_false = timeit.timeit("if False: pass", number=n_if) / n_if

    print(f"for _ in range(10): pass    {t_for:.3e} s por bucle completo (~10 iter)")
    print(f"while i < 10 (10 iter)       {t_while:.3e} s por bucle completo")
    print(f"if True: pass                {t_if_true:.3e} s")
    print(f"if False: pass               {t_if_false:.3e} s")
    print(f"\nPython: {sys.version.split()[0]}")


def main() -> None:
    report_memory()
    report_timing()


if __name__ == "__main__":
    main()
