# Contributing, attribution and preservation

This repository documents and preserves a **historical research-software prototype**. The guiding principle is to keep the original implementation identifiable: correct defects and improve usability without presenting a modern rewrite as the original project.

## Original authorship

- **Ophélie Choupin:** the core Python generators, domain architecture, `Database/` organisation, `CoreFunctions/`, `mainRun.py` and the historical work outside the interface module.
- **Francesco Ferri:** the original `db_interface/` application, its Dash interface, navigation and supporting modules.

Authorship should remain explicit in the README, code history and any derived presentation of the software. Any future licence decision must consider both contributors' rights and any applicable institutional or third-party restrictions.

## AI-assisted recovery (2026)

ChatGPT (OpenAI) was used as a **coding and documentation assistant** for limited recovery work. It did **not** author the original WEC class-generation approach, its data architecture or Francesco's Dash application.

The accepted 2026 interface integration keeps Francesco's original `app.py` lines and comments, adding code to display the **local generated `.py` files in `DynamicFunctions/`** without replacing his menus. A separate `dynamic_catalogue.py` helper was added for static source inspection.

The **numbered record** in [docs/AI_ASSISTED_CHANGES_2026.md](docs/AI_ASSISTED_CHANGES_2026.md) distinguishes:

1. Confirmed additions to the final merged interface.
2. Earlier debugging and recovery changes to verify against the final working folder.
3. Documentation, anonymisation and Git/repository preparation.

Future substantial AI-assisted contributions should similarly identify the actual modified files and tasks, not suggest that AI authored the entire program.

## Guidelines for changes

- Preserve original source comments, menus and historical design unless a change is necessary and explicitly documented.
- Use `Database/` for input descriptions and `DynamicFunctions/` for **generated output**. The Dash catalogue must read only generated Python source, never invent its own hierarchy by scanning the descriptions or loading `.pyc` caches.
- Do not hand-edit generated WEC classes as a permanent fix; changes may be overwritten by `mainRun.py`.
- Make focused commits documenting *what changed and why*, especially for bug fixes versus new functionality.
- Test both entry points from the repository root on the documented Python environment; preserve the original GUI controls even when some remain placeholders.
- Do not commit private datasets, personal contact details, passwords, tokens, environment files, caches or machine-specific paths.
- Do not publish externally or relicense jointly authored code, historical research samples or third-party assets without the relevant permissions.

## Licence and permissions

No repository-wide open-source licence has yet been selected. The historic Plotly MIT text applies to Plotly material, **not automatically to this entire program**. See the README for the status of permissions.
