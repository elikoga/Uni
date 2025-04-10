<script lang="ts">
  let sudokuGrid: (number | null)[][] = Array(9)
    .fill(null)
    .map(() => Array(9).fill(null));

  function resetSudoku(): void {
    sudokuGrid = Array(9)
      .fill(null)
      .map(() => Array(9).fill(null));
  }

  function makeStep(): void {
    // TODO: Implement a single solution step
    console.log("Making one solution step");
  }

  function solveFully(): void {
    // TODO: Implement full solution algorithm
    console.log("Solving the sudoku completely");
  }

  function generateNew(): void {
    // TODO: Implement sudoku generation
    console.log("Generating a new sudoku puzzle");
  }
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
                  type="text"
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
      <button on:click={resetSudoku}>Reset</button>
      <button on:click={makeStep}>Make Step</button>
      <button on:click={solveFully}>Solve</button>
      <button on:click={generateNew}>New Puzzle</button>
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
