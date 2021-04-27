def arithmetic_arranger(problems, include_solution=False):
    first_nums = ""
    second_nums = ""
    all_lines = ""
    solutions = ""
    arranged_problems = ""

    # Limit problems to 5
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        # Generate rows
        parts = problem.split(" ")
        first_num = parts[0]
        second_num = parts[-1]
        operator = parts[1]

        # Make sure operator is + or -
        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."
        
        # Make sure operands only contain digits
        if not first_num.isdecimal() or not second_num.isdecimal():
            return "Error: Numbers must only contain digits."

        # Make sure numbers are no more than 4 digits
        if len(first_num) > 4 or len(second_num) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Start formatting
        if len(first_num) > len(second_num):
            second_num = operator + " " * (len(first_num) - len(second_num)) + " " + second_num
            lines = "-" * (len(first_num) + 2)
            first_num = " " * ((len(second_num) - len(first_num))) + first_num
        elif len(second_num) > len(first_num):
            first_num = " " * (len(second_num) - len(first_num)) + "  " + first_num
            lines = "-" * (len(second_num) + 2)
            second_num = operator + " " * (len(second_num) - len(first_num)) + " " + second_num
        else:
            second_num = operator + " " + second_num
            first_num = " " * 2 + first_num
            lines = "-" * len(second_num)

        # Check whether to generate solution
        if include_solution == True:
            solution = str(eval(problem))
            solution = " " * (len(lines) - len(solution)) + solution
        else:
            solution = ""
        
        # Assemble formatted rows
        first_nums = first_nums + first_num + "    "
        second_nums = second_nums + second_num + "    "
        all_lines = all_lines + lines + "    "
        solutions = solutions + solution + "    "

        # If last problem remove trailing whitespace
        if problem == problems[-1]:
            first_nums = first_nums.rstrip()
            second_nums = second_nums.rstrip()
            all_lines = all_lines.rstrip()
            solutions = solutions.rstrip()

    # Check whether to return problem solutions too
    if include_solution == True:
        arranged_problems = first_nums + "\n" + second_nums + "\n" + all_lines + "\n" + solutions
    else:
        arranged_problems = first_nums + "\n" + second_nums + "\n" + all_lines
    
    return arranged_problems
