---
title: FAQ
---

# Frequently asked questions

## Why is the "statistical distribution parameter" (Z_R) negative?

It is correct. Z_R is the **standard normal deviate** related to the reliability R in the AASHTO equation: it is negative for any R greater than 50% (with R = 90% it equals −1.282). The higher the reliability, the more negative Z_R is and the more conservative the design. See [Empirical method AASHTO](aashto.md#reliability-r-and-the-z_r-coefficient).

## Are the methods (AASHTO 1993, Ivanov, Westergaard) outdated?

They are **classical and well-established** methods, still the **reference standard** in professional practice and in the *Italian Catalogue of Road Pavements (CNR)*. They represent the most widely used regulatory basis for pavement sizing and verification. The most recent evolution is the *mechanistic-empirical* approach, more sophisticated but more demanding in terms of data and calibration.

## Why is there no "Calculate" button?

The calculation starts **automatically** when you open the **Results** tab — but only if you have **changed something** since the last calculation. If the data has not changed, RPD NX shows the already-computed result without re-running the calculation.

## The check is not satisfied: how do I pass it?

With FS < 1 the **How to pass the check** card appears, proposing, as alternatives, to **increase one layer** (each proposal is clickable and applies the thickness while recomputing) or to insert a **geogrid** with a given **TBR**. After applying, you can **undo** and try another solution.

## What is the geogrid TBR for?

The **Traffic Benefit Ratio** is the multiplier of the allowable axles due to the bituminous geogrid reinforcement. In the AASHTO method the allowable axles are multiplied by the TBR (default 1 = no effect). The actual value must be taken from the **manufacturer's data sheet**.

## The package is over-designed: can I reduce it?

Yes. When the check is satisfied with a wide margin, the **Package optimization** card appears: it proposes to **reduce** the thickness of one layer while keeping the check satisfied, to save material.

## In what units is the Structural Number?

The Structural Number is expressed in **inches** (with the cm equivalent shown next to it), as per the AASHTO method. Layer thicknesses, on the other hand, are entered in **cm**.

## In how many languages is RPD NX available?

In **7 languages**: Italian, English, French, Spanish, German, Romanian and Danish. You switch from the flag menu in the top-right corner.

## Where do I find the theoretical documents of the methods?

From the app's **?** menu → *Resources* tab → "Method documentation" section: you will find the PDFs "Empirical method" and "Rational method — Ivanov".

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RPD%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/en/faq.md).*
