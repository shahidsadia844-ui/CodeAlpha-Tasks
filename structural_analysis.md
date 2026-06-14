# TASK 2: Structural Load Analysis Report

## 1. Introduction
This report presents the structural load analysis for a simply supported **Concrete Beam** in a single-story basic structure. The objective is to calculate the total design load acting on the beam by considering Dead Loads, Live Loads, and basic Wind Loads.

---

## 2. Structure Specifications
We are analyzing a rectangular reinforced concrete beam with the following dimensions:
* **Length ($L$):** $5\text{ meters}$
* **Width ($b$):** $0.3\text{ meters}$
* **Depth ($h$):** $0.6\text{ meters}$
* **Density of Concrete ($\rho$):** $25\text{ kN/m}^3$

---

## 3. Load Calculations (Calculation Sheet)

### A. Dead Load ($DL$)
Dead load includes the self-weight of the concrete beam per meter length.
$$\text{Self-Weight} = b \times h \times \rho$$
$$\text{Self-Weight} = 0.3 \times 0.6 \times 25 = 4.5\text{ kN/m}$$

*Assuming an additional finishes load of $1.5\text{ kN/m}$:*
* **Total Dead Load ($DL$):** $4.5 + 1.5 = 6.0\text{ kN/m}$

### B. Live Load ($LL$)
Based on standard residential/office occupancy codes, we assume a uniform live load:
* **Total Live Load ($LL$):** $3.0\text{ kN/m}$

### C. Wind Load ($WL$) - Basic Level
For a basic low-rise structure, the horizontal wind pressure converted to an equivalent vertical load effect on this beam member is assumed as:
* **Wind Load ($WL$):** $1.2\text{ kN/m}$

---

## 4. Structural Behavior & Load Combinations
To safety-check the structure, we combine the loads using standard ultimate strength design factors:

| Load Combination Formula | Calculation | Ultimate Factored Load ($U$) |
| :--- | :--- | :--- |
| **Comb 1:** $1.4 \times DL$ | $1.4 \times 6.0$ | **$8.4\text{ kN/m}$** |
| **Comb 2:** $1.2 \times DL + 1.6 \times LL$ | $(1.2 \times 6.0) + (1.6 \times 3.0)$ | **$12.0\text{ kN/m}$** |
| **Comb 3:** $1.2 \times DL + 1.0 \times LL + 1.0 \times WL$ | $(1.2 \times 6.0) + 1.0 \times 3.0 + 1.0 \times 1.2$ | **$11.4\text{ kN/m}$** |

### Conclusion on Behavior
The critical design load is **$12.0\text{ kN/m}$** (from Combination 2). The beam must be engineered to withstand this maximum bending and shearing action safely without excessive deflection.
