import sys
from utils import Error
from lexer import Lexer

class Tachyon:
    had_error = False
    @staticmethod
    def main():
        if len(sys.argv) > 2:
            print("Usage python tachyon [script]")
            sys.exit(64)
        elif len(sys.argv) == 2:
            Tachyon.run_file(sys.argv[1])
            print(sys.argv[1])
        else:
            # for REPL [Read a line of input, Evaluate it, Print the result, then Loop and do it all over again.] mode
            Tachyon.run_prompt()


    @staticmethod
    def run_file(path):
        try:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                Tachyon.run(content)

        except IOError as e:
            print(f"Error reading file: {e}")
            exit(64)    # std exit code i found

        # indicate an error in the exit code
        if Tachyon.had_error:
            sys.exit(64)


    # REPL mode
    @staticmethod
    def run_prompt():
        print("Tachyon REPL (type 'exit' to quit)")
        while True:
            line = input("> ")
            if line == "" or line == "exit":
                break
            Tachyon.run(line)
            Tachyon.had_error = False

    # running the contents
    @staticmethod
    def run(source):
        lexer = Lexer(source)
        tokens = lexer.scan_tokens()

        # for now, just print the tokens
        for token in tokens:
            print(token)

    # Forwarding errors to the Error class
    @staticmethod
    def error(line, message):
        Error.report(line, "", message)
        Tachyon.had_error = True


if __name__ == "__main__":
    Tachyon.main()





