import math
import random

BETA = 8.7e-7  # Constante de calibración MLE del motor


def evaluacion_booleana_sop(c_adv: int, h_act: int, e_opt: int,
                            p_crit: int, v_com: int, s_sup: int) -> int:
    """Evalúa la ventaja táctica esperada Q en Suma de Productos (Sección 4.2)."""
    t1 = h_act and c_adv and e_opt and v_com
    t2 = p_crit and h_act and e_opt
    t3 = c_adv and v_com and s_sup
    t4 = e_opt and h_act and s_sup
    return int(bool(t1 or t2 or t3 or t4))


def calcular_stat_efectiva(stat_base_ajustada: float, stat_fisica_ajustada: float,
                           mult_pasivas: float = 1.0) -> float:
    """Calcula Statefectiva(X) según la Sección 5.2 y 7.1."""
    return (stat_base_ajustada + 0.5 * stat_fisica_ajustada) * mult_pasivas


def actualizar_estamina(e_actual: float, lambda_base: float, costo_skill: float,
                        alpha: float, presion: float) -> float:
    """Ecuación en diferencias finitas para consumo de estamina (Sección 5.1)."""
    desgaste = (lambda_base + costo_skill) * (1.0 + alpha * presion)
    return max(0.0, e_actual - desgaste)


def factor_estamina(e_actual: float, e_max: float) -> float:
    """Penalización funcional F_stam(t) con piso mínimo de 0.50."""
    return max(0.50, e_actual / e_max)


def fuerza_accion(stat_efectiva: float, momentum: int, m_tipo: float,
                  f_stam: float, c_crit: float, ruido_relativo: float = 0.0) -> float:
    """Calcula FA_base y aplica fluctuación estocástica epsilon."""
    fa_base = stat_efectiva * momentum * m_tipo * f_stam * c_crit
    return fa_base * (1.0 + ruido_relativo)


def probabilidad_victoria(fa_atacante: float, fa_defensor: float, beta: float = BETA) -> float:
    """Función sigmoide logística de Bradley-Terry (Sección 5.3)."""
    delta_fa = fa_atacante - fa_defensor
    return 1.0 / (1.0 + math.exp(-beta * delta_fa))


def entropia_shannon(distribucion_rival: list[float]) -> float:
    """Calcula H(sigma_B) en bits para el modelo de faroleo (Sección 6.2)."""
    return -sum(q * math.log2(q) for q in distribucion_rival if q > 0)


if __name__ == "__main__":
    # Parámetros del caso de estudio (Sección 7.1): Tsubasa Ozora vs Deuter Müller
    stat_tsubasa = calcular_stat_efectiva(34500, 30000)  # 49,500
    stat_muller = calcular_stat_efectiva(33800, 28000)   # 47,800

    # Escenario A: Duelo estándar sin críticos (C_crit = 1.0, epsilon = 0)
    fa_tsubasa_a = fuerza_accion(stat_tsubasa, momentum=510, m_tipo=1.15, f_stam=1.00, c_crit=1.0)
    fa_muller_a = fuerza_accion(stat_muller, momentum=500, m_tipo=1.00, f_stam=1.00, c_crit=1.0)
    p_gol_a = probabilidad_victoria(fa_tsubasa_a, fa_muller_a)

    # Escenario B: Crítico Dorado de Müller (C_crit = 1.5, epsilon = 0)
    fa_muller_b = fuerza_accion(stat_muller, momentum=500, m_tipo=1.00, f_stam=1.00, c_crit=1.5)
    p_gol_b = probabilidad_victoria(fa_tsubasa_a, fa_muller_b)

    # Escenario C: Desgaste de estamina bajo presión + ruido adverso del 2%
    e_tsubasa_t1 = actualizar_estamina(e_actual=600, lambda_base=10, costo_skill=210, alpha=0.2, presion=1.0)
    f_stam_c = factor_estamina(e_tsubasa_t1, e_max=1100)
    fa_tsubasa_c = fuerza_accion(stat_tsubasa, momentum=510, m_tipo=1.15, f_stam=f_stam_c, c_crit=1.0, ruido_relativo=-0.02)
    fa_muller_c = fuerza_accion(stat_muller, momentum=500, m_tipo=1.00, f_stam=1.00, c_crit=1.0, ruido_relativo=+0.02)
    p_gol_c = probabilidad_victoria(fa_tsubasa_c, fa_muller_c)

    print(f"Escenario A (Estándar):      FA_Tsubasa={fa_tsubasa_a:,.0f} | FA_Müller={fa_muller_a:,.0f} | P(Gol)={p_gol_a*100:.3f}%")
    print(f"Escenario B (Crítico Oro):   FA_Tsubasa={fa_tsubasa_a:,.0f} | FA_Müller={fa_muller_b:,.0f} | P(Gol)={p_gol_b*100:.3f}%")
    print(f"Escenario C (Fatiga + RNG):  FA_Tsubasa={fa_tsubasa_c:,.1f} | FA_Müller={fa_muller_c:,.0f} | P(Gol)={p_gol_c*100:.3f}%")
