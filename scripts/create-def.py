import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print("Usage: python create-def.py input_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    try:
        process = subprocess.Popen(['cat', input_file], stdout=subprocess.PIPE)
        sed_command1 = subprocess.Popen(['sed', r's/\(@[0-9]*\)@.*/\1/;s/\(^.*\)\(@[0-9]*\)/\1\ =\ \1\2/;s/^mgl/wgl/;s/wgd//'], stdin=process.stdout, stdout=subprocess.PIPE)
        sed_command2 = subprocess.Popen(['sed', r's/; Check!!!.*$//; /lto_priv/d; /CallWndProc/d'], stdin=sed_command1.stdout, stdout=subprocess.PIPE)
        grep_command = subprocess.Popen(['grep', '-e', '^LIB', '-e', '^EXP', '-e', r"\ =\ "], stdin=sed_command2.stdout, stdout=subprocess.PIPE)
        
        output, _ = grep_command.communicate()
        print(output.decode('utf-8'), end='')
    
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
