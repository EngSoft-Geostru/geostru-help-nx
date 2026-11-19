# AI assistant

The **Assistant** button opens the chat. The assistant is an artificial intelligence system working on the open project. If asked, it states that it is an artificial intelligence.

## What it can read

- the project and its individual sections;
- site data and seismic parameters;
- the import report;
- calculation status;
- validation errors and warnings;
- this manual, including the operational notes needed to guide you.

For questions about commands, steps, methods and messages it consults the manual before answering. It then relates the explanation to your project when needed.

## What it can change

When asked, it can update a section, add an anchor or load and append a stage with its events. It can open an example in place of the project only after an explicit request.

Before changing a section it reads the current content. It preserves identifiers and data you did not ask to change. After writing it reports any errors or warnings.

While the assistant is working, page edits are suspended. When finished, the page refreshes if the project changed.

## What it does not do

- it does not invent ground parameters, elevations or site data;
- it does not estimate results or declare checks satisfied without calculation;
- it does not delete data without an explicit request and confirmation;
- it does not directly generate Word or DXF;
- it does not replace the designer's judgement.

If data is missing, it tells you where to enter it. If an operation fails, it reports that nothing was changed.

## Questions about methods and formulas

The assistant explains the purpose, assumptions, inputs, results and limits of methods. It points to public literature and the [bibliography](metodi.md#bibliografia-essenziale).

It does not provide the engine equations or proprietary details. For theory use the bibliographic references. For your project numbers use the results calculated by the program.

## Example requests

- “What is missing before calculation?”
- “Explain the difference between an active and a passive anchor.”
- “Read the import report and tell me what to check.”
- “Add a stage with excavation to the elevation I give you.”
- “What does this governing condition mean?”

## Cost and limits

Each message costs **3 NX credits**. A message ending in error or without an answer is not charged. Changes completed before the error remain in the project.

A message can contain at most 20,000 characters, including an attachment. The number of operations in a single message is limited. If it reaches the limit, you can ask it to continue.

If the session has expired or another message is running, sending does not start. A monthly usage limit per application also applies.

## Support

The **Open a support ticket** quick action starts a support request. While the ticket is open, messages go to the operator instead of the assistant.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/en/assistente.md).*
