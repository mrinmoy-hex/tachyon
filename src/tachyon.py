import sys

class Lox:
    had_error = False
    @staticmethod
    def main():
        if len(sys.argv) > 2:
            print("Usage python lox.py [script]")
            sys.exit(64)
        elif len(sys.argv) == 2:
            Lox.run_file(sys.argv[1])
            print(sys.argv[1])
        else:
            # for REPL [Read a line of input, Evaluate it, Print the result, then Loop and do it all over again.] mode
            Lox.run_prompt()


    @staticmethod
    def run_file(file):
        pass

    @staticmethod
    def run_prompt():
        pass

if __name__ == "__main__":
    Lox.main()