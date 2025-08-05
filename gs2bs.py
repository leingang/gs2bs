#!/usr/bin/env python3

import re

import typer

def delete_displaystyle(line: str) -> str:
    """
    Deletes LaTeX displaystyle commands from the input line.
    The function uses a regular expression to find and remove the command.
    """
    pattern = r'\\displaystyle\s*'
    return re.sub(pattern, '', line)

def convert_delimiters(line:str) -> str:
    """
    Converts LaTeX delimiters from `$$...$$` to `\\(...\\)`.
    The function uses a nested function to process the matched content.
    """
    def replace_delimiters(match):
        content = match.group(1)
        return r"\( " + content.strip() + r" \)"

    # Pattern to match both $$...$$ and $...$
    pattern = r'\$\$(.*?)\$\$'
    return re.sub(pattern, lambda m: replace_delimiters(m), line)

def adjust_differential_spacing(line: str) -> str:
    """
    Convert strings like '\ dx' to '\,dx' for proper spacing in LaTeX.  
    """
    # Pattern to match '\ dx' and replace it with '\,dx'
    pattern = r'\\\s*d'
    return re.sub(pattern, r'\\,d', line)

def main(text: str) -> None:
    """
    Main function to read input text, filter, and display the converted text.
    """
    text = delete_displaystyle(text)
    text = adjust_differential_spacing(text)
    text = convert_delimiters(text)
    print(text)
    


if __name__ == "__main__":
    typer.run(main)