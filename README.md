# TA-IND-04 — Villamarín

Trabajo Autónomo Individual **TA-IND-04**: Análisis de Rendimiento Paralelo (Unidad 4) aplicado al Proyecto Fin de Curso, para la asignatura **Aplicaciones Distribuidas (ISR-701)**, Universidad Técnica Estatal de Quevedo (UTEQ), Facultad de Ciencias de la Computación, Carrera de Ingeniería de Software. Período académico 2026–2027 PPA. Docente: Gleiston C. Guerrero-Ulloa, M.Sc.

## Identificación

| Campo                                         | Valor                                                       |
| --------------------------------------------- | ----------------------------------------------------------- |
| Estudiante                                    | Iván Andrés Villamarín Cuenca                               |
| Equipo de PE-U4                               | Equipo C — Freddy Farinango, Jeremy Gaibor, Iván Villamarín |
| Transformación declarada como foco individual | **T5 — ordenamiento global y Top-20**                       |
| PFC de referencia                             | SCLI — Sistema de Control de Laboratorios Informáticos      |
| Repositorio de origen de los datos (PE-U4)    | <https://github.com/ffarinangog2/pe-u4-spark-equipo-c>      |
| Commit exacto de los datos base               | `3a0ae757b6f8288bf095905e286bca75d8026a36` (rama `main`)    |

## Estructura del repositorio

```
ta-ind-04-villamarin/
├── README.md                          <- este archivo
├── LICENSE
├── docs/
│   ├── TA_IND_04_Informe.tex          <- documento fuente LaTeX
│   ├── TA_IND_04_Informe.pdf          <- PDF compilado (committeado)
│   └── references.bib                <- bibliografía IEEE (biblatex)
├── datos/
│   ├── tiempos_base.csv               <- copia exacta de resultados/tiempos_resumen.csv (PE-U4, commit 3a0ae757)
│   └── tiempos_crudos.csv             <- copia exacta de resultados/tiempos_crudos.csv (PE-U4, commit 3a0ae757), incluye las 5 repeticiones de T5 en N=1,2,4
└── figuras/
    ├── fig_speedup.png                <- figura propia (300 DPI), incluida en el informe
    └── generar_fig_speedup.py         <- script de elaboración propia que genera fig_speedup.png
```

## Instrucciones exactas de compilación

Requiere una distribución TeX Live con `pdflatex` y `biber` (paquetes `IEEEtran`, `biblatex`, `siunitx`, `booktabs`, `tikz`, `babel-spanish`).

```bash
cd docs
pdflatex -interaction=nonstopmode TA_IND_04_Informe.tex
biber TA_IND_04_Informe
pdflatex -interaction=nonstopmode TA_IND_04_Informe.tex
pdflatex -interaction=nonstopmode TA_IND_04_Informe.tex
```

El resultado es `docs/TA_IND_04_Informe.pdf`. Se verificó que esta secuencia reproduce el PDF sin errores en un entorno limpio (Ubuntu 24.04 + TeX Live 2023, paquetes `texlive-publishers`, `texlive-lang-spanish`, `biber`).

Para regenerar la figura propia (opcional, ya está versionada en `figuras/fig_speedup.png`):

```bash
cd figuras
pip install matplotlib numpy
python3 generar_fig_speedup.py
```

## Trazabilidad de los datos

Todas las cifras numéricas del informe (tiempos, _speedup_, eficiencia, Karp-Flatt, ajuste de Amdahl y umbral de rentabilidad) se derivan exclusivamente de `datos/tiempos_base.csv` y `datos/tiempos_crudos.csv`, copias idénticas —verificadas byte a byte— de `resultados/tiempos_resumen.csv` y `resultados/tiempos_crudos.csv` en el commit `3a0ae757b6f8288bf095905e286bca75d8026a36` del repositorio de origen. No se generó, alteró ni corrigió ninguna cifra experimental. El detalle del cálculo (fórmulas y valores intermedios) está documentado en `docs/TA_IND_04_Informe.tex`, Secciones II–V.
