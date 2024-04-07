"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""


class Code:
    """Translates Hack assembly language mnemonics into binary codes."""
    
    @staticmethod
    def dest(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a dest mnemonic string.

        Returns:
            str: 3-bit long binary code of the given mnemonic.
        """
        if("A" in mnemonic):
            a = "1"
        else:
            a= "0"
        if("D" in mnemonic):
            d = "1"
        else:
            d = "0"
        if("M" in mnemonic):
            m = "1"
        else:
            m = "0"
        return a+d+m

    @staticmethod
    def comp(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a comp mnemonic string.

        Returns:
            str: the binary code of the given mnemonic.
        """
        if(mnemonic == "0"):
            return "0101010"
        if(mnemonic == "1"):
            return "0111111"
        if(mnemonic == "-1"):
            return "0111010"
        if(mnemonic == "D"):
            return "0001100"
        if(mnemonic == "A"):
            return "0110000"
        if(mnemonic == "M"):
            return "1110000"
        if(mnemonic == "!D"):
            return "0001101"
        if(mnemonic == "!A"):
            return "0110001"
        if(mnemonic == "!M"):
            return "1110001"
        if(mnemonic == "-D"):
            return "0001111"
        if(mnemonic == "-A"):
            return "0110011"
        if(mnemonic == "-M"):
            return "1110011"
        if(mnemonic == "D+1"):
            return "0011111"
        if(mnemonic == "A+1"):
            return "0110111"
        if(mnemonic == "M+1"):
            return "1110111"
        if(mnemonic == "D-1"):
            return "0001110"
        if(mnemonic == "A-1"):
            return "0110010"
        if(mnemonic == "M-1"):
            return "1110010"
        if(mnemonic == "D+A"):
            return "0000010"
        if(mnemonic == "D+M"):
            return "1000010"
        if(mnemonic == "D-A"):
            return "0010011"
        if(mnemonic == "D-M"):
            return "1010011"
        if(mnemonic == "A-D"):
            return "0000111"
        if(mnemonic == "M-D"):
            return "1000111"
        if(mnemonic == "D&A"):
            return "0000000"
        if(mnemonic == "D&M"):
            return "1000000"
        if(mnemonic == "D|A"):
            return "0010101"
        if(mnemonic == "D|M"):
            return "1010101"
        if(mnemonic == "A<<"):
            return "1010100000"
        if(mnemonic == "D<<"):
            return "1010110000"
        if(mnemonic == "M<<"):
            return "1011100000"
        if(mnemonic == "A>>"):
            return "1010000000"
        if(mnemonic == "D>>"):
            return "1010010000"
        if(mnemonic == "M>>"):
            return "1011000000"
        pass

    @staticmethod
    def jump(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a jump mnemonic string.

        Returns:
            str: 3-bit long binary code of the given mnemonic.
        """
        if(mnemonic == "JGT"):
            return "001"
        if(mnemonic == "JEQ"):
            return "010"
        if(mnemonic == "JGE"):
            return "011"
        if(mnemonic == "JLT"):
            return "100"
        if(mnemonic == "JNE"):
            return "101"
        if(mnemonic == "JLE"):
            return "110"
        if(mnemonic == "JMP"):
            return "111"
        return "000"
