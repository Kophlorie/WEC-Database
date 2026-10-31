# AI-assisted changes (2026) — numbered source record

This file records **targeted AI-assisted recovery work**, not authorship of the historical project.

**Original authors:** Ophélie Choupin developed the core database architecture and class-generation code outside `db_interface/`. Francesco Ferri developed the original Dash application in `db_interface/`. The original algorithmic concepts, generated-class design and visual interface belong to that historical work, **not** to ChatGPT.

## A. Accepted interface integration — verified against Francesco's original ZIP

The latest accepted integration was prepared by comparing against the original version of db_interface from 2019. All **141 original lines of `db_interface/interface/app.py` remained in order**, including comments and original navigation. New code was added rather than replacing those lines.

1. **`db_interface/interface/app.py` — generated catalogue reader connection.** Imported the new helper and redirected the legacy navigation's data provider to the current `DynamicFunctions/` source hierarchy. The historical `database_scan` import remains in the file, but is superseded for catalogue routing. The original `company()` function is preserved for provenance, although generated company routes now use the new handler.
2. **`db_interface/interface/app.py` — company/WEC/child/object pages.** Added small helper functions for displaying generated metadata and clickable links; these extend organisation pages below the original company information, then expose associated WEC classes, child classes and generated object constructor attributes.
3. **`db_interface/interface/app.py` — navigation refresh and routing.** Added generated-source route handling inside the existing Dash callback while leaving the original **X**, **Objects Info**, **Back to Home**, **Previous Page** and menu definitions unchanged. Refreshing or navigating rereads current generated source rather than reusing a cached catalogue snapshot.
4. **`db_interface/interface/utils/dynamic_catalogue.py` — new file.** Added a static reader based on Python's `ast` for `DynamicFunctions/MainCreation.py` and the generated WEC `.py` files. It checks corresponding source modules, extracts organisational/class/object metadata without executing the generated classes, ignores `.pyc` files, and does not browse `Database/` to populate the web UI. Includes a compatibility path for Python 3.7, where `ast.unparse` is unavailable.

The accepted merge retains Francesco's original interface and comments. **Earlier proposed replacement UIs and `Database/`-driven catalogue browsers are not the accepted design.**

## B. Earlier recovery fixes — verify against the final submitted project

The following earlier recovery changes have been checked against the final publication candidate. They are limited corrections and extensions to the historical implementation, not replacements of the original architecture.

5. **`CoreFunctions/FixPeople.py`** — removed an extra positional `self` argument from `self.checkPeople(...)`, resolving a `TypeError` during import/initialisation.
6. **`CoreFunctions/CreationWECChild.py`** — adjusted parsing of legacy WEC child-object descriptions where the optional `Country_time` field is absent.
7. **`mainRun.py`** — removed an obsolete debugging attribute lookup and adjusted the placement of an unfinished integrated interface import.
8. **Root `run.py` (new)** — added a small launcher for the existing Dash app so it can run from the repository root without changing folders. The root launcher used in the reviewed version binds to `127.0.0.1` with `debug=False`.
9. **Other earlier candidate fixes** — earlier review copies also changed `db_interface/run.py`, `db_interface/interface/user_interface.py` and `db_interface/interface/utils/organization.py` to address `webbrowser` imports or a machine-specific path. **Do not attribute these as final changes unless the exact files in the final directory confirm them.** Francesco's original versions were retained in the latest interface merge where possible.

## C. Non-code and repository preparation

10. **Sample data:** Anonymised three `Database/Lists/People/Person*.txt` example records in an earlier review copy. Verify any real-name, contact or research descriptions against the final working directory.
11. **Git tracking:** Updated `.gitignore` in an earlier review so generated `DynamicFunctions/*.py` files are **included**, while `.pyc` files and `__pycache__` remain excluded. Generated `.py` modules are essential catalogue input, not cache.
12. **Documentation:** Consolidated `README.md`, `CONTRIBUTING.md`, clarifying architecture, installation, authorship, the intended-versus-implemented distinction and the currently unsupported dependency stack.
13. **Licence attribution:** Identified the recovered 2018 Plotly MIT text as a historical third-party notice rather than a project-wide copyright/licence. Recommended keeping that unchanged notice under `docs/ORIGINAL_PLOTLY_LICENSE.md`.

## D. Final Display and safety formatting restoration 

14. **generated_info()** Modified only the AI-added in `db_interface/interface/app.py` to present generated class and object attributes in a white information panel, reflecting the visual presentation of Francesco Ferri's original interface. No original interface code, comments, core generators or generated Python sources were modified.
15. Removed a machine-specific PowerShell profile; retained the corrected relative path in **organization.py**; disabled debugging and restricted historical Dash entry points to localhost; disabled an unused external jQuery dependency; replaced imports of a duplicated webbrowser implementation with Python's standard library and removed the redundant copy. No modifications were made to the original code-generation architecture, generated WEC hierarchy or domain algorithms.

## Preservation principle

The purpose of these additions is to **recover, make usable, document and accurately attribute** the historical project. They should not be described as an AI-authored replacement for either the generator or Francesco's interface. The final source folder and Git diff, rather than this document alone, determine precisely what has been changed in the published release.
