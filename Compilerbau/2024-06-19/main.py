from antlr4 import CommonTokenStream, InputStream
from lang import LangParser, LangLexer, ASTBuilder, GameBoyAssemblyGenerator
from antlr4.tree.Trees import Trees

def main():

    program = """
    let a: Byte = 1;
    {
    let a: Byte = 2;
    printByte(a);
    }
    """

    input_stream = InputStream(program)
    lexer = LangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LangParser(stream)
    visitor = ASTBuilder()

    print("Parsing...")
    tree = parser.program()
    print(f"Tree: {Trees.toStringTree(tree, None, parser)}")
    # print(tree)
    ast = visitor.visit(tree)
    # print(ast)
    print("Generating assembly...")
    assembly_generator = GameBoyAssemblyGenerator(ast)
    assembly = assembly_generator.generate()
    print(assembly)
    # save as ./build/main.asm
    with open("./build/main.asm", "w") as f:
        f.write(str(assembly))

if __name__ == '__main__':
    main()