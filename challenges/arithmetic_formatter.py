def arithmetic_arranger(problems, result=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  operators = {
    '+': lambda pair: str(pair[0] + pair[1]),
    '-': lambda pair: str(pair[0] - pair[1]),
  }
  arranged_problems = []
  top = []
  bottom = []
  lines = []
  results = []

  for problem in problems:
    problems_array = problem.split()
    max_len = len(max(problems_array, key=len))

    if not all([i.isnumeric() for i in problems_array[::2]]):
      return "Error: Numbers must only contain digits."
    elif problems_array[1] not in operators.keys():
      return "Error: Operator must be '+' or '-'."
    elif max_len > 4:
      return "Error: Numbers cannot be more than four digits."

    line_len = max_len + 2

    line = '-' * line_len
    first_num = problems_array[0].rjust(line_len, ' ')
    second_num = f"{problems_array[1]}{' ' * (line_len - len(problems_array[2]) - 1)}{problems_array[2]}"

    top.append(first_num)
    bottom.append(second_num)
    lines.append(line)

    if result:
      res = operators[problems_array[1]]([int(i) for i in problems_array[::2]])
      results.append(f"{res.rjust(line_len, ' ')}")

  arranged_problems = '\n'.join(['    '.join(i) for i in (top, bottom, lines)])

  if results:
    arranged_problems += '\n' + '    '.join(results)

  return arranged_problems
