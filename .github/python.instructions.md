---
applyTo: "**/*.py"
---

## AGENT.md (or GEMINI.md)

This file contains core policies and style guides for the Gemini coding agent. These instructions are mandatory for all code generation and refactoring tasks.

### 1. Code Style and Formatting (Context-Efficient)

**Goal:** Ensure all generated Python code is immediately compliant with standard industry practices, prioritizing readability and consistency.


* **Automated Formatting:** Use Black for automated code formatting. Run `black .` in the project root to format all Python files.
* **Linting:** Use Flake8 for linting to catch style violations and potential errors. Run `flake8 .` to check for issues.
* **PEP 8 Compliance:** All Python code **MUST** strictly adhere to PEP 8, unless explicitly overridden below.
* **Indentation:** Use **4 spaces** for indentation.
* **Line Length:** Max line length is **79 characters**. Wrap lines gracefully.
* **Naming Conventions:**
    * Functions and variables: `snake_case` (e.g., `calculate_score`).
    * Classes and Exceptions: `CamelCase` (e.g., `UserDataProcessor`).
    * Constants (Module-level): `CAPS_SNAKE_CASE` (e.g., `MAX_RETRIES`).
* **Imports:** Group imports in the following order, separated by a blank line:
    1.  Standard library imports.
    2.  Related third-party imports.
    3.  Local application/library specific imports.
* **Spacing:** Use two blank lines to separate top-level functions and class definitions.

### 2. General Programming Policy

**Goal:** Improve maintainability, robustness, and clarity of the generated code.

* **Type Hinting:** All function signatures **MUST** include type hints for parameters and return values (e.g., `def process(data: list[str]) -> dict:`).
* **Error Handling:** Use specific exception types (e.g., `ValueError`, `FileNotFoundError`). **NEVER** use a bare `except:`.
* **Docstrings:** Provide concise docstrings (following the **Google** or **NumPy** style) for all classes and all non-trivial public functions/methods.
* **Readability Over Performance:** Prefer the clearest, most Pythonic solution (e.g., list comprehensions, built-in functions) even if a micro-optimization is theoretically possible.

### 3. Agent Workflow and Context Management

**Goal:** Guide the agent in its interaction to maximize the use of the available context.

* **Prioritize Local Context:** When generating code, always prioritize the style, patterns, and architectural context from the files surrounding the requested change. **Your main goal is to match the existing codebase's style and conventions.**
* **Atomic Actions:** Execute only one primary action per prompt (e.g., generate the code, *then* refactor it, *then* add tests). Avoid trying to do everything in a single, complex step.
* **Concise Responses:** Provide code and minimal necessary explanation. **Do not include verbose conversational filler or redundant summaries.**