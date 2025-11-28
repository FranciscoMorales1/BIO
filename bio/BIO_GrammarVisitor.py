# Generated from BIO_Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BIO_Grammar import BIO_Grammar
else:
    from BIO_Grammar import BIO_Grammar

# This class defines a complete generic visitor for a parse tree produced by BIO_Grammar.

class BIO_GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BIO_Grammar#program.
    def visitProgram(self, ctx:BIO_Grammar.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#stmt.
    def visitStmt(self, ctx:BIO_Grammar.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#bloque.
    def visitBloque(self, ctx:BIO_Grammar.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#asignacion.
    def visitAsignacion(self, ctx:BIO_Grammar.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#retornarStmt.
    def visitRetornarStmt(self, ctx:BIO_Grammar.RetornarStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#siStmt.
    def visitSiStmt(self, ctx:BIO_Grammar.SiStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#mientrasStmt.
    def visitMientrasStmt(self, ctx:BIO_Grammar.MientrasStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#paraStmt.
    def visitParaStmt(self, ctx:BIO_Grammar.ParaStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#breakStmt.
    def visitBreakStmt(self, ctx:BIO_Grammar.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#continueStmt.
    def visitContinueStmt(self, ctx:BIO_Grammar.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#imprimirStmt.
    def visitImprimirStmt(self, ctx:BIO_Grammar.ImprimirStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#graficarStmt.
    def visitGraficarStmt(self, ctx:BIO_Grammar.GraficarStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#funcionDef.
    def visitFuncionDef(self, ctx:BIO_Grammar.FuncionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#params.
    def visitParams(self, ctx:BIO_Grammar.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#expr.
    def visitExpr(self, ctx:BIO_Grammar.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#logical_or.
    def visitLogical_or(self, ctx:BIO_Grammar.Logical_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#logical_and.
    def visitLogical_and(self, ctx:BIO_Grammar.Logical_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#equality.
    def visitEquality(self, ctx:BIO_Grammar.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#comparison.
    def visitComparison(self, ctx:BIO_Grammar.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#addition.
    def visitAddition(self, ctx:BIO_Grammar.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#multiplication.
    def visitMultiplication(self, ctx:BIO_Grammar.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#exponent.
    def visitExponent(self, ctx:BIO_Grammar.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#unary.
    def visitUnary(self, ctx:BIO_Grammar.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#primary.
    def visitPrimary(self, ctx:BIO_Grammar.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#postfix.
    def visitPostfix(self, ctx:BIO_Grammar.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#atom.
    def visitAtom(self, ctx:BIO_Grammar.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#funcionNativa.
    def visitFuncionNativa(self, ctx:BIO_Grammar.FuncionNativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#argumentos.
    def visitArgumentos(self, ctx:BIO_Grammar.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#lista.
    def visitLista(self, ctx:BIO_Grammar.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BIO_Grammar#matriz.
    def visitMatriz(self, ctx:BIO_Grammar.MatrizContext):
        return self.visitChildren(ctx)



del BIO_Grammar