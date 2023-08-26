import numpy as np
from matplotlib import pyplot as plt
import math
import scienceplots

plt.style.use("science")

plt.rcParams.update({"font.size": 26})
plt.rcParams.update({"legend.title_fontsize": 18})

letters = "abcdefghijklmn"
markers = ["o", "v", "^", "s", "d"]
colz = [
    "#377eb8",
    "#ff7f00",
    "#4daf4a",
    "#f781bf",
    "#a65628",
    "#984ea3",
    "#999999",
    "#e41a1c",
    "#dede00",
]

# dictionary with case as key and beam energy as values
yellow = {41: 165, 55: 180, 56: 150, 57: 131, 59: 110, 60: 150}
green = {54: 180}

# open file and store data in vectors
(
    case,
    At211,
    Bi212,
    Fr212,
    Rn212,
    Ra213_1,
    Ra213_2,
    Ra213_3,
    Fr213,
    Ra212,
    Ra214,
    Po211m,
    Po211,
    At212m,
    At212,
    Rn213,
    Fr214m,
    Fr214,
    Ra215,
) = np.genfromtxt("yellow_yields_sort.csv", delimiter=",", unpack=True, skip_footer=0)

# combine the data for Ra213
Ra213 = []
for i in range(len(Ra213_1)):
    Ra213.append(Ra213_1[i] + Ra213_2[i] + Ra213_3[i])

# dictionary to give each vector a string name
nuclei = {
    "$^{211}$Po": Po211,
    "$^{211m}$Po": Po211m,
    "$^{211}$At": At211,  #
    "$^{212}$Bi": Bi212,
    "$^{212}$At": At212,
    "$^{212m}$At": At212m,
    "$^{212}$Rn": Rn212,
    "$^{212}$Fr": Fr212,
    "$^{212}$Ra": Ra212,  #
    "$^{213}$Rn": Rn213,
    "$^{213}$Fr": Fr213,
    "$^{213}$Ra": Ra213,
    # "$^{213}$Ra(6521)": Ra213_1,
    # "$^{213}$Ra(6624)": Ra213_2,
    # "$^{213}$Ra(6732)": Ra213_3,  #
    "$^{214}$Fr": Fr214,
    # "$^{214m}$Fr": Fr214m,
    "$^{214}$Ra": Ra214,  #
    "$^{215}$Ra": Ra215,  #
}

# Make an energies vector and sort it in order for the plots.
"""
energy = []
for i in case:
    energy.append(yellow[int(i)])
energy.sort()
"""

#
for key in nuclei:
    vector = []
    vector = [i / 60 for i in nuclei[key]]
    nuclei[key] = vector

i = 0  # Counter for figure styles

# Define the figure with enough axes
masses = [211, 212, 213, 214, 215]
fig, axes = plt.subplots(
    math.ceil(len(masses) / 2),
    2,
    figsize=(14, 24),
    sharex=True,
    sharey=True,
    gridspec_kw={"hspace": 0, "wspace": 0},
)
m = -1  # Counter for mass figure

el_colour = {
    "Bi": "C6",
    "Po": "C1",
    "At": "C2",
    "Rn": "C3",
    "Fr": "C4",
    "Ra": "C0",
}
el_marker = {"Bi": "x", "Po": "o", "At": "v", "Rn": "^", "Fr": "s", "Ra": "d"}

for mass in masses:
    m += 1
    ax = axes[int(m / 2), m % 2]
    textpos = (110, 5.25) if m % 2 != 0 else (155, 5.25)
    legendtitle = "(" + letters[m] + ") A=" + str(mass)
    ax.set_ylim(-0.25, 5.99)

    for name in nuclei:
        # Only take the nuclei with the selected mass number
        if str(mass) not in name:
            continue

        # Use the same style for isomers than for g.s.
        if "m" in name:
            i -= 1
            line = "--"
            colour = "white"
        else:
            line = "-"
            colour = el_colour[name[-2:]]

        ax.plot(
            case,
            nuclei[name],
            marker=el_marker[name[-2:]],
            markersize=8,
            linestyle=line,
            linewidth=2.5,
            color=el_colour[name[-2:]],
            label=name,
            markerfacecolor=colour,
        )

        i += 1
    i = 0
    ax.grid(True)
    legendpos = "upper right"
    ax.legend(fontsize="x-small", loc=legendpos, ncol=2)
    ax.text(110, 5.4, legendtitle)

fig.supylabel("Yield [10$^{-3}$ Counts/(s pnA)]")
fig.text(0.35, 0.07, "Recoil Exit Energy [MeV]", fontsize=28)
plt.savefig("Bi_Yields.pdf", transparent=True, bbox_inches="tight")
