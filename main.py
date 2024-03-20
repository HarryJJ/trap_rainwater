import random
import time

from trap_rainwater import DynamicProgrammingSolver, BruteForceSolver, TwoPointerSolver, TrapRainwaterStack


_ITERATIONS = 10000
_RANGE = 40


def main():

    solver_times = {
        DynamicProgrammingSolver: 0,
        BruteForceSolver: 0,
        TwoPointerSolver: 0,
        TrapRainwaterStack: 0
    }

    for iteration in range(_ITERATIONS):

        # Generate random heights list
        heights = [random.randint(0, 20) for _ in range(_RANGE)]

        # Creating instances of solvers
        solvers = [
            DynamicProgrammingSolver(heights),
            BruteForceSolver(heights),
            TwoPointerSolver(heights),
            TrapRainwaterStack(heights)
        ]

        for solver in solvers:
            start_time = time.time()
            water_trapped = solver.trap_rainwater()
            solver_times[solver.__class__] += time.time() - start_time
            #print(f"Amount of water trapped ({solver.__class__.__name__}): {water_trapped}")
            #print(f"Time taken ({solver.__class__.__name__}): {time.time() - start_time} seconds\n")

    for solver, total_time in solver_times.items():
        print(f'{solver} \n\tTotal Time: {total_time} \n\tAverage Time: {total_time/_ITERATIONS}\n')


if __name__ == "__main__":
    main()
