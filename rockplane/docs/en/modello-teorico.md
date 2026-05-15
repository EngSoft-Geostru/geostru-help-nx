# Theoretical model

RockPlane NX follows the **Hoek-Bray planar wedge** scheme (1981, RocPlane). The wedge is a 2D rigid body; the analysis is per metre of development along the crest. The Limit Equilibrium Method (LEM) is applied directly — no iteration, no slice subdivision, closed-form solution.

## Reference frame

\[ O = (0, 0) \text{ — toe of the slope (origin)} \]
\[ +X \text{ — toward the mountain (intact rock)} \]
\[ +Y \text{ — vertical, upward} \]
\[ \hat{t} = (-\cos\alpha, -\sin\alpha) \text{ — sliding direction (toward valley-down)} \]

- O = (0, 0) — toe of the slope
- B = (H·cot β, H) — crest of the slope face
- C = top of the failure plane (on the upper bench)
- D = top of the tension crack (if present)

## Geometry — Case A (no tension crack)

Equations (1)–(9) of the theoretical manual:

\[ N = \frac{H}{\sin\beta} \]
\[ B_x = H \cdot \cot\beta, \quad B_y = H \]
\[ L = H \cdot \frac{1 - \cot\beta \cdot \tan\psi}{\sin\alpha - \cos\alpha \cdot \tan\psi} \]
\[ M = \frac{L \cdot \cos\alpha - H \cdot \cot\beta}{\cos\psi} \]
\[ C_x = L \cdot \cos\alpha, \quad C_y = L \cdot \sin\alpha \]
\[ A = \frac{1}{2} \cdot |B_x \cdot C_y - B_y \cdot C_x| \]
\[ W = \gamma \cdot A \]

## Geometry — Case B (with tension crack)

The TC adds a vertex D between B and C. The failure plane goes O → D (instead of O → C), and the wedge is the quadrilateral OBCD.

## Limit equilibrium (eq. 26–30 of the manual)

Sum the actions in the global frame:

\[ F_x = E_x + S_x + J_x + V_x + U_{p,x} + R1_x \]
\[ F_y = W_y + E_y + S_y + J_y + V_y + U_{p,y} + R1_y \]

where:

- W: wedge weight (always negative Y)
- E: external load
- S: seismic
- J: active anchor pre-load
- V: water in the tension crack
- U<sub>p</sub>: ponded water at the toe
- R1: drape mesh normal pressure
- K: passive nail forces (enter separately into N and τ)

Project onto the failure plane:

\[ N = -(F_y + K_y) \cdot \cos\alpha + (F_x + K_x) \cdot \sin\alpha - U \quad \text{(eq. 28)} \]
\[ S = -F_y \cdot \sin\alpha - F_x \cdot \cos\alpha \quad \text{(eq. 29)} \]

Resisting τ:

\[ \tau = \frac{c \cdot L}{\gamma_c} + N \cdot \frac{\tan\varphi}{\gamma_\varphi} + K_x \cdot \cos\alpha + K_y \cdot \sin\alpha + \tau_{R2} \quad \text{(eq. 30)} \]

Factor of safety:

\[ FS = \frac{\tau}{|S|} \quad \text{verified: } FS \ge FS_{required} (\gamma_R) \]

## Barton-Bandis variant

When the Barton-Bandis criterion is active, the friction term is replaced with:

\[ \tau = \sigma_n \cdot \tan(\varphi_b + i_{eff}) \cdot N/\gamma_\varphi + K \cdot \cos\alpha + ... \]

with i<sub>eff</sub> = JRC · log₁₀(JCS / σ<sub>n</sub>) and σ<sub>n</sub> = N / L. The dependency on σ<sub>n</sub> makes the formula non-linear in N, so the software solves it directly using the computed N.

## Reinforcement

- **Active anchors (J)**: axial pre-load applied as an action. Reduces S and N.
- **Passive nails (K)**: mobilised force. Enters τ directly via cos α + sin α components, and also increases N (and hence friction).
- **R1 meshes**: normal pressure q on the slope face, enters R1<sub>x</sub>, R1<sub>y</sub>.
- **R2 meshes**: τ added directly to the resisting term.

## Overturning verification

The software also computes an **overturning safety factor F<sub>r</sub>** as ratio of stabilising to overturning moments about the toe O. This is a structural overall check (typical of the GeoStru SRS desktop), separate from sliding.

[See verification page →](verifica.md)
