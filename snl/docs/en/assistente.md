# AI assistant

The **Assistant** button opens the chat. The assistant is an artificial intelligence system that works on the open project; if you ask, it says so.

## What it reads

- the project, all of it or one step at a time, with the validation errors and warnings;
- the site and the proposed kh and kv;
- the import report;
- the analysis status and the **results**: summary of the checks, stages, single nails, sliding, layers, facing;
- this manual.

For questions on commands, steps, methods and messages it looks up the manual before answering, then relates the explanation to your project.

## What it does

- **runs the analysis** with the current data, like the **Calculate** button: the analysis is free;
- updates a step of the project at your request (geometry, layers, water table, loads, nails, factors, kh and kv);
- applies a **constant vertical spacing** or the **same data for all** to the nails, like the commands of the Nails step.

Before changing anything it reads the current data and keeps what you did not ask to change. After writing it reports validation errors and warnings. While it works, changes from the page are suspended; at the end the page reloads if the project or the analysis changed.

## What it does not do

- it does not invent soil parameters, levels, factors or site data;
- it does not estimate thrusts, forces or safety factors in its head: numbers come from the analysis;
- it does not declare a wall verified without an up-to-date result;
- it does not remove layers, nails, loads, the water table or the seismic action without your explicit request;
- it does not generate the Word report or the DXF drawing;
- it does not replace the designer's judgement.

## Example requests

- «What is missing to run the analysis?»
- «Run the analysis and tell me which stage governs internal stability.»
- «Why does nail 4 fail the pull-out check?»
- «Put eight nails starting at 0.8 m with 1.1 m spacing.»
- «Explain the proposed kh and kv.»
- «Read the import report and tell me what to check.»

Nails are referred to by the number of their row in the Nails step; stages follow the order of excavation depth.

## Cost and limits

Each message costs **3 NX credits**. A message that ended in error or without an answer is not charged; changes made before the error stay in the project.

A message can contain at most 20,000 characters, attachment included, and a limited number of operations: if the assistant reaches the limit, ask it to continue. There is also a monthly usage limit.

## Support

The quick action **Open a support ticket** starts a request to support. While the ticket is open, messages go to the operator.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/snl/docs/en/assistente.md).*
