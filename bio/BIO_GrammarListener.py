# Generated from BIO_Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BIO_Grammar import BIO_Grammar
else:
    from BIO_Grammar import BIO_Grammar

# This class defines a complete listener for a parse tree produced by BIO_Grammar.
class BIO_GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by BIO_Grammar#program.
    def enterProgram(self, ctx:BIO_Grammar.ProgramContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#program.
    def exitProgram(self, ctx:BIO_Grammar.ProgramContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#stmt.
    def enterStmt(self, ctx:BIO_Grammar.StmtContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#stmt.
    def exitStmt(self, ctx:BIO_Grammar.StmtContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#bloque.
    def enterBloque(self, ctx:BIO_Grammar.BloqueContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#bloque.
    def exitBloque(self, ctx:BIO_Grammar.BloqueContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#asignacion.
    def enterAsignacion(self, ctx:BIO_Grammar.AsignacionContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#asignacion.
    def exitAsignacion(self, ctx:BIO_Grammar.AsignacionContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#retornarStmt.
    def enterRetornarStmt(self, ctx:BIO_Grammar.RetornarStmtContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#retornarStmt.
    def exitRetornarStmt(self, ctx:BIO_Grammar.RetornarStmtContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#siStmt.
    def enterSiStmt(self, ctx:BIO_Grammar.SiStmtContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#siStmt.
    def exitSiStmt(self, ctx:BIO_Grammar.SiStmtContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#mientrasStmt.
    def enterMientrasStmt(self, ctx:BIO_Grammar.MientrasStmtContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#mientrasStmt.
    def exitMientrasStmt(self, ctx:BIO_Grammar.MientrasStmtContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#paraStmt.
    def enterParaStmt(self, ctx:BIO_Grammar.ParaStmtContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#paraStmt.
    def exitParaStmt(self, ctx:BIO_Grammar.ParaStmtContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#breakStmt.
    def enterBreakStmt(self, ctx:BIO_Grammar.BreakStmtContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#breakStmt.
    def exitBreakStmt(self, ctx:BIO_Grammar.BreakStmtContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#continueStmt.
    def enterContinueStmt(self, ctx:BIO_Grammar.ContinueStmtContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#continueStmt.
    def exitContinueStmt(self, ctx:BIO_Grammar.ContinueStmtContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#imprimirStmt.
    def enterImprimirStmt(self, ctx:BIO_Grammar.ImprimirStmtContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#imprimirStmt.
    def exitImprimirStmt(self, ctx:BIO_Grammar.ImprimirStmtContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#graficarStmt.
    def enterGraficarStmt(self, ctx:BIO_Grammar.GraficarStmtContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#graficarStmt.
    def exitGraficarStmt(self, ctx:BIO_Grammar.GraficarStmtContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#funcionDef.
    def enterFuncionDef(self, ctx:BIO_Grammar.FuncionDefContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#funcionDef.
    def exitFuncionDef(self, ctx:BIO_Grammar.FuncionDefContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#params.
    def enterParams(self, ctx:BIO_Grammar.ParamsContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#params.
    def exitParams(self, ctx:BIO_Grammar.ParamsContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#expr.
    def enterExpr(self, ctx:BIO_Grammar.ExprContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#expr.
    def exitExpr(self, ctx:BIO_Grammar.ExprContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#logical_or.
    def enterLogical_or(self, ctx:BIO_Grammar.Logical_orContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#logical_or.
    def exitLogical_or(self, ctx:BIO_Grammar.Logical_orContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#logical_and.
    def enterLogical_and(self, ctx:BIO_Grammar.Logical_andContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#logical_and.
    def exitLogical_and(self, ctx:BIO_Grammar.Logical_andContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#equality.
    def enterEquality(self, ctx:BIO_Grammar.EqualityContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#equality.
    def exitEquality(self, ctx:BIO_Grammar.EqualityContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#comparison.
    def enterComparison(self, ctx:BIO_Grammar.ComparisonContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#comparison.
    def exitComparison(self, ctx:BIO_Grammar.ComparisonContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#addition.
    def enterAddition(self, ctx:BIO_Grammar.AdditionContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#addition.
    def exitAddition(self, ctx:BIO_Grammar.AdditionContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#multiplication.
    def enterMultiplication(self, ctx:BIO_Grammar.MultiplicationContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#multiplication.
    def exitMultiplication(self, ctx:BIO_Grammar.MultiplicationContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#exponent.
    def enterExponent(self, ctx:BIO_Grammar.ExponentContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#exponent.
    def exitExponent(self, ctx:BIO_Grammar.ExponentContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#unary.
    def enterUnary(self, ctx:BIO_Grammar.UnaryContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#unary.
    def exitUnary(self, ctx:BIO_Grammar.UnaryContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#primary.
    def enterPrimary(self, ctx:BIO_Grammar.PrimaryContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#primary.
    def exitPrimary(self, ctx:BIO_Grammar.PrimaryContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#postfix.
    def enterPostfix(self, ctx:BIO_Grammar.PostfixContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#postfix.
    def exitPostfix(self, ctx:BIO_Grammar.PostfixContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#atom.
    def enterAtom(self, ctx:BIO_Grammar.AtomContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#atom.
    def exitAtom(self, ctx:BIO_Grammar.AtomContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#funcionNativa.
    def enterFuncionNativa(self, ctx:BIO_Grammar.FuncionNativaContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#funcionNativa.
    def exitFuncionNativa(self, ctx:BIO_Grammar.FuncionNativaContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#argumentos.
    def enterArgumentos(self, ctx:BIO_Grammar.ArgumentosContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#argumentos.
    def exitArgumentos(self, ctx:BIO_Grammar.ArgumentosContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#lista.
    def enterLista(self, ctx:BIO_Grammar.ListaContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#lista.
    def exitLista(self, ctx:BIO_Grammar.ListaContext):
        pass


    # Enter a parse tree produced by BIO_Grammar#matriz.
    def enterMatriz(self, ctx:BIO_Grammar.MatrizContext):
        pass

    # Exit a parse tree produced by BIO_Grammar#matriz.
    def exitMatriz(self, ctx:BIO_Grammar.MatrizContext):
        pass



del BIO_Grammar