def arithmetic_arranger(problems, bool=False):
    first_rows = ""
    second_rows = ""
    all_lines = ""
    answers = ""
    arranged_problems = ""

    # Limit problems to 5
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        # Generate rows
        parts = problem.split(" ")
        first_row = parts[0]
        second_row = parts[-1]
        operator = parts[1]

        # Make sure operator is + or -
        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."
        
        # Make sure operands only contain digits
        if not first_row.isdecimal() or not second_row.isdecimal():
            return "Error: Numbers must only contain digits."

        # Make sure numbers are no more than 4 digits
        if len(first_row) > 4 or len(second_row) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Start formatting
        if len(first_row) > len(second_row):
            second_row = operator + " " * (len(first_row) - len(second_row)) + " " + second_row
            lines = "-" * (len(first_row) + 2)
            first_row = " " * ((len(second_row) - len(first_row))) + first_row
        elif len(second_row) > len(first_row):
            first_row = " " * (len(second_row) - len(first_row)) + "  " + first_row
            lines = "-" * (len(second_row) + 2)
            second_row = operator + " " * (len(second_row) - len(first_row)) + " " + second_row
        else:
            second_row = operator + " " + second_row
            first_row = " " * 2 + first_row
            lines = "-" * len(second_row)

        # Check whether to generate answers
        if bool == True:
            answer = str(eval(problem))
            answer = " " * (len(lines) - len(answer)) + answer
        else:
            answer = ""
        
        # Assemble formatted rows
        first_rows = first_rows + first_row + "    "
        second_rows = second_rows + second_row + "    "
        all_lines = all_lines + lines + "    "
        answers = answers + answer + "    "

    # Check whether to return problem answers too
    if bool == True:
        arranged_problems = first_rows + "\n" + second_rows + "\n" + all_lines + "\n" + answers
    else:
        arranged_problems = first_rows + "\n" + second_rows + "\n" + all_lines + "\n"
    print(arranged_problems)
    # return arranged_problems


arithmetic_arranger(["32 + 68", "301 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)