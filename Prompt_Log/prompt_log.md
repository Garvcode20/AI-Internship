# Task 3: Prompt Engineering Challenge

This document showcases 5 poor prompts, their effective conversions, and the resulting output improvements when passed to an AI tool.

---

### Challenge 1: Clean Code
**Poor Prompt:**
> Write a python script to download a webpage.

**Improved Prompt:**
> Write a clean, modular Python script using the `requests` library to download the HTML content of a given URL. Include error handling for HTTP errors and connection timeouts, and format the code according to PEP 8 standards with appropriate docstrings.

**Output Improvements:**
- The poor prompt yielded a 3-line script that would crash if the internet was disconnected.
- The improved prompt yielded a reusable function wrapped in a `try-except` block (`requests.exceptions.RequestException`), proper type hinting (`url: str -> str`), and docstrings explaining the parameters.

---

### Challenge 2: Optimized Code
**Poor Prompt:**
> Write code to find duplicate numbers in a list.

**Improved Prompt:**
> Write a time-optimized Python function to find all duplicate numbers in a large list of integers. Compare the brute-force approach (O(n^2)) with an optimized hash set approach (O(n)), and provide only the optimized code with comments explaining the space-time trade-off.

**Output Improvements:**
- The poor prompt resulted in a nested `for` loop (O(n^2)) or a naive `list.count()` approach which is very slow for large datasets.
- The improved prompt yielded an O(n) solution using a `set()`, alongside a detailed comment explaining that we traded O(n) space to achieve O(n) time complexity.

---

### Challenge 3: Beginner-Friendly Explanations
**Poor Prompt:**
> Explain OOP.

**Improved Prompt:**
> Explain Object-Oriented Programming (OOP) to a beginner who has only written basic procedural Python scripts. Use a real-world analogy (like a Car factory) to explain the four main pillars: Encapsulation, Abstraction, Inheritance, and Polymorphism. Avoid overly academic jargon.

**Output Improvements:**
- The poor prompt generated a dry, textbook definition of OOP that was difficult to understand without prior context.
- The improved prompt generated an engaging tutorial mapping classes to "Blueprints" and objects to "Physical Cars", making abstract concepts like Polymorphism (e.g., `Car.drive()` vs `Boat.drive()`) immediately understandable.

---

### Challenge 4: Production-Level Documentation
**Poor Prompt:**
> Add comments to this code. `def calc(a,b): return a/b`

**Improved Prompt:**
> Generate production-level documentation for the following Python function. Include a standard docstring format (e.g., Google or Sphinx style) detailing arguments, return types, and potential exceptions (like `ZeroDivisionError`). 
> Code: `def calc(a,b): return a/b`

**Output Improvements:**
- The poor prompt added a single redundant inline comment: `# divides a by b`.
- The improved prompt generated a full Google-style docstring detailing `Args:`, `Returns:`, and `Raises:` sections, ensuring the function is ready for auto-documentation tools like Sphinx.

---

### Challenge 5: Comprehensive Testing
**Poor Prompt:**
> Write test cases for a login function.

**Improved Prompt:**
> Write a suite of unit tests using Python's `unittest` framework for a `login(username, password)` function. Include positive test cases (successful login) and negative edge cases (empty strings, SQL injection attempts, incorrect passwords). Use mock objects for the database connection.

**Output Improvements:**
- The poor prompt provided a few `print()` statements manually checking if `login("admin", "123")` returned true.
- The improved prompt provided a robust, automated test class inheriting from `unittest.TestCase`, covering security edge cases and demonstrating how to mock external dependencies.
