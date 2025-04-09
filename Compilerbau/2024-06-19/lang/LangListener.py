# Generated from Lang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete listener for a parse tree produced by LangParser.
class LangListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#program.
    def enterProgram(self, ctx:LangParser.ProgramContext):
        pass

    # Exit a parse tree produced by LangParser#program.
    def exitProgram(self, ctx:LangParser.ProgramContext):
        pass


    # Enter a parse tree produced by LangParser#statement.
    def enterStatement(self, ctx:LangParser.StatementContext):
        pass

    # Exit a parse tree produced by LangParser#statement.
    def exitStatement(self, ctx:LangParser.StatementContext):
        pass


    # Enter a parse tree produced by LangParser#comment.
    def enterComment(self, ctx:LangParser.CommentContext):
        pass

    # Exit a parse tree produced by LangParser#comment.
    def exitComment(self, ctx:LangParser.CommentContext):
        pass


    # Enter a parse tree produced by LangParser#let_statement.
    def enterLet_statement(self, ctx:LangParser.Let_statementContext):
        pass

    # Exit a parse tree produced by LangParser#let_statement.
    def exitLet_statement(self, ctx:LangParser.Let_statementContext):
        pass


    # Enter a parse tree produced by LangParser#expression.
    def enterExpression(self, ctx:LangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#expression.
    def exitExpression(self, ctx:LangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#expression_statement.
    def enterExpression_statement(self, ctx:LangParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by LangParser#expression_statement.
    def exitExpression_statement(self, ctx:LangParser.Expression_statementContext):
        pass


    # Enter a parse tree produced by LangParser#expression_with_block.
    def enterExpression_with_block(self, ctx:LangParser.Expression_with_blockContext):
        pass

    # Exit a parse tree produced by LangParser#expression_with_block.
    def exitExpression_with_block(self, ctx:LangParser.Expression_with_blockContext):
        pass


    # Enter a parse tree produced by LangParser#expression_without_block.
    def enterExpression_without_block(self, ctx:LangParser.Expression_without_blockContext):
        pass

    # Exit a parse tree produced by LangParser#expression_without_block.
    def exitExpression_without_block(self, ctx:LangParser.Expression_without_blockContext):
        pass


    # Enter a parse tree produced by LangParser#block_expression.
    def enterBlock_expression(self, ctx:LangParser.Block_expressionContext):
        pass

    # Exit a parse tree produced by LangParser#block_expression.
    def exitBlock_expression(self, ctx:LangParser.Block_expressionContext):
        pass


    # Enter a parse tree produced by LangParser#loop_expression.
    def enterLoop_expression(self, ctx:LangParser.Loop_expressionContext):
        pass

    # Exit a parse tree produced by LangParser#loop_expression.
    def exitLoop_expression(self, ctx:LangParser.Loop_expressionContext):
        pass


    # Enter a parse tree produced by LangParser#while_expression.
    def enterWhile_expression(self, ctx:LangParser.While_expressionContext):
        pass

    # Exit a parse tree produced by LangParser#while_expression.
    def exitWhile_expression(self, ctx:LangParser.While_expressionContext):
        pass


    # Enter a parse tree produced by LangParser#if_expression.
    def enterIf_expression(self, ctx:LangParser.If_expressionContext):
        pass

    # Exit a parse tree produced by LangParser#if_expression.
    def exitIf_expression(self, ctx:LangParser.If_expressionContext):
        pass


    # Enter a parse tree produced by LangParser#literal_expression.
    def enterLiteral_expression(self, ctx:LangParser.Literal_expressionContext):
        pass

    # Exit a parse tree produced by LangParser#literal_expression.
    def exitLiteral_expression(self, ctx:LangParser.Literal_expressionContext):
        pass


    # Enter a parse tree produced by LangParser#variable_expression.
    def enterVariable_expression(self, ctx:LangParser.Variable_expressionContext):
        pass

    # Exit a parse tree produced by LangParser#variable_expression.
    def exitVariable_expression(self, ctx:LangParser.Variable_expressionContext):
        pass


    # Enter a parse tree produced by LangParser#function_call_expression.
    def enterFunction_call_expression(self, ctx:LangParser.Function_call_expressionContext):
        pass

    # Exit a parse tree produced by LangParser#function_call_expression.
    def exitFunction_call_expression(self, ctx:LangParser.Function_call_expressionContext):
        pass


    # Enter a parse tree produced by LangParser#negation_expression.
    def enterNegation_expression(self, ctx:LangParser.Negation_expressionContext):
        pass

    # Exit a parse tree produced by LangParser#negation_expression.
    def exitNegation_expression(self, ctx:LangParser.Negation_expressionContext):
        pass


    # Enter a parse tree produced by LangParser#grouped_expression.
    def enterGrouped_expression(self, ctx:LangParser.Grouped_expressionContext):
        pass

    # Exit a parse tree produced by LangParser#grouped_expression.
    def exitGrouped_expression(self, ctx:LangParser.Grouped_expressionContext):
        pass


    # Enter a parse tree produced by LangParser#math_operator.
    def enterMath_operator(self, ctx:LangParser.Math_operatorContext):
        pass

    # Exit a parse tree produced by LangParser#math_operator.
    def exitMath_operator(self, ctx:LangParser.Math_operatorContext):
        pass


    # Enter a parse tree produced by LangParser#comparison_operator.
    def enterComparison_operator(self, ctx:LangParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by LangParser#comparison_operator.
    def exitComparison_operator(self, ctx:LangParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by LangParser#logical_operator.
    def enterLogical_operator(self, ctx:LangParser.Logical_operatorContext):
        pass

    # Exit a parse tree produced by LangParser#logical_operator.
    def exitLogical_operator(self, ctx:LangParser.Logical_operatorContext):
        pass


    # Enter a parse tree produced by LangParser#assignment_operator.
    def enterAssignment_operator(self, ctx:LangParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by LangParser#assignment_operator.
    def exitAssignment_operator(self, ctx:LangParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by LangParser#break_expression.
    def enterBreak_expression(self, ctx:LangParser.Break_expressionContext):
        pass

    # Exit a parse tree produced by LangParser#break_expression.
    def exitBreak_expression(self, ctx:LangParser.Break_expressionContext):
        pass


    # Enter a parse tree produced by LangParser#type.
    def enterType(self, ctx:LangParser.TypeContext):
        pass

    # Exit a parse tree produced by LangParser#type.
    def exitType(self, ctx:LangParser.TypeContext):
        pass



del LangParser