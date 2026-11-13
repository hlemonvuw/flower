from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import CobbDouglas

# figure settings
Config.load("econ-viz.toml").use()

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# italic x and y
cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
# five curves and one through the optimum
lvls = levels.around(eq.utility, n=5)
cvs.add_utility(model, levels=lvls)
# the line and its feasible set
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
# with the expansion path
cvs.add_equilibrium(eq, show_ray=True)
cvs.save("cobb_douglas.png")