def validate_data(problem):
  #Check if both numbers are digits
  try:
    int(problem[0])
    int(problem[2])
  except:
    return "Error: Numbers must only contain digits."

  #Check if both numbers length is < 4
  try:
    if len(problem[0]) > 4 or len(problem[2]) > 4:
      raise BaseException
  except:
    return "Error: Numbers cannot be more than four digits."

  #Check if operator is valid
  try:
    if problem[1] != '+' and problem[1] != '-':
      raise BaseException
  except:
    return "Error: Operator must be '+' or '-'."

  #Return True if data is validated
  return True

def arithmetic_arranger(problems, showAnswer=False):
  arranged_problems = 0
  line1=line2=line3=line4 = ""
  problem_gap = " " * 4 
  #Check Problem Count
  try:
    if len(problems) > 5:
      raise BaseException
  except:
    return "Error: Too many problems."

  #Handle each problem
  for problem in problems:
    part = problem.split()
    #Validate problems
    valid = validate_data(part)
    if valid != True:
      return valid

    #Arrange Problems 
    space = max(len(part[0]),len(part[2])) + 2
    if len(line1) > 0:
      line1 += problem_gap
      line2 += problem_gap
      line3 += problem_gap

    line1 += part[0].rjust(space)
    line2 += part[1] + part[2].rjust(space-1)
    line3 += '-' * (space)

    #If showAnswer is true
    if showAnswer:
      #Perform math
      if part[1] == '+':
        solution = int(part[0]) + int(part[2])
      else:
        solution = int(part[0]) - int(part[2])
    
      if len(line4) > 0:
        line4 += problem_gap
      line4 += str(solution).rjust(space)

  #Return Arranged Problems
  arranged_problems = line1 + "\n" + line2 + "\n" + line3
  if showAnswer:
    arranged_problems += "\n" + line4
  return arranged_problems