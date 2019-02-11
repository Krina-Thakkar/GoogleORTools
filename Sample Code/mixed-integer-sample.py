from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
  solver = pywraplp.Solver('SolveIntegerProblem',
                           pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

  # c and t are integer non-negative variables.
  c = solver.IntVar(0.0, solver.infinity(), 'c')
  t = solver.IntVar(0.0, solver.infinity(), 't')

  # 6c + 7t <= 21
  constraint = solver.Constraint(-solver.infinity(), 21)
  constraint.SetCoefficient(c, 6)
  constraint.SetCoefficient(t, 7)

  # Maximize 12c + 13t
  objective = solver.Objective()
  objective.SetCoefficient(c, 12)
  objective.SetCoefficient(t, 13)
  objective.SetMaximization()

  """Solve the problem and print the solution."""
  result_status = solver.Solve()
  # The problem has an optimal solution.
  assert result_status == pywraplp.Solver.OPTIMAL

  # The solution looks legit (when using solvers other than
  # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
  assert solver.VerifySolution(1e-7, True)

  print('Number of variables =', solver.NumVariables())
  print('Number of constraints =', solver.NumConstraints())

  # The objective value of the solution.
  print('Optimal objective value = %d' % solver.Objective().Value())
  print()
  # The value of each variable in the solution.
  variable_list = [c, t]

  for variable in variable_list:
    print('%s = %d' % (variable.name(), variable.solution_value()))

if __name__ == '__main__':
  main()




  