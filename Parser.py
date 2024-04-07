"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing


class Parser:
    """Encapsulates access to the input code. Reads an assembly program
    by reading each command line-by-line, parses the current command,
    and provides convenient access to the commands components (fields
    and symbols). In addition, removes all white space and comments.
    """

    def __init__(self, input_file: typing.TextIO) -> None:
        """Opens the input file and gets ready to parse it.

        Args:
            input_file (typing.TextIO): input file.
        """
        # A good place to start is to read all the lines of the input:
        # input_lines = input_file.read().splitlines()
        self._file = input_file.read().splitlines()
        i=len(self._file)-1
        while(i>=0):
            #serach for cmd in line
            has_cmd = self._file[i].find("//")
            if(has_cmd != -1):
                #delete cmd from line
                self._file[i] = self._file[i][:has_cmd]
            #delete speace
            self._file[i] = self._file[i].strip()
            #delete empty lines
            if(self._file[i] == ''):
                del self._file[i]
            i-=1
        #initialise line counter
        self._line = 0
        pass

    def has_more_commands(self) -> bool:
        """Are there more commands in the input?

        Returns:
            bool: True if there are more commands, False otherwise.
        """
        if(self._line < len(self._file)):
            return True
        return False

    def advance(self) -> None:
        """Reads the next command from the input and makes it the current command.
        Should be called only if has_more_commands() is true.
        """
        self._line += 1
        pass

    def command_type(self) -> str:
        """
        Returns:
            str: the type of the current command:
            "A_COMMAND" for @Xxx where Xxx is either a symbol or a decimal number
            "C_COMMAND" for dest=comp;jump
            "L_COMMAND" (actually, pseudo-command) for (Xxx) where Xxx is a symbol
        """
        #A command
        if(self._file[self._line][0] == "@"):
            return "A_COMMAND"
        #L command
        elif(self._file[self._line][0] == "("):
            return "L_COMMAND"
        return "C_COMMAND"

    def symbol(self) -> str:
        """
        Returns:
            str: the symbol or decimal Xxx of the current command @Xxx or
            (Xxx). Should be called only when command_type() is "A_COMMAND" or 
            "L_COMMAND".
        """
        cmd = self.command_type()
        symbol = self._file[self._line]
        if(cmd == "A_COMMAND"):
            symbol = symbol[1:]
        elif(cmd == "L_COMMAND"):
            symbol = symbol[1:len(self._file[self._line])-1]
        return symbol

    def dest(self) -> str:
        """
        Returns:
            str: the dest mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        dest = 0
        if("=" in self._file[self._line]):
            dest = self._file[self._line].find("=")
        return self._file[self._line][:dest]

    def comp(self) -> str:
        """
        Returns:
            str: the comp mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        #dest = 0
        #if("=" in self._file[self._line]):
        #    dest = self._file[self._line].find("=")    
        dest = self._file[self._line].find("=")
        comp = len(self._file[self._line])
        if(";" in self._file[self._line]):
            comp = self._file[self._line].find(";")
        return self._file[self._line][dest+1:comp]

    def jump(self) -> str:
        """
        Returns:
            str: the jump mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        #comp = len(self._file[self._line]) -1
        #if(";" in self._file[self._line]):
        #    comp = self._file[self._line].find(";")
        #return self._file[self._line][comp+1:]
        comp = self._file[self._line].find(";")
        return self._file[self._line][comp+1:]


    def reset(self) -> None:
        self._line = 0
        pass