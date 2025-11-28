from antlr4.error.ErrorListener import ErrorListener

class BIOErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"[Error de sintaxis] Línea {line}, columna {column}: {msg}")
        # Evita que ANTLR siga parseando basura
        raise Exception("ErrorSintaxis")
