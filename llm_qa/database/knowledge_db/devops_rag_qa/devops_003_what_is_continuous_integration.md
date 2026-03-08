# Question
What is Continuous Integration?

# Category
devops / beginner

# Keywords
ci, continuous integration, build, test

# Answer

Continuous Integration (CI) means developers frequently merge code into a shared repository. Each change triggers automated build and tests to validate that changes can be safely merged. CI is not just about compiling—it establishes a fast feedback loop. A typical CI pipeline includes: fetch code, install dependencies, build, static checks, unit tests, integration tests, and results reporting. Problems surface in minutes rather than at release time.

# Key Points

- Frequent merges to shared repo
- Automated build and tests on every change
- Fast feedback loop
- Early detection of integration issues

# Example

Git push → Jenkins/GitHub Actions triggers build → tests run → results reported to PR.

# Related Concepts

Continuous Delivery, Testing, Automation
