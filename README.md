# Wave Energy Converter (WEC) Database

**A Python research prototype for description-driven generation of WEC classes, with a local Dash catalogue.**

Originally developed in **2019** during research at **Aalborg University**; recovered and prepared for local use and technical demonstration in **2026**.

This project explores an approach to managing information about wave energy converters (WECs), their designs, configurations and experiments. Its distinctive mechanism is not simply storing data: the Python generators **create and update actual Python source-code modules** from a hierarchical set of descriptions. The separate web interface presents the **generated Python state**.

> **Status: historical research prototype.** The code generator and local catalogue can be demonstrated, but a number of originally planned experiment-processing and auxiliary modules are unfinished. This is not a production database service, a complete inventory of real-world WECs or a publicly hosted application.

## What the project does

1. **Describe:** Organise information in `Database/` folders with text descriptions of organisations, WEC families, design variants and individual test configurations.
2. **Generate:** Run `mainRun.py` to interpret those descriptions and generate Python classes, inheritance relationships and object definitions in `DynamicFunctions/`.
3. **Inspect:** Launch the local Dash catalogue to browse the generated organisations, WEC parent classes, child classes and object information.
4. **Regenerate:** When descriptions change, rerun the generator. The interface then reflects the updated generated files on the next navigation/refresh.

**The distinction between the two sources is essential:**

- `Database/` is the **input** to the original code generator.
- `DynamicFunctions/*.py` is the **sole catalogue data source** for the current web interface.
- The web catalogue does **not** scan `Database/`, import `.pyc` caches, or use saved catalogue data from a previous run. It reads the local generated `.py` source, including `MainCreation.py`, using a static Python parser.
- `MainCreation.py` is itself generated output, representing the **last generated state**, not necessarily unsaved changes in `Database/`.

## Project layout

```text
Database/                                   Hierarchical input descriptions and examples
CoreFunctions/                              Original fixed classes and source generators
DynamicFunctions/                           Generated Python source modules (tracked in Git)
  MainCreation.py                           Generated hierarchy and object construction
  FoldersPath.py                            Generated path information
  ...                                       Generated WEC parent/child class modules
mainRun.py                                  Generator entry point
run.py                                      Root-level launcher for the original Dash interface
db_interface/                               Historical Dash interface by Francesco Ferri
  interface/app.py                          Original navigation with 2026 additions
  interface/utils/dynamic_catalogue.py     2026 static reader for generated Python source
requirements.txt                            Historical pinned dependencies
docs/CONTRIBUTING.md                             Authorship and contribution guidance
docs/AI_ASSISTED_CHANGES_2026.md             Numbered, version-aware change record
```

The source archive used during recovery contained 28 generated Python files (26 WEC class modules plus `MainCreation.py` and `FoldersPath.py`). This is **a snapshot count**, not a fixed limit or a count of WEC instances. The catalogue is intended to follow the local generated files rather than a hard-coded number.

## Installation on Windows

The historical interface uses dependencies from around 2019. A **Python 3.7 conda environment** was used to recover it. Python 3.7 and this Dash/Flask dependency stack are now unsupported, so **run locally only**.

