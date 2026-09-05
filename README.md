# DASW oTree Apps

> A modular collection of experimental applications built with **oTree** for behavioral, economic, decision-making, and Real Effort Task (RET) experiments.

[![oTree](https://img.shields.io/badge/oTree-Experimental%20Framework-blue)](https://www.otree.org/)
[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📖 About

**DASW oTree Apps** is a collection of modular experimental applications developed using [oTree](https://www.otree.org/).

The project is intended to provide a reusable foundation for developing and conducting:

- Behavioral experiments
- Economic experiments
- Decision-making experiments
- Real Effort Tasks (RET)
- Investment experiments
- Consumption and shopping experiments
- Probability-based experiments
- Other customized experimental tasks

Each application is developed as an independent oTree app so that it can be tested, modified, reused, or combined with other applications.

The project is designed for researchers, experiment developers, research assistants, students, and other users who need a flexible experimental environment.

---

# 🎯 Project Goals

The main goals of DASW oTree Apps are:

1. **Modularity**  
   Build experiments as independent and reusable applications.

2. **Reusability**  
   Allow existing applications to be reused in future experiments.

3. **Consistency**  
   Maintain a common structure and development approach across experiments.

4. **Flexibility**  
   Allow experimental rules, interfaces, scoring, and payoff systems to be customized.

5. **Data Collection**  
   Store participant decisions and task performance using oTree's data system.

6. **Experiment Integration**  
   Allow several applications to be combined into a single experimental session.

---

# 🧩 Applications

The repository contains several experimental applications.

## 📊 Application Overview

| Application | Category | Description |
|---|---|---|
| `algebraic` | RET | Algebra and mathematical problem-solving |
| `count_word` | RET | Counting occurrences of a target character |
| `decoding` | RET | Decoding symbols or characters |
| `donation_with_rank` | Behavioral | Donation decision with ranking |
| `investment` | Economic | Investment and risk-return decisions |
| `shop_apps` | Behavioral / Economic | Shopping and consumption decisions |
| `slot_machine` | RET / Probability | Probability-based slot machine task |
| `transcription_continuous` | RET | Continuous transcription task |
| `transcription_exact` | RET | Exact transcription task |

Applications can be used independently or combined into a larger experiment.

---

# 🧠 Real Effort Tasks

Real Effort Tasks are designed to require participants to perform a measurable activity involving effort, concentration, accuracy, speed, or problem-solving.

The project currently contains several RET applications.

---

## 🔐 1. Decoding

**Application:** `decoding`

The Decoding task requires participants to decode a character, symbol, or value using a predefined rule.

### Example

```text
Rule:

A → 1
B → 2
C → 3

Question:

B

Answer:

2
```

### Main Purpose

The task can be used to measure:

- Accuracy
- Speed
- Cognitive effort
- Problem-solving performance

### Typical Workflow

```text
Display Rule
     ↓
Display Question
     ↓
Participant Decodes
     ↓
Submit Answer
     ↓
Calculate Result
```

---

# ✍️ 2. Exact Transcription

**Application:** `transcription_exact`

Exact Transcription requires participants to reproduce displayed text exactly.

The task can be used to measure typing and transcription performance.

### Participant Workflow

```text
Display Text
     ↓
Participant Types Text
     ↓
Submit
     ↓
Compare With Original
     ↓
Calculate Score
```

### Possible Measurements

- Correct transcription
- Incorrect transcription
- Accuracy
- Completion time
- Score
- Reward

The application can be configured for different text sets and task durations.

---

# ⏱️ 3. Continuous Transcription

**Application:** `transcription_continuous`

Continuous Transcription is designed as a time-based transcription task.

Participants continuously transcribe displayed text during a predefined period.

### General Workflow

```text
Start Task
     ↓
Display Text
     ↓
Participant Transcribes
     ↓
Submit Answer
     ↓
Check Answer
     ↓
Record Performance
     ↓
Continue Until Time Expires
```

### Performance Data

The application can record information such as:

- Total attempts
- Correct answers
- Errors
- Accuracy
- Reward
- Start time
- End time
- Performance during the task

This makes the application suitable for experiments where effort is measured through repeated task performance.

---

# 🔢 4. Count Word

**Application:** `count_word`

Count Word is a visual counting task.

Participants are shown a table containing characters and are asked to determine how many times a specific target character appears.

### Example

```text
Target: U

A  U  B  C  U
D  E  F  U  G
U  H  I  J  K

Answer: 4
```

### Workflow

```text
Generate Table
     ↓
Select Target Character
     ↓
Display Table
     ↓
Participant Counts Target
     ↓
Submit Answer
     ↓
Validate Answer
     ↓
Calculate Score
```

### Possible Measurements

- Correct answer
- Incorrect answer
- Response time
- Score
- Accuracy

---

# ➗ 5. Algebraic

**Application:** `algebraic`

The Algebraic task presents participants with mathematical or algebraic problems.

The task can be configured with different problem sets and difficulty levels.

### Possible Experimental Variables

- Problem difficulty
- Number of questions
- Time limit
- Reward per correct answer
- Maximum score
- Randomized questions

### Workflow

```text
Generate Problem
     ↓
Display Problem
     ↓
Participant Solves
     ↓
Submit Answer
     ↓
Validate Answer
     ↓
Calculate Score
```

---

# 🎰 6. Slot Machine

**Application:** `slot_machine`

Slot Machine is a probability-based experimental task presented through a slot-machine-style interface.

The application combines participant interaction with randomized outcomes.

### Main Components

- Random outcomes
- Probability logic
- Participant interaction
- JavaScript interface
- Result calculation
- Payoff logic

### General Workflow

```text
Start Game
     ↓
Participant Interacts
     ↓
Random Outcome
     ↓
Determine Result
     ↓
Calculate Payoff
```

The task can be adapted for experiments involving probability, luck, risk, and decision-making.

---

# 💰 Economic & Behavioral Experiments

In addition to RET applications, the repository contains applications designed for behavioral and economic experiments.

---

# 📈 7. Investment

**Application:** `investment`

The Investment application is designed for experiments involving investment and financial decision-making.

Participants can be provided with an endowment and make decisions about how much to allocate to an investment opportunity.

### Possible Components

- Initial endowment
- Investment amount
- Risk level
- Probability
- Investment return
- Consumption
- Profit
- Final payoff

### General Workflow

```text
Receive Endowment
       ↓
Investment Decision
       ↓
Investment Outcome
       ↓
Calculate Return
       ↓
Calculate Consumption
       ↓
Calculate Final Payoff
```

The investment mechanism can be customized according to the requirements of the experiment.

---

# 🛒 8. Shop Apps

**Application:** `shop_apps`

Shop Apps provides a simulated shopping environment where participants can select products and quantities.

Participants interact with a shopping cart before proceeding to checkout.

### Main Components

- Product catalog
- Product prices
- Quantity controls
- Shopping cart
- Total price
- Checkout
- Purchase summary

### General Workflow

```text
View Products
     ↓
Select Products
     ↓
Adjust Quantity
     ↓
Shopping Cart
     ↓
Review Purchase
     ↓
Checkout
```

The application can be used to study:

- Consumer behavior
- Purchasing decisions
- Consumption choices
- Budget allocation
- Price sensitivity

---

# ❤️ 9. Donation with Rank

**Application:** `donation_with_rank`

Donation with Rank combines a donation decision with participant ranking information.

The application can be used to investigate behavioral responses to relative performance or social comparison.

### Possible Research Topics

- Charitable giving
- Social preferences
- Relative position
- Competition
- Ranking effects
- Behavioral decision-making

### General Workflow

```text
Receive Endowment
       ↓
Donation Decision
       ↓
Calculate Donation
       ↓
Determine Rank
       ↓
Calculate Payoff
```

---

# 🏗️ Project Architecture

The project follows a modular oTree architecture.

```text
DASW oTree Apps
│
├── RET Applications
│   ├── decoding
│   ├── algebraic
│   ├── count_word
│   ├── transcription_exact
│   ├── transcription_continuous
│   └── slot_machine
│
├── Economic Applications
│   └── investment
│
├── Behavioral Applications
│   ├── donation_with_rank
│   └── shop_apps
│
├── _static/
├── _templates/
├── settings.py
├── requirements.txt
├── Procfile
├── LICENSE
└── README.md
```

---

# ⚙️ Configuration

The main experiment configuration is managed through:

```text
settings.py
```

Applications are added to oTree through `SESSION_CONFIGS`.

For example:

```python
SESSION_CONFIGS = [
    dict(
        name='count_word',
        display_name='RET Count Word',
        app_sequence=['count_word'],
        num_demo_participants=1,
    ),
]
```

The `app_sequence` determines the order in which applications are presented to participants.

---

# 🔄 Combining Multiple Applications

One of the main advantages of this project is that multiple applications can be combined into a single experiment.

For example:

```python
dict(
    name='combined_experiment',
    display_name='Combined Experiment',
    app_sequence=[
        'investment',
        'shop_apps',
        'transcription_continuous',
    ],
    num_demo_participants=1,
),
```

The resulting experiment becomes:

```text
Investment
    ↓
Shopping
    ↓
Continuous Transcription
    ↓
Results
```

This makes the project suitable for multi-stage experimental designs.

---

# 💵 Payoff & Scoring

Each application can implement its own scoring and payoff mechanism.

Depending on the experiment, the system may calculate:

- Task score
- Correct answers
- Accuracy
- Investment return
- Consumption
- Purchase cost
- Donation
- Experimental earnings
- Final participant payoff

A typical workflow is:

```text
Participant Action
       ↓
Task Result
       ↓
Score Calculation
       ↓
Payoff Calculation
       ↓
Final Earnings
```

When multiple applications are used in one experiment, results from previous applications can be incorporated into later stages or the final payment calculation.

---

# 📊 Data Collection

oTree automatically stores participant and experiment data through its models.

Depending on the application, data may include:

### Participant Information

- Participant ID
- Session information
- Group information
- Round information

### Task Performance

- Answers
- Attempts
- Correct answers
- Errors
- Accuracy
- Completion time
- Scores

### Economic Decisions

- Endowment
- Investment
- Consumption
- Purchase quantities
- Donation
- Payoff

The exact fields depend on the implementation of each application.

---

# 📁 Project Structure

A typical application follows the standard oTree structure:

```text
app_name/
│
├── __init__.py
├── models.py
├── pages.py
├── tests.py
│
├── templates/
│   └── app_name/
│       └── Page.html
│
└── static/
    └── app_name/
        ├── css/
        └── js/
```

Some applications may contain additional files depending on their requirements.

---

# 🛠️ Requirements

The project is built with:

- Python
- oTree
- HTML
- CSS
- JavaScript

The required Python packages are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/projectdasw/dasw_otree_apps.git
```

Move into the project directory:

```bash
cd dasw_otree_apps
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Start the oTree development server:

```bash
otree devserver
```

Then open:

```text
http://localhost:8000
```

or:

```text
http://127.0.0.1:8000
```

---

# 🧪 Testing

Before deploying an experiment, each application should be tested thoroughly.

Recommended tests include:

- Page navigation
- Form validation
- Randomization
- Timer behavior
- JavaScript functionality
- Score calculation
- Payoff calculation
- Multiple rounds
- Multiple participants
- Database recording
- Edge cases

oTree tests can be run using:

```bash
otree test
```

---

# 🗄️ Database

For local development, oTree can be used with a local database configuration.

For production deployments, PostgreSQL is recommended.

During development, the database can be reset using:

```bash
otree resetdb
```

> ⚠️ **Warning:** Resetting the database removes existing experiment data.

---

# 🌐 Production Deployment

Before deploying an experiment to production, review the following:

- Database configuration
- Environment variables
- Admin password
- Secret key
- HTTPS configuration
- Production server configuration
- Database backups
- Debug configuration
- Access control

Sensitive information should not be committed to the Git repository.

Use environment variables for credentials and other deployment-specific configuration.

---

# 🔐 Security

The repository should not contain:

- Database passwords
- Admin passwords
- API keys
- Secret keys
- Private credentials
- Participant personal information

Use environment variables or deployment secrets for sensitive configuration.

---

# 🧑‍💻 Development Workflow

The recommended development workflow is:

```text
1. Define Experiment
       ↓
2. Design Task Logic
       ↓
3. Create oTree App
       ↓
4. Implement Models
       ↓
5. Implement Pages
       ↓
6. Create Templates
       ↓
7. Add JavaScript / CSS
       ↓
8. Implement Scoring
       ↓
9. Implement Payoff
       ↓
10. Test Application
       ↓
11. Add to settings.py
       ↓
12. Run Experiment
```

---

# ➕ Creating a New Application

Create a new oTree application using:

```bash
otree startapp your_app_name
```

Example:

```bash
otree startapp memory_task
```

Then add the application to `settings.py`:

```python
dict(
    name='memory_task',
    display_name='Memory Task',
    app_sequence=['memory_task'],
    num_demo_participants=1,
),
```

---

# 📌 Development Principles

When adding a new application, follow these principles.

### Modular

Keep the application independent whenever possible.

### Reusable

Avoid hard-coding experimental parameters that may need to change.

### Configurable

Place frequently modified parameters in constants or configuration sections.

### Maintainable

Use clear naming conventions and organize templates, JavaScript, and CSS properly.

### Testable

Every important experimental rule should be tested before deployment.

---

# 📚 Recommended Documentation for Each App

Each application should ideally document the following:

```text
Application Name
│
├── Purpose
├── Experimental Design
├── Participant Instructions
├── Game Flow
├── Variables
├── Scoring
├── Payoff
├── Data Collected
├── Configuration
└── Known Limitations
```

This makes applications easier to reuse in future experiments.

---

# 🔬 Example Experimental Design

Multiple applications can be combined to create a complete experiment.

For example:

```text
                 EXPERIMENT
                     │
                     ▼
              ┌─────────────┐
              │ Investment  │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │  Shop Apps  │
              └──────┬──────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Continuous          │
          │ Transcription       │
          └──────────┬──────────┘
                     │
                     ▼
              ┌─────────────┐
              │ Final Result│
              └──────┬──────┘
                     │
                     ▼
                Participant
                  Payoff
```

This modular structure allows researchers to create complex experiments without having to develop every component from scratch.

---

# 📈 Future Development

The project is intended to continue growing with additional experimental applications and improvements.

Potential future developments include:

- Additional Real Effort Tasks
- More economic decision-making tasks
- Improved participant interfaces
- Additional scoring mechanisms
- More configurable experiment parameters
- Improved data summaries
- Additional payoff mechanisms
- More comprehensive automated testing
- Improved documentation
- Additional reusable UI components

---

# 🤝 Contributing

Contributions and improvements are welcome.

When developing a new application:

1. Create a dedicated oTree app.
2. Keep the application modular.
3. Document the experimental logic.
4. Add appropriate validation.
5. Test the complete participant flow.
6. Document scoring and payoff rules.
7. Update the project documentation when necessary.

---

# 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

# 🔗 Repository

**GitHub Repository**

https://github.com/projectdasw/dasw_otree_apps

---

# 📦 Project Status

**Status:** Active Development

DASW oTree Apps is continuously being developed as a reusable collection of oTree applications for experimental research.

Applications may have different development stages, and experimental implementations should be tested and validated before being used in a live study.

---

# 👤 Author

**DASW Project**

GitHub:

https://github.com/projectdasw

---

## ⭐ Acknowledgement

This project is built using **oTree**, an open-source framework for interactive multiplayer experiments.

Learn more about oTree:

https://www.otree.org/