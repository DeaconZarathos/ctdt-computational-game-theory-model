# Modelado Teórico-Computacional y Formal de *Captain Tsubasa: Dream Team*

[![DOI](https://shields.io)](https://doi.org)
[![License](https://shields.io)](https://creativecommons.org)
[![Python](https://shields.io)](https://python.org)


Este repositorio contiene el código de simulación numérica y los modelos matemáticos complementarios del artículo:

> **Modelado Teórico-Computacional y Formal del Juego de Estrategia Digital: Análisis de Complejidad, Lógica Booleana y Teoría de Juegos en Captain Tsubasa: Dream Team**  
> **Autor:** Jaime Alexander Roa Escobar (Ingeniero Mecatrónico)  
> **Publicación Oficial (Zenodo):** [https://doi.org](https://doi.org)

---

## Contenido del Modelo

* **Complejidad Computacional:** Demostración de evaluación local en clase **FP / P** y optimización global de alineaciones en clase **NP-hard** (reducción desde MKP y QKP 0-1).
* **Lógica Booleana (SOP):** Circuito combinacional monótono de ventaja táctica esperada ($Q$).
* **Procesos Estocásticos y Estamina:** Ecuaciones en diferencias finitas para degradación física y función logística de Bradley-Terry ($\beta = 8.7 \times 10^{-7}$).
* **Teoría de Juegos y Faroleo:** Equilibrio de Nash en Estrategias Mixtas (EMEN) y utilidad percibida modulada por entropía de Shannon $H(\sigma_B)$.

## Ejecución Rápida

```bash
python simulacion_duelo_ctdt.py
```

## Cómo Citar este Trabajo

```bibtex
@techreport{roa_escobar_2026_ctdt,
  author       = {Roa Escobar, Jaime Alexander},
  title        = {{Modelado Teórico-Computacional y Formal del Juego de Estrategia Digital: Análisis de Complejidad, Lógica Booleana y Teoría de Juegos en Captain Tsubasa: Dream Team}},
  month        = nov,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v1},
  doi          = {10.5281/zenodo.24092046},
  url          = {https://doi.org}
}
```
