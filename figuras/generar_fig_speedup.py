"""
Genera fig_speedup.png: speedup experimental (S) de la transformacion T5
(Ordenamiento y Top-20, foco individual TA-IND-04) frente a la curva
teorica de Amdahl, con el parametro p ajustado sobre la medicion en N=4.

Elaboracion propia. Fuente de los datos:
  Repositorio: https://github.com/ffarinangog2/pe-u4-spark-equipo-c
  Commit: 3a0ae757b6f8288bf095905e286bca75d8026a36 (rama main)
  Archivo: resultados/tiempos_resumen.csv (T5, executors[1,2,4])
"""
import numpy as np
import matplotlib.pyplot as plt

T_spark = {1: 1.563247100, 2: 1.173254300, 4: 1.356484800}
S_med = {N: T_spark[1] / T_spark[N] for N in [1, 2, 4]}

S4 = S_med[4]
p = (1 - 1 / S4) / 0.75  # ajuste de un solo punto (N=4)

def S_amdahl(N, p):
    return 1 / ((1 - p) + p / N)

N_cont = np.linspace(1, 4, 200)
S_teo_cont = [S_amdahl(N, p) for N in N_cont]

fig, ax = plt.subplots(figsize=(6.5, 4.2), dpi=300)
ax.plot(N_cont, S_teo_cont, color="#1f4e79", linewidth=2,
        label=f"Ley de Amdahl ($p={p:.4f}$, ajuste en $N=4$)")
Ns = [1, 2, 4]
Svals = [S_med[N] for N in Ns]
ax.plot(Ns, Svals, "o", color="#c0392b", markersize=8, zorder=5,
        label="Speedup experimental $S(N)$ — T5 (Top-20)")
for N in Ns:
    ax.annotate(f"{S_med[N]:.3f}", (N, S_med[N]),
                textcoords="offset points", xytext=(6, 6), fontsize=9)

ax.axhline(1, color="gray", linewidth=0.7, linestyle=":")
ax.set_xlabel("Número de unidades de procesamiento $N$ (executors)")
ax.set_ylabel("Speedup $S(N)$")
ax.set_title("T5 — Ordenamiento y Top-20: speedup experimental vs. Amdahl")
ax.set_xticks([1, 2, 3, 4])
ax.legend(loc="lower right", fontsize=8.5)
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("fig_speedup.png", dpi=300)
print("OK: fig_speedup.png (T5) generada")
