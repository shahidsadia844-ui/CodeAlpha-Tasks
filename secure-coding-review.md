# Task 3: Secure Coding Review

This repository contains a manual secure code review demonstrating SQL Injection vulnerability and its remediation in Python.

## Vulnerability Identified
* **SQL Injection:** The insecure login function directly concatenates user input into the SQL query string. This allows an attacker to bypass authentication using inputs like `admin' OR '1'='1`.

## Remediation Applied
* **Parameterized Queries:** The secure function uses placeholders (`?`) to safely bind user input, preventing malicious SQL code execution.
* 
