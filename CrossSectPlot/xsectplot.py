from matplotlib import pyplot as plt
import scienceplots

plt.style.use("science")
lebBlue = "#2c60a0"
lebOrange = "#e95858"

nuclei = [
    "$^{211}$Po",
    "$^{212}$At",
    "$^{212}$Rn",
    "$^{213}$Rn",
    "$^{213}$Fr",
    "$^{214}$Ra",
    "$^{214}$Fr",
    "$^{221}$Ac",
    "$^{221}$Fr",
    "$^{221}$Ra",
    "$^{223}$Ac",  #
    "$^{224}$Pa",  #
    "$^{226}$Th",  #
]


JRnum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
JR = [2.9, 1.6, 2.7, 2.2, 1.8, 0.4, 0.6, 1.6, 1.5, 2.1, 1.9, 1.0, 2.4]
JRerr = [0.2, 0.1, 0.2, 0.2, 0.2, 0.1, 0.1, 0.2, 0.3, 0.3, 0.3, 0.2, 0.3]
UJnum = [1, 2, 4, 5, 6, 7]
UJ = [2.9, 1.2, 3.4, 1.7, 0.3, 0.5]

fig, ax = plt.subplots()

ax.plot(UJnum, UJ, "s", color="black", label="RITU [1]")
ax.errorbar(
    JRnum,
    JR,
    yerr=JRerr,
    linestyle="",
    marker="D",
    markersize=3,
    capsize=2,
    color=lebOrange,
    label="MARA [2]",
)
ax.grid()
ax.legend(fontsize="small", title="Data taken at")
ax.set_xticks(JRnum, minor=False, labels=nuclei, rotation=60)
ax.xaxis.set_tick_params(which="minor", length=0, color="r")

ax.set_ylabel("Cross Section [µb]")
ax.set_ylim(0, 4)
ax.set_xlim(0, len(JRnum) + 1)
ax.vlines(7.5, ymin=0, ymax=5, linestyle="-", color="black", linewidth=0.5)

fig.savefig("xsect-compare.pdf", transparent=True, bbox_inches="tight")
