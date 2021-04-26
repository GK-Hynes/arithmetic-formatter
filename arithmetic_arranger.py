def arithmetic_arranger(problems):
    # Input
    # ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

    # Output
    #    32      3801      45      123
    # + 698    -    2    + 43    +  49
    # -----    ------    ----    -----
    first_rows = ""
    second_rows = ""
    all_lines = ""
    # operators = ""
    # answers = ""
    arranged_problems = ""

    for problem in problems:
        p = problem.split(" ")
        first_row = p[0]
        second_row = p[-1]
        operator = p[1]
        # print(f"First {first_row} - second {second_row} - operator {operator}")

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
            
        first_rows = first_rows + first_row + "   "
        second_rows = second_rows + second_row + "   "
        all_lines = all_lines + lines + "   "
    
    print(first_rows)
    print(second_rows)
    print(all_lines)
    arranged_problems = first_rows + "\n" + second_rows + "\n" + all_lines + "\n"
    # print(arranged_problems)
        # return arranged_problems

# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])