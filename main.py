class NumericError(Exception):
    """
    Class of errors associated with NumericFormatter
    """
    pass


class NumericFormatter:
    def parseInt(self, string: str):
        """
        Сonverts a string integer value to numeric format.
        Params:
            string (str): string of integer values

            Conditions:
            1) The string must contain positive and negative numeric values in string format from
            range [0-9] and arithmetic signs [‘+’, ‘-’] in front of a numeric value
            2)  The string should not contain decimal numbers
            3) The string must not be empty
            4) Length of the input string: 2 ≤ |s| ≤ 2^32-1
            If the conditions are not met, then errors are possible

        Return:
            integer (int): integer converted from string
        """
        if type(string) != str:
            raise NumericError("Type must be str()")
        try:
            integer = int(string)
            if len(string) not in range(2, (2**32-1)):
                raise NumericError("String length  out of range")
        except ValueError:
            raise NumericError("Invalid input") from None
        return integer
