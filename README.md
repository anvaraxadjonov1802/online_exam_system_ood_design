# 📝 Online Exam System OOD Design

Student: Anvar Axadjonov

Group: 23-311 Software Engineering
##

This project was taken over by the following.

* OOD design .doc file
* UML diagram
* Python programming language code

[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A Python-based **Online Exam System** designed with **Domain-Driven Design (DDD) principles** and Clean Architecture.  
Structured to separate **domain logic**, **application use-cases**, and **infrastructure concerns**.

---

## 📁 Project Structure

```text
code/
│
├── domain/                  # Core business logic
│   ├── enums/               # Fixed values / states
│   ├── entities/            # Business entities with behavior
│   └── value_objects/       # Immutable objects without identity
│
├── application/             # Use-case orchestration
├── infrastructure/          # Repositories / external services
├── main.py                  # Entry point
└── README.md
```

### 🔹 Folder Diagram (Visual)

```
code/
│
├── domain/
│   ├── enums/
│   │   ├── attempt_status.py
│   │   └── violation_type.py
│   ├── entities/
│   │   ├── student.py
│   │   ├── exam.py
│   │   ├── question.py
│   │   ├── exam_attempt.py   # Aggregate Root
│   │   ├── answer.py
│   │   ├── violation.py
│   │   └── result.py
│   └── value_objects/
│       └── answer.py
│
├── application/
│   └── exam_service.py
├── infrastructure/
│   └── repository.py
├── main.py
└── README.md
```

---

## ⚙️ Quick Start

### 1. Clone repository

```bash
git clone https://github.com/anvaraxadjonov1802/online_exam_system_ood_design.git
cd online_exam_system_ood_design/code
```

### 2. Run application

```bash
python main.py
```

*(Optionally, create a virtual environment and install dependencies)*

---

## 📌 Domain Overview

### 🔹 Enums (`domain/enums/`)

- `AttemptStatus` — State of exam attempt (e.g., IN_PROGRESS, FINISHED)  
- `ViolationType` — Types of exam violations (e.g., CHEATING, LATE_SUBMISSION)

### 🔹 Entities (`domain/entities/`)

- `Student`, `Exam`, `Question`, `ExamAttempt`, `Violation`, `Result`  
- **Aggregate Root:** `ExamAttempt`  

Key methods in `ExamAttempt`:

```python
submit_answer()
record_violation()
finish()
auto_submit()
```

### 🔹 Value Objects (`domain/value_objects/`)

- `Answer` — Immutable object representing student answer

> Note: `Answer` can also be an entity if it needs identity.

---

## 💡 Application Layer (`application/exam_service.py`)

```python
class ExamService:
    def start_exam(self, student, exam):
        return ExamAttempt("id", student, exam)
```

> Handles **use-case orchestration**. All domain logic stays in entities.

---

## ✅ Why This Structure?

> “This project follows **Clean Architecture / DDD principles**:  
> - Domain logic is independent of external layers  
> - Testable, maintainable, scalable  
> - Easy to extend with new features or external systems”

---


