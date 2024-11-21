import sys

class Error:
    """
    A utility class for handling error reporting.
    """

    @staticmethod
    def report(line, pos_where, message):
        """
        Report an error message with details about the line and position.

        Args:
            line (int): Line number where the error occurred.
            pos_where (str): Position-specific details, if any.
            message (str): Description of the error.

        Outputs:
            The error message is printed to stderr.
        """
        print(f"[line {line}] Error{pos_where}: {message}", file=sys.stderr)
