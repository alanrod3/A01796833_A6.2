# Hotel Reservation System - Activity 6.2

This repository contains the implementation of a basic hotel reservation system developed in Python. The project focuses on the application of software engineering best practices, following the **PEP-8** standard and implementing robust unit tests with a minimum coverage of 85%.

## Project Structure
The project is organized as follows:
* **source/**: Contains the business logic (classes: `Hotel`, `Customer`, and `Reservation`).
* **tests/**: Unit test cases developed using the `unittest` module.
* **data/**: JSON files for data persistence (Hotels, Customers, and Reservations).
* **results/**: Evidence of test execution and coverage reports.

## Implemented Requirements
The following persistent behaviors were implemented according to the activity guidelines:

### 1. Hotel Management
* Create, delete, and display hotel information.
* Modify existing information.
* Reserve and cancel rooms.

### 2. Customer Management
* Create and delete customer profiles.
* Display and modify customer information.

### 3. Reservations
* Create reservations linking a Customer and a Hotel.
* Cancel existing reservations.

## Code Quality and Standards
To ensure software quality, the following tools were used:
* **PEP-8**: All code follows the official Python style guides to ensure readability.
* **Flake8**: Used for static analysis and fixing style errors/warnings.
* **Pylint**: Employed to verify that the program does not generate logic errors or design issues.

## Testing and Coverage
Unit tests were designed to cover both "happy paths" (valid data) and error handling (invalid data or corrupt files).

* **Test Results**: 10 tests were executed successfully (OK).
* **Coverage**: The system meets the requirement of exceeding 85% line coverage.
* **Error Handling**: The program includes mechanisms to handle invalid data in JSON files, displaying the error in the console and allowing execution to continue without interruption.
