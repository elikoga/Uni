<script lang="ts">
  type CellValue = number | null;
  type SudokuGrid = CellValue[][];

  let sudokuGrid: SudokuGrid = $state(Array(9)
    .fill(null)
    .map(() => Array(9).fill(null)));

  const resetSudoku = () => {
    sudokuGrid = Array(9)
      .fill(null)
      .map(() => Array(9).fill(null));
  };



  const findEmptyCell = (grid: SudokuGrid): [number, number] | null => {
    for (let row = 0; row < 9; row++) {
      for (let col = 0; col < 9; col++) {
        if (grid[row][col] === null) {
          return [row, col];
        }
      }
    }
    return null;
  };

  const isPartialValid = (
    grid: SudokuGrid,
    row: number,
    col: number,
    value: number
  ): boolean => {
    // Check row
    for (let c = 0; c < 9; c++) {
      if (grid[row][c] === value && c !== col) {
        console.log(`1Invalid value ${value} at row ${row}, col ${c}`);
        return false;
      }
    }
    // Check column
    for (let r = 0; r < 9; r++) {
      if (grid[r][col] === value && r !== row) {
        console.log(`2Invalid value ${value} at row ${r}, col ${col}`);
        return false;
      }
    }
    // Check box
    const boxRowStart = Math.floor(row / 3) * 3;
    const boxColStart = Math.floor(col / 3) * 3;
    for (let r = boxRowStart; r < boxRowStart + 3; r++) {
      for (let c = boxColStart; c < boxColStart + 3; c++) {
        if (grid[r][c] === value && (r !== row || c !== col)) {
          console.log(`3Invalid value ${value} at row ${r}, col ${c}`);
          return false;
        }
      }
    }
    return true;
  };

  const isFullyValid = (grid: SudokuGrid): boolean => {
    for (let row = 0; row < 9; row++) {
      for (let col = 0; col < 9; col++) {
        const value = grid[row][col];
        if (value !== null) {
          // Check if the value is valid in its position
          if (!isPartialValid(grid, row, col, value)) {
            console.log(`Invalid value ${value} at row ${row}, col ${col}`);
            return false;
          }
        }
      }
    }
    return true;
  };



  const makeStep = () => {
    // later
  };

  const solveFully = () => {
    const solve = (grid: SudokuGrid): boolean => {
      console.log(`Solving... Current grid: ${JSON.stringify(grid)}`);
      const emptyCell = findEmptyCell(grid);
      if (!emptyCell) {
        return isFullyValid(grid);
      }
      const [row, col] = emptyCell;

      // if not fully valid, return false
      if (!isFullyValid(grid)) {
        console.log(`Invalid grid at row ${row}, col ${col}`);
        return false;
      }

      for (let num = 1; num <= 9; num++) {
        if (isPartialValid(grid, row, col, num)) {
          grid[row][col] = num; // Place the number
          if (solve(grid)) {
            return true; // If solved, return true
          }
          grid[row][col] = null; // Backtrack
        }
      }
      return false;
    };
    const isSolved = solve(sudokuGrid);
    if (isSolved) {
      alert("Sudoku solved!");
    } else {
      alert("No solution exists.");
    }
  };

  const generateNew = () => {};
</script>

<main>
  <div class="sudoku-container">
    <table class="sudoku-table">
      <tbody>
        {#each Array(9) as _, row}
          <tr>
            {#each Array(9) as _, col}
              <td
                class="sudoku-cell"
                class:right-border={col % 3 === 2 && col !== 8}
                class:bottom-border={row % 3 === 2 && row !== 8}
                class:left-border={col % 3 === 0 && col !== 0}
                class:top-border={row % 3 === 0 && row !== 0}
              >
                <input
                  type="number"
                  maxlength="1"
                  bind:value={sudokuGrid[row][col]}
                />
              </td>
            {/each}
          </tr>
        {/each}
      </tbody>
    </table>

    <div class="button-container">
      <button onclick={resetSudoku}>Reset</button>
      <button onclick={makeStep}>Make Step</button>
      <button onclick={solveFully}>Solve</button>
      <button onclick={generateNew}>New Puzzle</button>
    </div>
  </div>
</main>

<style>
  main {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f0f0f0;
  }

  .sudoku-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
    align-items: center;
  }

  .button-container {
    display: flex;
    gap: 10px;
    margin-top: 10px;
  }

  button {
    padding: 8px 16px;
    background-color: #4a90e2;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.2s;
  }

  button:hover {
    background-color: #357abd;
  }

  .sudoku-table {
    border-collapse: collapse;
    border: 3px solid #000;
  }

  .sudoku-cell {
    width: 40px;
    height: 40px;
    border: 1px solid #888;
    text-align: center;
    padding: 0;
  }

  .right-border {
    border-right: 3px solid #000;
  }

  .bottom-border {
    border-bottom: 3px solid #000;
  }

  .left-border {
    border-left: 3px solid #000;
  }

  .top-border {
    border-top: 3px solid #000;
  }

  input[type="text"] {
    width: 100%;
    height: 100%;
    border: none;
    text-align: center;
    font-size: 24px;
    background-color: transparent;
    box-sizing: border-box;
  }
</style>
