# Third-party Packages in Python
# ------------------------------

# You can use third-party packages that are not part of the standard library. These packages can be installed via `pip`.

# Example: Using the `requests` package to make HTTP requests
import requests

response = requests.get("https://www.example.com")
print(response.status_code)  # Output: 200 (if the request was successful)

# To install the `requests` package, run:
# pip install requests

# Best Practices
# --------------
# 1. Use `pip` to install third-party packages and manage dependencies.
# 2. Check the documentation of third-party packages for usage instructions.

# Exercises
# ---------
# 1. Install and use the `pandas` package to load a CSV file into a DataFrame.
# 2. Install the `matplotlib` package and create a simple line plot.