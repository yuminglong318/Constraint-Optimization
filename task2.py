from ortools.sat.python import cp_model

# Variables
num_vals = 9  # For a 9x9 Sudoku

# Create the model
model = cp_model.CpModel()


grid = [[model.NewIntVar(1, num_vals, f'grid[{i}][{j}]') for j in range(num_vals)] for i in range(num_vals)]

# Constraints
# Row Constraints
for i in range(num_vals):
  model.AddAllDifferent(grid[i])

# Column Constraints
for j in range(num_vals):
  model.AddAllDifferent([grid[i][j] for i in range(num_vals)])

# 3x3 Constraints
for i in range(0, num_vals, 3):
  for j in range(0, num_vals, 3):
    model.AddAllDifferent([grid[i0][j0] for i0 in range(i, i + 3) for j0 in range(j, j + 3)])

# Given Cells
model.Add(grid[0][7] == 3)
model.Add(grid[1][0] == 7)
model.Add(grid[1][2] == 5)
model.Add(grid[1][4] == 2)
model.Add(grid[2][1] == 9)
model.Add(grid[2][6] == 4)
model.Add(grid[3][5] == 4)
model.Add(grid[3][8] == 2)
model.Add(grid[4][1] == 5)
model.Add(grid[4][2] == 9)
model.Add(grid[4][3] == 6)
model.Add(grid[4][8] == 8)
model.Add(grid[5][0] == 3)
model.Add(grid[5][4] == 1)
model.Add(grid[5][7] == 5)
model.Add(grid[6][0] == 5)
model.Add(grid[6][1] == 7)
model.Add(grid[6][4] == 6)
model.Add(grid[6][6] == 1)
model.Add(grid[7][3] == 3)
model.Add(grid[8][0] == 6)
model.Add(grid[8][3] == 4)
model.Add(grid[8][8] == 5)

# Solve and Print
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
    for i in range(num_vals):
        print(' '.join([str(x) for x in [int(solver.Value(grid[i][j])) for j in range(num_vals)]]))

else:
    print('no solution')
