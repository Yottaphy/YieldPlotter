import numpy as np
from matplotlib import pyplot as plt
import math

plt.rcParams.update({"font.size": 26})
plt.rcParams.update({"legend.title_fontsize": 18})
plt.rcParams.update({"font.family": "Latin Modern Roman"})
plt.rcParams.update({"mathtext.fontset": "cm"})

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
# yellow = {41: 165, 55: 180, 56: 150, 57: 131, 59: 110, 60: 150}
# green = {54: 180}

# open file and store data in vectors
(
    energy,
    Th219,
    Fr220,
    Ra220,
    Ac220,
    Rn221,
    Fr221,
    Ra221,
    Ac221,
    Ra222,
    Ac222,
    Pa222,
    Ac223,
    Th223,
    Pa223,
    Th224,
    Pa224,
    Th225,
    Th226,
    _,
) = np.genfromtxt("pink_yields.csv", delimiter=",", unpack=True, skip_footer=0)

# dictionary to give each vector a string name
nuclei = {
    "$^{219}$Th": Th219,
    "$^{220}$Fr": Fr220,
    "$^{220}$Ra": Ra220,
    "$^{220}$Ac": Ac220,
    "$^{221}$Rn": Rn221,
    "$^{221}$Fr": Fr221,
    "$^{221}$Ra": Ra221,
    "$^{221}$Ac": Ac221,
    "$^{222}$Ra": Ra222,
    "$^{222}$Ac": Ac222,
    "$^{222}$Pa": Pa222,
    "$^{223}$Ac": Ac223,
    "$^{223}$Th": Th223,
    "$^{223}$Pa": Pa223,
    "$^{224}$Th": Th224,
    "$^{224}$Pa": Pa224,
    "$^{225}$Th": Th225,
    "$^{226}$Th": Th226,
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
masses = np.arange(219, 227)
fig, axes = plt.subplots(
    math.ceil(len(masses) / 2),
    2,
    figsize=(14, 24),
    sharex=True,
    sharey=True,
    gridspec_kw={"hspace": 0, "wspace": 0},
)
m = -1  # Counter for mass figure

for mass in masses:
    m += 1
    ax = axes[int(m / 2), m % 2]
    textpos = (110, 5.25) if m % 2 != 0 else (155, 5.25)
    legendpos = "upper left"
    legendtitle = "(" + letters[m] + ") A=" + str(mass)
    ax.set_ylim(-0.1, 1.24)

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
            colour = colz[i]

        ax.plot(
            energy,
            nuclei[name],
            marker=markers[i % 5],
            markersize=8,
            linestyle=line,
            linewidth=2.5,
            color=colz[i],
            label=name,
            markerfacecolor=colour,
        )

        i += 1
    i = 0
    ax.legend(fontsize="x-small", loc=legendpos, ncol=3)  # title=legendtitle )
    ax.grid(True)

fig.supylabel("Yield [10$^{-3}$ Counts/(s pnA)]")
fig.text(0.35, 0.07, "Recoil Exit Energy [MeV]", fontsize=28)
plt.savefig("U_Yields.pdf", transparent=True, bbox_inches="tight")
