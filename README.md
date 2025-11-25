# Team Calculator Project

## Goal
You will work as a team of 4 developers to build a simple shared calculator module in Python.

Each of you is responsible for ONE function:
- `add(a, b)`
- `sub(a, b)`
- `mul(a, b)`
- `div(a, b)`

All functions MUST live in the same shared file: `calculator/operations.py`.

The project will be developed in **PyCharm** and version-controlled with **GitHub** using **Git Flow** conventions.

---

## Git Flow rules for this workshop

### Branches
- `main`
  - Always stable / releasable.
  - Protected: you are NOT allowed to push directly.

- `develop`
  - Integration branch for features.
  - Protected: you are NOT allowed to push directly.
  - Only merged into using Pull Requests.

- `feature/<something>`
  - Your personal working branch.
  - Example: `feature/add`, `feature/sub`, `feature/mul`, `feature/div`.

### Workflow
1. Clone the repo locally in PyCharm.
2. Create a new branch from `develop`:
   - Developer A → `feature/add`
   - Developer B → `feature/sub`
   - Developer C → `feature/mul`
   - Developer D → `feature/div`
3. Implement ONLY your own function in `calculator/operations.py`.
4. Write tests for your function in `tests/test_*.py`.
5. Run `pytest` locally. All your tests must PASS before you continue.
6. Create a Pull Request from your feature branch → `develop`.
7. Ask at least ONE teammate to review your Pull Request.
8. After approval, merge into `develop`.

Later, when all four functions work and all tests are green,
`develop` can be merged into `main`.

---

## Very important rules
- Do NOT create new Python files for your function.
  All 4 functions go in the SAME file `calculator/operations.py`.
- Expect merge conflicts in `operations.py`. Solving those conflicts together is part of the assignment.
- You are NOT allowed to merge your own Pull Request without review.

---

## Running the calculator
You can run the interactive calculator from PyCharm:

```bash
python main.py
```

This script will:
- ask which operation you want (`add`, `sub`, `mul`, `div`)
- ask for two numbers
- show the full calculation and the result

---

## Running tests
Install dependencies (once):
```bash
pip install -r requirements.txt
```

Then run:
```bash
pytest
```

All tests should pass before making a Pull Request.
