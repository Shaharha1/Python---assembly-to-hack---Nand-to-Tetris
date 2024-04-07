"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import os
import sys
import typing
from SymbolTable import SymbolTable
from Parser import Parser
from Code import Code


def assemble_file(
        input_file: typing.TextIO, output_file: typing.TextIO) -> None:
    """Assembles a single file.

    Args:
        input_file (typing.TextIO): the file to assemble.
        output_file (typing.TextIO): writes all output to this file.
    """
    # A good place to start is to initialize a new Parser object:
    # parser = Parser(input_file)
    # Note that you can write to output_file like so:
    # output_file.write("Hello world! \n")
    parser1 = Parser(input_file)
    table = SymbolTable()
    line = 0
    table_index = 16
    #firt loop - create symbol table
    while(parser1.has_more_commands()):
        if(parser1.command_type() == "L_COMMAND"):
            symbol = parser1.symbol()
            if(table.contains(symbol)):
                pass
            else:
                table.add_entry(symbol,line)
                parser1.advance()
                continue
        line +=1
        parser1.advance()
    #second loop
    parser1.reset()
    while(parser1.has_more_commands()):
        if(parser1.command_type() == "A_COMMAND"):
            if(parser1.symbol().isdigit()):
                symbol_num = int(parser1.symbol())
            else:
                if(table.contains(parser1.symbol())):
                    symbol_num = int(table.get_address(parser1.symbol()))
                else:
                    table.add_entry(parser1.symbol(), table_index)
                    symbol_num = table_index
                    table_index+=1
            output_file.write(chang_to_bin(symbol_num)+"\n")
        elif(parser1.command_type() == "L_COMMAND"):
            pass
        elif(parser1.command_type() == "C_COMMAND"):
            comp = parser1.comp()
            if(">>" in comp or "<<" in comp):
                comp = comp[1:]
                output_file.write(Code.comp(comp)+Code.dest(parser1.dest())+Code.jump(parser1.jump())+"\n")
            else:
                output_file.write("111"+Code.comp(comp)+Code.dest(parser1.dest())+Code.jump(parser1.jump())+"\n")
        parser1.advance()
    pass

def chang_to_bin(num):
    bin = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
    if (num >= 2**15):
        bin[0] = '1'
        num = num - (2**15)
    if num >= 2**14:
        bin[1] = '1'
        num = num - (2**14)
    if num >= 2**13:
        bin[2] = '1'
        num = num - (2**13)
    if num >= 2**12:
        bin[3] = '1'
        num = num - (2**12)
    if num >= 2**11:
        bin[4] = '1'
        num = num - (2**11)
    if num >= 2**10:
        bin[5] = '1'
        num = num - (2**10)
    if num >= 2**9:
        bin[6] = '1'
        num = num - (2**9)
    if num >= 2**8:
        bin[7] = '1'
        num = num - (2**8)
    if num >= 2**7:
        bin[8] = '1'
        num = num - (2**7)
    if num >= 2**6:
        bin[9] = '1'
        num = num - (2**6)
    if num >= 2**5:
        bin[10] = '1'
        num = num - (2**5)
    if num >= 2**4:
        bin[11] = '1'
        num = num - (2**4)
    if num >= 2**3:
        bin[12] = '1'
        num = num - (2**3)
    if num >= 2**2:
        bin[13] = '1'
        num = num - (2**2)
    if num >= 2**1:
        bin[14] = '1'
        num = num - (2**1)
    if num >= 2**0:
        bin[15] = '1'
        num = num - (2**0)
    bin = ''.join(bin)
    return str(bin)


if "__main__" == __name__:
    # Parses the input path and calls assemble_file on each input file.
    # This opens both the input and the output files!
    # Both are closed automatically when the code finishes running.
    # If the output file does not exist, it is created automatically in the
    # correct path, using the correct filename.
    if not len(sys.argv) == 2:
        sys.exit("Invalid usage, please use: Assembler <input path>")
    argument_path = os.path.abspath(sys.argv[1])
    if os.path.isdir(argument_path):
        files_to_assemble = [
            os.path.join(argument_path, filename)
            for filename in os.listdir(argument_path)]
    else:
        files_to_assemble = [argument_path]
    for input_path in files_to_assemble:
        filename, extension = os.path.splitext(input_path)
        if extension.lower() != ".asm":
            continue
        output_path = filename + ".hack"
        with open(input_path, 'r') as input_file, \
                open(output_path, 'w') as output_file:
            assemble_file(input_file, output_file)

    """input_path = "Shift.asm"
    output_path = "Shift.hack"
    with open(input_path, 'r') as input_file, \
                open(output_path, 'w') as output_file:
            assemble_file(input_file, output_file)"""