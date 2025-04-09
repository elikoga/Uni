# Generated from Lang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete generic visitor for a parse tree produced by LangParser.

class LangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LangParser#program.
    def visitProgram(self, ctx:LangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#statement.
    def visitStatement(self, ctx:LangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#comment.
    def visitComment(self, ctx:LangParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#let_statement.
    def visitLet_statement(self, ctx:LangParser.Let_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#expression.
    def visitExpression(self, ctx:LangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#expression_statement.
    def visitExpression_statement(self, ctx:LangParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#expression_with_block.
    def visitExpression_with_block(self, ctx:LangParser.Expression_with_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#expression_without_block.
    def visitExpression_without_block(self, ctx:LangParser.Expression_without_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#block_expression.
    def visitBlock_expression(self, ctx:LangParser.Block_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#loop_expression.
    def visitLoop_expression(self, ctx:LangParser.Loop_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#while_expression.
    def visitWhile_expression(self, ctx:LangParser.While_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#if_expression.
    def visitIf_expression(self, ctx:LangParser.If_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#literal_expression.
    def visitLiteral_expression(self, ctx:LangParser.Literal_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#variable_expression.
    def visitVariable_expression(self, ctx:LangParser.Variable_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#function_call_expression.
    def visitFunction_call_expression(self, ctx:LangParser.Function_call_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#negation_expression.
    def visitNegation_expression(self, ctx:LangParser.Negation_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#grouped_expression.
    def visitGrouped_expression(self, ctx:LangParser.Grouped_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#math_operator.
    def visitMath_operator(self, ctx:LangParser.Math_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#comparison_operator.
    def visitComparison_operator(self, ctx:LangParser.Comparison_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#logical_operator.
    def visitLogical_operator(self, ctx:LangParser.Logical_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#assignment_operator.
    def visitAssignment_operator(self, ctx:LangParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#break_expression.
    def visitBreak_expression(self, ctx:LangParser.Break_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#type.
    def visitType(self, ctx:LangParser.TypeContext):
        return self.visitChildren(ctx)



del LangParser