import difflib
import sys

def compare_python_scripts(file1_path, file2_path):
    """
    Compara dois arquivos e exibe suas diferenças, se houver.
    """
    try:
        # lendo os arquivos
        with open(file1_path, 'r') as file1:
            file1_lines = file1.readlines()

        with open(file2_path, 'r') as file2:
            file2_lines = file2.readlines()

        # comparando os arquivos
        diff = difflib.unified_diff(
            file1_lines, file2_lines,
            fromfile=f"File1: {file1_path}",
            tofile=f"File2: {file2_path}",
            lineterm=''
        )

        # mostrando as diferenças
        print("\n".join(diff))

    # disparando erros
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


compare_python_scripts('/Users/liviaalves/Workspace/useful-scripts/python_compare/script1.py', '/Users/liviaalves/Workspace/useful-scripts/python_compare/script2.py')
