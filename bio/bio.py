import sys
from antlr4 import *
from BIO_Lexer import BIO_Lexer
from BIO_Grammar import BIO_Grammar
from EvalVisitor import EvalVisitor
from BIOErrorListener import BIOErrorListener


# ============================================================
# EJECUTAR CÓDIGO BIO DESDE UN STRING
# ============================================================
def ejecutar_codigo(codigo, visitor):

    input_stream = InputStream(codigo)
    lexer = BIO_Lexer(input_stream)
    tokens = CommonTokenStream(lexer)

    parser = BIO_Grammar(tokens)

    # Instalar gestor de errores
    parser.removeErrorListeners()
    parser.addErrorListener(BIOErrorListener())

    try:
        tree = parser.program()
        visitor.visit(tree)

    except Exception as e:
        # Error ya manejado por el listener
        if str(e) == "ErrorSintaxis":
            return
        print(f"[Error en tiempo de ejecución] {e}")


# ============================================================
# EJECUTAR ARCHIVO .bio
# ============================================================
def ejecutar_archivo(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            codigo = f.read()
    except FileNotFoundError:
        print(f"[Error] No se encontró el archivo: {ruta}")
        return

    visitor = EvalVisitor()
    ejecutar_codigo(codigo, visitor)


# ============================================================
# REPL (INTERPRETADOR INTERACTIVO ROBUSTO)
# Soporta bloques multilínea con { }
# y ejecuta al presionar ENTER si el bloque está completo.
# ============================================================
def iniciar_repl():
    print("BIO v1.0 — Lenguaje de programación para aprendizaje profundo")
    print("Escribe 'salir' para terminar.\n")

    visitor = EvalVisitor()

    buffer = ""
    nivel_bloque = 0

    while True:
        try:
            linea = input(">> ")
        except EOFError:
            break

        if linea.strip() == "salir":
            break

        # Conteo de llaves
        nivel_bloque += linea.count("{")
        nivel_bloque -= linea.count("}")

        # Añadir línea al buffer
        buffer += linea + "\n"

        # -----------------------------
        # LÓGICA ROBUSTA DE EJECUCIÓN
        # -----------------------------
        linea_limpia = linea.strip()

        # *** Caso 1: buffer completo y ENTER en línea vacía ***
        if nivel_bloque == 0 and linea_limpia == "" and buffer.strip() != "":
            ejecutar_codigo(buffer, visitor)
            buffer = ""
            continue

        # *** Caso 2: termina en ';' o en '}' ***
        if nivel_bloque == 0 and (
            linea_limpia.endswith(";") or
            linea_limpia.endswith("}")
        ):
            ejecutar_codigo(buffer, visitor)
            buffer = ""
            continue


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":

    if len(sys.argv) == 2:
        ejecutar_archivo(sys.argv[1])
    else:
        iniciar_repl()
