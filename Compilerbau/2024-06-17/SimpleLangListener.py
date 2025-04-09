# Generated from SimpleLang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#program.
    def enterProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#program.
    def exitProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#statement.
    def enterStatement(self, ctx:SimpleLangParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#statement.
    def exitStatement(self, ctx:SimpleLangParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#assignment.
    def enterAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#assignment.
    def exitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#expression.
    def enterExpression(self, ctx:SimpleLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#expression.
    def exitExpression(self, ctx:SimpleLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#magicFunctionCall.
    def enterMagicFunctionCall(self, ctx:SimpleLangParser.MagicFunctionCallContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#magicFunctionCall.
    def exitMagicFunctionCall(self, ctx:SimpleLangParser.MagicFunctionCallContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#parameters.
    def enterParameters(self, ctx:SimpleLangParser.ParametersContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#parameters.
    def exitParameters(self, ctx:SimpleLangParser.ParametersContext):
        pass



del SimpleLangParser