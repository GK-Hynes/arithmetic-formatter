def arithmetic_arranger(problems, bool=False):
    first_rows = ""
    second_rows = ""
    all_lines = ""
    answers = ""
    arranged_problems = ""

    for problem in problems:
        p = problem.split(" ")
        first_row = p[0]
        second_row = p[-1]
        operator = p[1]

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

        if bool == True:
            answer = str(eval(problem))
            answer = " " * (len(lines) - len(answer)) + answer
        else:
            answer = ""
            
        first_rows = first_rows + first_row + "   "
        second_rows = second_rows + second_row + "   "
        all_lines = all_lines + lines + "   "
        answers = answers + answer + "   "
    
    # print(first_rows)
    # print(second_rows)
    # print(all_lines)

    if bool == True:
        arranged_problems = first_rows + "\n" + second_rows + "\n" + all_lines + "\n" + answers
    else:
        arranged_problems = first_rows + "\n" + second_rows + "\n" + all_lines + "\n"
    print(arranged_problems)
        # return arranged_problems


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)