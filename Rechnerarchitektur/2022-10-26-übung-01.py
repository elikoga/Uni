# %%
import sympy
from sympy import Symbol, init_printing, latex

init_printing(use_unicode=True)

# %%
cost_per_wafer = Symbol("\\text{Kosten-pro-Wafer}")
wafer_area = Symbol("\\rm{Waferfläche}")  # wafer_fläche
die_area = Symbol("\\rm{Diefläche}")  # die_fläche
defect_density = Symbol("\\rm{Defektdichte}")  # defekt_dichte
# alpha = Symbol("\\alpha")
alpha = 2

# %%
ausbeute = 1 / (
    (1 + ((defect_density * die_area) / alpha)) ** alpha
)  # yield = ausbeute
dies_per_wafer = wafer_area / die_area  # approximated
cost_per_die: sympy.Expr = cost_per_wafer / (dies_per_wafer * ausbeute)


# %%
cost_per_die = cost_per_die.expand()
cost_per_die = cost_per_die.simplify()
print(latex(cost_per_die))

# %%
