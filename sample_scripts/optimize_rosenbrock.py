# %%
# imports
from skopt import gp_minimize
from scipy.optimize import rosen


# %%
# show some sample outputs of the rosenbrock function
for i in [
        [1.5, -1.5, .5],
        [0, .2, 2],
        [0,0,0]]:
    print(f'Sample rosenbrock evaluation: {i}\t-> {rosen(i)}')

print()


# %%
# optimize the rosenbrock function as an example
results = gp_minimize(
        func = rosen,
        dimensions = [(-2.0, 2.0), (-4.0, 6.0), (1.0, 3.0)],
        n_initial_points = 10,
        n_calls=25,
        x0 = [-1.0, 5.0, 2.5],
        random_state = 100)

print(f"""
results summary:
{results.x}
""")
