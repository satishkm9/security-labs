# Security Lab Portfolio

**Satish Kumar Mahto · SOC investigations · Detection practice · VAPT**

This repository is my journal for independent security training across TryHackMe, other learning platforms, and my own lab environments. It is designed to show my reasoning, evidence, testing, and reporting as I complete work.

**Current status:** portfolio starter. Templates and folder structure are ready; no completed lab investigations have been added to this repository yet. A template or draft is not evidence of a completed investigation.

[Lab index](labs/INDEX.md) · [Learning-note template](templates/learning-note.md) · [SOC report template](templates/soc-report.md) · [VAPT report template](templates/vapt-report.md)

## What a completed entry contains

1. A specific objective and a clearly identified training environment.
2. My contribution, including tools used and any assistance or reference material.
3. Evidence that supports the conclusion, with relevant interpretation.
4. A result, limitations, and an explanation of what I would do next.
5. Reproduction steps only where the source permits them, or for my own original lab work.

## Structure

```text
security-labs/
├── README.md
├── labs/
│   └── INDEX.md
├── templates/
│   ├── learning-note.md
│   ├── soc-report.md
│   └── vapt-report.md
├── scripts/
│   └── new_lab.py
└── .gitignore
```

New entries are grouped by track and platform, for example:

```text
labs/soc/tryhackme/<date>-<topic>/README.md
labs/soc/homelab/<date>-<topic>/README.md
labs/vapt/homelab/<date>-<topic>/README.md
```

Use **one folder for each lab**, rather than creating a new repository for every room. Add evidence images or original code inside that folder when appropriate.

## Add a lab

Python 3.10 or newer is sufficient; no third-party packages are required. From this repository's root, run:

```bash
python3 scripts/new_lab.py --track soc --platform tryhackme --slug alert-triage --title "Alert triage learning notes"
```

This creates a **draft learning note**, an evidence folder, and an entry in the lab index. It does not claim that the lab is complete.

For an original SOC experiment using your own sample logs:

```bash
python3 scripts/new_lab.py --track soc --platform homelab --slug failed-login-analysis --title "Failed login analysis" --type soc
```

For a VAPT report on your own authorised test application:

```bash
python3 scripts/new_lab.py --track vapt --platform homelab --slug access-control-review --title "Access control review" --type vapt
```

Use `--help` for all options. If you do not use Python, copy the appropriate template into a new lab folder and add its link to [the index](labs/INDEX.md) manually.

## Publish useful evidence

- **TryHackMe active labs:** publish original, high-level reflections only, without answers, flags, solutions, platform screenshots revealing solutions, or walkthroughs. Recreate a concept using your own synthetic data for a detailed public case study.
- **Retired content:** verify the platform's current publication guidance before posting a detailed report.
- **Other platforms:** check their publication rules individually; a subscription alone does not establish permission to redistribute lab content.
- **Own lab:** identify the environment as a simulation and distinguish expected output from observed output.
- **Assistance:** identify copied or adapted code, external references, and material AI assistance. Explain what you personally changed, tested, or concluded.

TryHackMe's [Acceptable Use Policy](https://tryhackme.com/legal/acceptable-use-policy), section 8, explains its active-content and examination restrictions.

## Completion criteria

Before changing a draft's status to **Completed**, fill in its conclusions, link the evidence that may be shared, verify your results, remove unused template prompts, and check the platform's publication rules. Update the status in both the report and the lab index.

A report can conclude **inconclusive**. Record missing evidence and the next investigation step rather than presenting an unsupported result.
