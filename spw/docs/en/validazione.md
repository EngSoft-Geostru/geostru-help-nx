# Validation and limits

Validation documents the field of application, theoretical basis, test cases and known deviations. It helps the designer assess software reliability as required by Section 10.2 of NTC 2018.

It is not certification. It does not replace checking the model, data and results by the person signing the design.

The general reference is the [Calculation code validation](https://geostru.ai/en/validation/) page. The SPW NX technical validation document accompanies the engine identified in the report's “Calculation software” block.

## References used

Verification uses two families of reference:

- **public literature**, for methods, assumptions and solved cases;
- the **desktop program**, to check the port where the two models coincide.

The bibliography of methods is in [Methods](metodi.md#bibliografia-essenziale). A desktop comparison does not replace an independent reference.

## Comparison levels

| Level | In simple terms | What it demonstrates |
|---|---|---|
| L0 | The desktop reader is compared with known results from the same program | that the reference port is read and reproduced correctly |
| L1 | SPW NX and desktop work on a single-stage case with the same model | that calculation coincides where direct comparison is possible |
| L2 | A multi-stage project is compared with an independent reference | that the construction sequence is correct against an external source |
| L3 | SPW NX and desktop are compared on a multi-stage project with different models | which differences arise from the new model, without expecting agreement |

L1 comparison uses cases where geometry, combinations and history are compatible. L3 comparison measures and explains deviations. It neither automatically treats them as errors nor hides them.

Independent L2 references for multi-stage cases still need to be expanded. A result close to the desktop one is not enough to demonstrate the validity of the new model.

## Differences requiring attention

In multi-stage projects differences may arise from:

- supports installed on the already deformed wall;
- factors applied to actions or their effects according to the combination;
- seismic action limited to the intended combinations and stages;
- hydraulic checks without structural diagrams;
- desktop data that cannot be represented in the single-wall and single-stratigraphy model.

The import report and validation document help distinguish an intended difference from data requiring a check.

## Field of application

SPW NX covers RC pile, micropile and diaphragm walls, with supports and loads, analysed by stages. The FEM provides displacements, internal actions, pressures and support forces. Checks cover the areas listed in the Checks and reinforcement step.

LEM provides internal forces, embedment and support forces, without displacements. The code factor table is marked as requiring confirmation.

## Main limitations

- The response depends on the quality of ground parameters and the selected subgrade reaction modulus.
- Earth pressure assumptions must be consistent with geometry, soil-wall friction and displacements.
- The seepage regime uses the available model; the desktop flow net is not imported.
- Strut buckling is not checked.
- Global stability, vertical bearing capacity and section SLE checks are not available.
- An incomplete combination does not enter the envelopes.
- “Not calculated” is not a satisfied check.
- After an input change, previous results are out of date.

## Designer's responsibility

Before using results:

1. check the import report;
2. confirm the factor table and read every exception;
3. check calculation convergence and warnings;
4. check the governing condition and concomitant actions;
5. complete checks not covered with other tools;
6. keep the engine version and data fingerprint with the report.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/en/validazione.md).*
