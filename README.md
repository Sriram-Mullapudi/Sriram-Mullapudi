![Engineering across the full stack. I build systems that hold up.](assets/engineering-banner.svg)

# Sriram Mullapudi

**Full-Stack Software Engineer · Java / Spring Boot / React / Kafka / AWS**

I build payment services, operational interfaces, and data systems with a focus on reliability and performance. My 4+ years of experience span distributed payments at JPMorgan Chase and identity and access management at Accenture.

[**Explore my portfolio ↗**](https://sriram-mullapudi.github.io/portfolio/) · [LinkedIn](https://www.linkedin.com/in/srirammullapudi/) · [Email](mailto:srirammullapudi20@gmail.com)

Open to full-stack and backend opportunities in the U.S. · Open to relocation

## Engineering in practice

At JPMorgan Chase, my work included:

- **500K+ daily Kafka events** on a platform handling **10M+ annual transactions**.
- **30% lower end-to-end latency** after migrating synchronous validation flows to Kafka workflows.
- **150+ operations analysts** using React and TypeScript investigation dashboards daily.

## A trail of small commits

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/output/github-contribution-grid-snake-dark.svg" />
  <img src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/output/github-contribution-grid-snake.svg" alt="An animated snake travels across my GitHub contribution calendar, collecting contribution squares." width="100%" />
</picture>

<sub>My contribution calendar, with a little personality. Updated every 12 hours.</sub>

## Selected work

### 01 / Speedway POS

An offline-first Windows point-of-sale application for sales, refunds, inventory, promotions, loyalty, and shift reconciliation.

- **Built for transaction integrity:** atomic SQLite operations, duplicate-payment controls, and append-only audit logs.
- **Backend-enforced rules:** pricing, promotions, loyalty, RBAC, and Argon2 PIN hashing in Rust.
- **Validated separately:** 5K+ real-world sales; 10K+ integrity-test attempts across 20+ failure/concurrency scenarios, with zero duplicate charges in those tests.

`Rust` `Tauri 2` `SQLite` `React` `TypeScript`

[**Browse the code ↗**](https://github.com/Sriram-Mullapudi/speedway-pos) · [Read the case study](https://sriram-mullapudi.github.io/portfolio/#speedway-pos)

### 02 / Multi-Tenant Knowledge Search

A hybrid retrieval system combining pgvector HNSW and PostgreSQL full-text search with Reciprocal Rank Fusion.

- **Retrieval at scale:** 30K documents; ~1 s p95 retrieval latency.
- **Measured answer quality:** 92% Recall@10 and an 83% acceptable-answer rate on ~200 labelled queries.
- **Tenant-aware delivery:** isolation at API and data-access layers, citation-backed answers over SSE, and keyword fallback when the LLM service is unavailable.

`Java 17` `Spring Boot` `React` `PostgreSQL` `pgvector` `Redis` `AWS` `Terraform`

[**Read the architecture and evaluation ↗**](https://sriram-mullapudi.github.io/portfolio/#knowledge-search)

### More to explore

- [**Cargo Booker Pro**](https://github.com/Sriram-Mullapudi/Cargo-Booker-Pro) — Django logistics application for shipment booking, tracking, and invoices.
- [**Xv6 systems work**](https://github.com/Sriram-Mullapudi/OS_Project-2-Syscalls-and-Schedulers) — custom system calls, scheduling, and command-line utilities.
- [**Portfolio source**](https://github.com/Sriram-Mullapudi/portfolio) — engineering case studies, interactive architecture walkthroughs, and photography.

## Tools I work with

| Layer | Core tools |
| :--- | :--- |
| Backend | Java 17, Spring Boot, Spring Security, Rust, REST APIs |
| Frontend | React, TypeScript, Redux Toolkit |
| Data & messaging | Kafka, PostgreSQL, pgvector, Redis, SQLite |
| Cloud & delivery | AWS, Docker, Terraform, GitHub Actions, Jenkins |
| Quality & security | JUnit 5, Mockito, Cypress, OAuth 2.0, RBAC |

<details>
<summary><strong>Full skills matrix</strong></summary>

| Area | Skills |
| :--- | :--- |
| Languages | Java, TypeScript, JavaScript, SQL, Rust, Python, C |
| Frontend | React, Next.js, Redux Toolkit, Tailwind CSS, MUI, HTML, CSS |
| Backend | Spring Boot, Spring Security, Spring Data JPA, Hibernate, Node.js, Express.js, REST APIs, GraphQL, Kafka, OAuth 2.0, JWT |
| Data | PostgreSQL, Oracle, MySQL, Redis, SQLite, pgvector |
| Cloud & DevOps | AWS ECS Fargate, EC2, RDS, S3, IAM, CloudWatch, Docker, Terraform, GitHub Actions, Jenkins, CI/CD |
| Testing & tools | JUnit 5, Mockito, Cypress, Jest, SonarQube, Git, Linux |
| Architecture | Microservices, event-driven systems, API design, idempotent processing, multi-tenant systems, RAG |

</details>

## Experience

**JPMorgan Chase & Co. — Software Engineer, Full Stack**<br>
Payments Platform · Tampa, Florida · March 2025 – May 2026

Java and Spring Boot payment services, Kafka workflows, React operational dashboards, and automated quality gates.

**Accenture — Associate Software Engineer**<br>
Chennai, India · October 2021 – July 2024

Identity and access management for applications serving 25K+ users, AWS migration, and REST endpoint performance improvements.

<details>
<summary><strong>More about my contributions</strong></summary>

### JPMorgan Chase & Co.

- Developed Java 17 and Spring Boot services for payment validation, routing, and status tracking across a distributed platform handling 10M+ transactions annually.
- Migrated synchronous validation flows to Kafka workflows processing 500K+ events daily, reducing end-to-end latency by 30%.
- Built React, TypeScript, and Redux Toolkit investigation dashboards used daily by 150+ operations analysts.
- Increased automated test coverage from 65% to 85%+ and enforced SonarQube quality gates in Jenkins and GitHub Actions pipelines.
- Designed Oracle and PostgreSQL schemas and data-access layers for payment workflows.

### Accenture

- Implemented Okta-based OAuth 2.0/JWT authentication and Spring Security RBAC for applications serving 25K+ users.
- Automated user provisioning, role assignment, and access management through Microsoft Graph and Google Workspace APIs.
- Containerized and migrated backend services to AWS, contributing to a 15% reduction in production incidents.
- Tuned MySQL and PostgreSQL queries, reducing high-volume REST endpoint response times by 20%.
- Increased backend test coverage to 80%+ and mentored three junior engineers.

</details>

## Education & recognition

**M.S. in Computer Science · University of South Florida** — GPA: 3.96 / 4.00

AWS Certified Cloud Practitioner · Outstanding Performer at Accenture

<details>
<summary><strong>GitHub activity</strong></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="profile-summary-card-output/github_dark/0-profile-details.svg" />
  <img src="profile-summary-card-output/github/0-profile-details.svg" alt="GitHub contribution activity summary" width="100%" />
</picture>

</details>

---

<p align="center">
  <img src="assets/developer-illustration.png" alt="A playful developer character exploring a glowing holographic globe at a computer." width="260" />
</p>

<p align="center"><strong>Always exploring. Always building.</strong></p>

**Good systems. Good people.**<br>
Interested in working together? [Get in touch](mailto:srirammullapudi20@gmail.com) or [explore my portfolio](https://sriram-mullapudi.github.io/portfolio/).
