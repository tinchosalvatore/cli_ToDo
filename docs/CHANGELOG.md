# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.1] - 2026-01-25

### Changed
- **UI:** More minimalistic UI, quitted directory contexto and changed colors for omni view with some new icons.
- **Traduction:** Tool output was originally in Spanish, no it is completely in English + argparse too

## [2.0.0] - 2026-01-25
### Added
- **Multitenancy (Context Awareness):** Tasks are now isolated by directory. Running `todo` in different folders shows different lists.
- **Omni View (`-o` / `--omni`):** New command to visualize all tasks across all directories/projects in a single global view.
- **Migration System:** Automatic migration of V1 legacy tasks (flat list) to the new V2 dictionary structure upon first run.
- **"Day Off" Celebration:** Added a visual celebration message when the pending list (`-u`) is empty.

### Changed
- **Persistence Architecture:** `tasks.json` structure changed from a simple `List` to a `Dictionary` where keys are absolute paths.
- **Reset Behavior (`-r`):** The reset command now performs a **Wipeout** (deletes all tasks in the current context) instead of just unchecking them.
- **UI:** Enhanced headers to show the current working directory (Context).

### Fixed
- Fixed issue where empty lists looked "broken" instead of "clean".

## [1.0.0] - 2025-12-01
### Added
- Initial release.
- Basic CRUD operations (Add, Toggle, Delete).
- Rich TUI integration.
- Flat file persistence.
