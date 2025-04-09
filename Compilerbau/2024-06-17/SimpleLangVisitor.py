# Generated from SimpleLang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#program.
    def visitProgram(self, ctx:SimpleLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#statement.
    def visitStatement(self, ctx:SimpleLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assignment.
    def visitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#expression.
    def visitExpression(self, ctx:SimpleLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#magicFunctionCall.
    def visitMagicFunctionCall(self, ctx:SimpleLangParser.MagicFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#parameters.
    def visitParameters(self, ctx:SimpleLangParser.ParametersContext):
        return self.visitChildren(ctx)



del SimpleLangParser