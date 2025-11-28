# ==============================
# EvalVisitor.py
# ==============================
from BIO_GrammarVisitor import BIO_GrammarVisitor

from stdlib.matematicas import *
from stdlib.matrices import *
from stdlib.archivos import *
from stdlib.graficas import *
from stdlib.regresion import *
from stdlib.redes import *


class BreakException(Exception): pass
class ContinueException(Exception): pass


class EvalVisitor(BIO_GrammarVisitor):

    def __init__(self):
        self.global_vars = {}
        self.funciones = {}       # funciones definidas por el usuario
        self.return_value = None
        self.inside_return = False

    # ============================================================
    # PROGRAM
    # ============================================================
    def visitProgram(self, ctx):
        for stmt in ctx.stmt():
            self.visit(stmt)
        return None

    # ============================================================
    # STATEMENTS
    # ============================================================
    def visitStmt(self, ctx):

        if ctx.asignacion():
            return self.visit(ctx.asignacion())

        if ctx.imprimirStmt():
            return self.visit(ctx.imprimirStmt())

        if ctx.graficarStmt():
            return self.visit(ctx.graficarStmt())

        if ctx.siStmt():
            return self.visit(ctx.siStmt())

        if ctx.mientrasStmt():
            return self.visit(ctx.mientrasStmt())

        if ctx.paraStmt():
            return self.visit(ctx.paraStmt())

        if ctx.funcionDef():
            return self.visit(ctx.funcionDef())

        if ctx.breakStmt():
            raise BreakException()

        if ctx.continueStmt():
            raise ContinueException()

        if ctx.retornarStmt():
            return self.visit(ctx.retornarStmt())

        if ctx.bloque():
            return self.visit(ctx.bloque())

        if ctx.expr():
            val = self.visit(ctx.expr())
            if val is not None:
                print(val)
            return val

        return None

    # ============================================================
    # ASIGNACION
    # ============================================================
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expr())
        self.global_vars[nombre] = valor
        return valor

    # ============================================================
    # IMPRIMIR
    # ============================================================
    def visitImprimirStmt(self, ctx):
        val = self.visit(ctx.expr())
        print(val)
        return val

    # ============================================================
    # RETORNAR
    # ============================================================
    def visitRetornarStmt(self, ctx):
        if ctx.expr():
            self.return_value = self.visit(ctx.expr())
        else:
            self.return_value = None
        self.inside_return = True
        return self.return_value

    # ============================================================
    # GRAFICAR
    # ============================================================
    def visitGraficarStmt(self, ctx):
        args = []
        if ctx.argumentos():
            args = [self.visit(e) for e in ctx.argumentos().expr()]
        return graficar(*args)

    # ============================================================
    # BLOQUE
    # ============================================================
    def visitBloque(self, ctx):
        for stmt in ctx.stmt():
            try:
                self.visit(stmt)
            except BreakException:
                raise
            except ContinueException:
                raise

            if self.inside_return:
                break
        return None

    # ============================================================
    # IF
    # ============================================================
    def visitSiStmt(self, ctx):

        if self.visit(ctx.expr(0)):
            return self.visit(ctx.bloque(0))

        for i in range(len(ctx.SINO_SI())):
            if self.visit(ctx.expr(i + 1)):
                return self.visit(ctx.bloque(i + 1))

        if ctx.SINO():
            return self.visit(ctx.bloque(len(ctx.SINO_SI()) + 1))

        return None

    # ============================================================
    # MIENTRAS
    # ============================================================
    def visitMientrasStmt(self, ctx):
        while self.visit(ctx.expr()):
            try:
                self.visit(ctx.bloque())
            except BreakException:
                break
            except ContinueException:
                continue
        return None

    # ============================================================
    # PARA
    # ============================================================
    def visitParaStmt(self, ctx):
        self.visit(ctx.asignacion(0))
        while self.visit(ctx.expr()):
            try:
                self.visit(ctx.bloque())
            except BreakException:
                break
            except ContinueException:
                self.visit(ctx.asignacion(1))
                continue
            self.visit(ctx.asignacion(1))
        return None

    # ============================================================
    # EXPRESIONES
    # ============================================================
    def visitExpr(self, ctx):
        return self.visit(ctx.logical_or())

    def visitLogical_or(self, ctx):
        val = self.visit(ctx.logical_and(0))
        for i in range(1, len(ctx.logical_and())):
            val = bool(val or self.visit(ctx.logical_and(i)))
        return val

    def visitLogical_and(self, ctx):
        val = self.visit(ctx.equality(0))
        for i in range(1, len(ctx.equality())):
            val = bool(val and self.visit(ctx.equality(i)))
        return val

    def visitEquality(self, ctx):
        val = self.visit(ctx.comparison(0))
        j = 1
        for i in range(1, len(ctx.comparison())):
            op = ctx.getChild(j).getText()
            right = self.visit(ctx.comparison(i))
            val = (val == right) if op == "==" else (val != right)
            j += 2
        return val

    def visitComparison(self, ctx):
        val = self.visit(ctx.addition(0))
        j = 1
        for i in range(1, len(ctx.addition())):
            op = ctx.getChild(j).getText()
            right = self.visit(ctx.addition(i))
            if op == ">": val = val > right
            elif op == "<": val = val < right
            elif op == ">=": val = val >= right
            elif op == "<=": val = val <= right
            j += 2
        return val

    def visitAddition(self, ctx):
        val = self.visit(ctx.multiplication(0))
        for i in range(1, len(ctx.multiplication())):
            op = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.multiplication(i))
            val = val + right if op == "+" else val - right
        return val

    def visitMultiplication(self, ctx):
        val = self.visit(ctx.exponent(0))
        for i in range(1, len(ctx.exponent())):
            op = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.exponent(i))
            if op == "*": val *= right
            elif op == "/": val /= right
            else: val %= right
        return val

    def visitExponent(self, ctx):
        base = self.visit(ctx.unary())
        if ctx.exponent():
            exp = self.visit(ctx.exponent())
            return base ** exp
        return base

    def visitUnary(self, ctx):
        if ctx.MINUS(): return -self.visit(ctx.unary())
        if ctx.NOT(): return not self.visit(ctx.unary())
        return self.visit(ctx.primary())

    # ============================================================
    # PRIMARY / POSTFIX
    # ============================================================
    def visitPrimary(self, ctx):
        value = self.visit(ctx.atom())
        for p in ctx.postfix():
            value = self.applyPostfix(p, value)
        return value

    def applyPostfix(self, ctx, base):
        if ctx.PAR_OPEN():
            if not callable(base):
                raise Exception("Intento de llamar algo que no es función.")
            args = []
            if ctx.argumentos():
                args = [self.visit(e) for e in ctx.argumentos().expr()]
            return base(*args)

        if ctx.COR_OPEN():
            index = self.visit(ctx.expr())
            return base[index]

        raise Exception("Postfix no reconocido")

    # ============================================================
    # ATOM
    # ============================================================
    def visitAtom(self, ctx):

        if ctx.PAR_OPEN():
            return self.visit(ctx.expr())

        if ctx.funcionNativa():
            return self.visit(ctx.funcionNativa())

        if ctx.matriz():
            return self.visit(ctx.matriz())

        if ctx.lista():
            return self.visit(ctx.lista())

        if ctx.NUMERO():
            text = ctx.NUMERO().getText()
            return float(text) if "." in text else int(text)

        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]

        if ctx.ID():
            nombre = ctx.ID().getText()

            if nombre in self.global_vars:
                return self.global_vars[nombre]

            if nombre in self.funciones:
                def wrapper(*args, __nombre=nombre, __self=self):
                    return __self.ejecutarFuncionUsuario(__nombre, list(args))
                return wrapper

            if nombre in globals() and callable(globals()[nombre]):
                return globals()[nombre]

            raise Exception(f"Variable o función '{nombre}' no definida.")

        raise Exception("Atom inválido")

    # ============================================================
    # LISTAS / MATRICES
    # ============================================================
    def visitLista(self, ctx):
        return [self.visit(e) for e in ctx.expr()] if ctx.expr() else []

    def visitMatriz(self, ctx):
        return [self.visit(l) for l in ctx.lista()] if ctx.lista() else []

    # ============================================================
    # FUNCIONES NATIVAS
    # ============================================================
    def visitFuncionNativa(self, ctx):
        nombre = ctx.getChild(0).getText()
        args = []
        if ctx.argumentos():
            args = [self.visit(e) for e in ctx.argumentos().expr()]

        if nombre in globals():
            return globals()[nombre](*args)

        raise Exception(f"Función nativa '{nombre}' no existe.")

    # ============================================================
    # FUNCIONES DE USUARIO
    # ============================================================
    def visitFuncionDef(self, ctx):
        self.funciones[ctx.ID().getText()] = ctx
        return None

    def ejecutarFuncionUsuario(self, nombre, args):
        ctx = self.funciones[nombre]
        params = [p.getText() for p in ctx.params().ID()] if ctx.params() else []

        if len(params) != len(args):
            raise Exception(f"La función '{nombre}' esperaba {len(params)} parámetros.")

        saved_vars = self.global_vars.copy()
        saved_ret = self.return_value
        saved_flag = self.inside_return

        for p, v in zip(params, args):
            self.global_vars[p] = v

        self.return_value = None
        self.inside_return = False

        self.visit(ctx.bloque())

        result = self.return_value

        self.global_vars = saved_vars
        self.return_value = saved_ret
        self.inside_return = saved_flag

        return result