Install [Miniforge](https://github.com/conda-forge/miniforge) if conda is not already available. Then open a terminal in the **project root** (the directory containing both `mainRun.py` and `run.py`).

### First-time setup (only once per environment)

```powershell
conda create -n wec2026 python=3.7 pip -y
conda run -n wec2026 python -m pip install -r requirements.txt
conda run -n wec2026 python --version
conda run -n wec2026 python -m pip check
```

Do **not** recreate the environment or reinstall dependencies every time you launch the application. If an environment named `wec2026` already exists and contains the packages, skip setup. The commands use `conda run` because PowerShell's `conda activate` may not be initialised. Avoid upgrading pip indiscriminately: some original package metadata is incompatible with newer packaging tools.

### Run the code generator

```powershell
conda run -n wec2026 python mainRun.py
```

This reads `Database/` and may **rewrite** generated source files in `DynamicFunctions/`. Use a working checkout, and review changes before committing them.

### Run the local web catalogue

```powershell
conda run --no-capture-output -n wec2026 python run.py
```

Open [http://127.0.0.1:8050](http://127.0.0.1:8050) if your browser does not open automatically. Stop the server with `Ctrl+C` in the terminal.

**No need to `cd db_interface`.** The root-level `run.py` starts Francesco's original Dash application. Its original interface directory and internal entry point remain part of the historical project.

### Browse the interface

The original menu—including the **X**, **Objects Info**, **Back to Home** and **Previous Page** elements—has been preserved. The principal generated-source browsing route is:

**Path and Info → Classes Info → Company Info → organisation → WEC parent class → WEC child class → generated object information.**

Selecting an organisation displays its generated metadata **and clickable WEC links below it**. Selecting a WEC displays its class details and child-class links. The generated objects attached to a child class appear on its page. The historical top-level **Objects Info** control is retained, but it is not presented as a separately completed global objects browser.

## How the software was designed

The original documentation (*ProgramDescription*, *ClassDiagram_UML*, *FolderOrganisation* and its diagram slides) describes three related concepts:

- **Fixed/domain classes:** persistent concepts such as organisations, identifiers, people, projects, dates and testing environments.
- **Creation/generator classes:** notably `CreationWEC`, `CreationWECChild` and `CreationMainCreation`, which read descriptions and generate class source code.
- **Generated WEC classes:** parent and inherited child classes plus the object definitions assembled by the main generator.

The proposed experiment hierarchy also distinguishes numerical tests, dry tests, wave-tank tests and sea trials, with raw measurements, calibration, reports and post-processing kept in distinct folders. These are **design objectives**; some auxiliary classes, calibration procedures and WEC experiment post-processing features were planned but not implemented fully.

Generated Python files should **not be edited manually** for lasting changes, because the generator may overwrite them. Amend the descriptions or the appropriate generator instead.

## Authorship and recovery history

**Original work (2019):**

- **Ophélie Choupin:** the Python data model and code-generation system outside `db_interface/`, including `CoreFunctions/`, the folder/database architecture and `mainRun.py`.
- **Francesco Ferri:** the original `db_interface/` Dash application, its interface design and supporting code.

**Recovery and documentation (2026):** Ophélie Choupin recovered the project and prepared it for reproducible local execution. **ChatGPT (OpenAI) assisted with targeted debugging, integration and documentation; it did not create the historical algorithms, generator architecture or Francesco's original interface.**

For transparency, the 2026 AI-assisted work is numbered in [docs/AI_ASSISTED_CHANGES_2026.md](docs/AI_ASSISTED_CHANGES_2026.md). In particular, the final 2026 interface integration **retains all 141 original lines of Francesco's `app.py` in their original order except for run_server()**, adds a generated-source browser, and introduces `dynamic_catalogue.py` as a separate helper. Earlier experimental replacements are not the accepted interface design.

See [CONTRIBUTING](docs/CONTRIBUTING.md) for the authorship/contribution policy for outstanding checks before public release.

## Licence, redistribution and privacy

**No project-wide open-source licence has been selected.** The historical LICENSE shared as `docs/ORIGINAL_PLOTLY_LICENSE.md` containing *Copyright (c) 2018 plotly* is a third-party MIT notice; it is **not** a licence granted by Ophélie Choupin or Francesco Ferri for this entire project.

The original interface's redistribution permission and any rights or restrictions affecting historical WEC descriptions must be confirmed before making the repository public. The absence of a project-wide licence does not itself establish permission to publish someone else's code or research data. Installed dependencies carry their own respective licences.

This software is intended for **local demonstration**. It is not supported for public web hosting. Before a public GitHub release, inspect all source, samples, documentation and Git history for credentials, personal information, machine-specific paths and non-public research information.

## Known limitations

- Several historical classes and experimental-data workflows remain incomplete.
- The source generator and the Dash interface are separate entry points; Dash displays the **generated** state, not unprocessed changes under `Database/`.
- The source reader inspects generated Python syntax without executing generated modules; it is a catalogue view, not a full runtime verification of every object.
- `mainRun.py` can overwrite **tracked** `DynamicFunctions/*.py` files. Inspect `git diff` after regenerating.
- The original interface includes historical controls that remain placeholders. Preserving their appearance does not imply those features are implemented.
- Historical Python/Dash dependencies should be used in an isolated, local environment, not an internet-facing service.
