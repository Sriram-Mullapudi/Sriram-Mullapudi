<img src="assets/banner.svg" width="100%" alt="Sriram Mullapudi — Full-Stack Software Engineer" />

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0B0E14?style=for-the-badge&logo=linkedin&logoColor=5B8EF6&labelColor=0B0E14)](https://linkedin.com/in/srirammullapudi)
[![Email](https://img.shields.io/badge/Email-0B0E14?style=for-the-badge&logo=maildotru&logoColor=5B8EF6&labelColor=0B0E14)](mailto:srirammullapudi20@gmail.com)
[![LeetCode](https://img.shields.io/badge/LeetCode-0B0E14?style=for-the-badge&logo=leetcode&logoColor=5B8EF6&labelColor=0B0E14)](https://leetcode.com/)
[![AWS Certified](https://img.shields.io/badge/AWS_Certified-0B0E14?style=for-the-badge&logo=amazonwebservices&logoColor=5B8EF6&labelColor=0B0E14)](https://aws.amazon.com/certification/)

</div>

<br/>

I build **Java and Spring Boot services** and **React front ends** for systems where being wrong is expensive — payments, identity, and the data layers underneath them. Four years in, most of that work has been about the unglamorous parts: making event consumers idempotent, isolating downstream failures, and giving operations teams a screen that answers their question without a log search.

Currently finishing an **M.S. in Computer Science at USF** (GPA 3.96) and open to full-stack and backend engineering roles.

<img src="assets/metrics.svg" width="100%" alt="10M+ transactions per year · 500K+ Kafka events per day · 150+ daily dashboard users · 30% latency reduction" />

<br/>

## Selected Work

### Multi-Tenant Knowledge Search Platform

Hybrid document retrieval that stays grounded: **pgvector HNSW** vector search fused with **PostgreSQL full-text search** via Reciprocal Rank Fusion, streaming citation-backed answers over Server-Sent Events — with a keyword-search fallback for when the LLM service is down. Tenant isolation enforced end to end through JWT and refresh-token auth, RBAC, owner-scoped queries, execution tracing, and append-only audit records. Infrastructure provisioned as code.

<sub>`Java 17` · `Spring Boot` · `React` · `PostgreSQL/pgvector` · `Redis` · `ECS Fargate` · `Terraform` · `GitHub Actions (OIDC)`</sub>

### Offline-First Point-of-Sale System

An installable Windows POS that keeps selling when the network doesn't — offline sales, refunds, inventory, promotions, loyalty, and shift reconciliation. Pricing, promotion, and authorization rules live in the **Rust** core rather than the UI; transaction integrity is held by atomic SQLite operations, RBAC, Argon2 PIN hashing, append-only audit logs, and duplicate-payment controls.

<sub>`Rust` · `Tauri 2` · `SQLite` · `React` · `TypeScript`</sub>

<br/>

<details>
<summary><b>More projects</b></summary>
<br/>

| Project | What it solves | Stack |
|:--------|:---------------|:------|
| [**Event-Driven Integration Service**](https://github.com/Sriram-Mullapudi) | Async pipeline with idempotent processing, exponential-backoff retry, and DLQ routing | `Spring Boot` `AWS SQS` `PostgreSQL` `Docker` |
| [**Task Management Platform**](https://github.com/Sriram-Mullapudi) | Full-stack app — JWT auth, API versioning, pagination, OpenAPI docs, concurrent schema design | `React` `Spring Boot` `PostgreSQL` `Docker` |
| [**Cargo Booker Pro**](https://github.com/Sriram-Mullapudi/cargo-booker-pro) | Logistics booking workflows, shipment tracking, invoicing, admin panel | `Python` `Django` `SQLite` |
| [**Fairness-Income-Prediction**](https://github.com/Sriram-Mullapudi/Fairness-Income-Prediction) | Measuring disparate impact in income classification models | `Python` `Scikit-learn` `Pandas` |
| [**Leaf Disease Detection**](https://github.com/Sriram-Mullapudi/Leaf-Disease-Detection) | Transfer learning for classification on small labeled datasets | `Python` `PyTorch` |
| [**Schnorr Digital Signature**](https://github.com/Sriram-Mullapudi/Schnorr-Digital-Signature) | Full Schnorr scheme from scratch — keygen, signing, verification | `C` `Number Theory` |
| [**HORS Digital Signature**](https://github.com/Sriram-Mullapudi/HORS-Digital-Signature) | Hash-to-Obtain-Random-Subset stateless one-time signatures | `C` `Hash Functions` |
| [**Omnidroid DP Algorithm**](https://github.com/Sriram-Mullapudi/Omnidroid-DP-Algorithm) | Optimal scheduling under robot control constraints via dynamic programming | `Python` `Algorithms` |

</details>

<br/>

## Experience

**Software Engineer, Full Stack — Payments Platform** · JPMorgan Chase & Co. &nbsp;<sub>`Mar 2025 – May 2026 · Tampa, FL`</sub>

- Built Java 17 and Spring Boot services for payment validation, routing, and status tracking across a distributed platform handling **10M+ transactions annually**.
- Migrated synchronous validation flows to event-driven **Kafka workflows processing 500K+ events daily** — idempotent consumers, recovery paths, and downstream failure isolation cut end-to-end latency **30%**.
- Shipped React, TypeScript, and Redux Toolkit investigation dashboards used daily by **150+ operations analysts**, replacing manual application-log searches with live payment status and failure detail.
- Raised automated test coverage from **65% to 85%+** with JUnit 5, Mockito, and Cypress, and enforced SonarQube quality gates across Jenkins and GitHub Actions pipelines.
- Designed Oracle and PostgreSQL schemas and data-access layers for payment validation, routing, and status workflows.

<br/>

**Associate Software Engineer** · Accenture &nbsp;<sub>`Oct 2021 – Jul 2024 · Chennai, India`</sub>

- Implemented Okta-based OAuth 2.0/JWT authentication and Spring Security role-based access control for applications serving **25K+ users**.
- Automated user provisioning, role assignment, and access management through Microsoft Graph and Google Workspace APIs.
- Containerized and migrated backend services to AWS (EC2, S3, IAM, Docker, CloudWatch), contributing to a **15% reduction in production incidents**.
- Tuned MySQL and PostgreSQL queries for high-volume REST endpoints, cutting response times **20%**.
- Grew backend test coverage past **80%** and mentored three junior engineers through code reviews, design discussions, and structured debugging sessions. Recognized as an **Outstanding Performer**.

<br/>

## Toolkit

<table>
<tr>
  <td width="150"><b>Languages</b></td>
  <td>Java · TypeScript · JavaScript · SQL · Rust · Python · C</td>
</tr>
<tr>
  <td><b>Frontend</b></td>
  <td>React · Next.js · Redux Toolkit · Tailwind CSS · MUI</td>
</tr>
<tr>
  <td><b>Backend</b></td>
  <td>Spring Boot · Spring Security · Spring Data JPA · Hibernate · Node.js · Express · REST · GraphQL · Kafka · OAuth 2.0 · JWT</td>
</tr>
<tr>
  <td><b>Data</b></td>
  <td>PostgreSQL · Oracle · MySQL · Redis · SQLite · pgvector</td>
</tr>
<tr>
  <td><b>Cloud &amp; DevOps</b></td>
  <td>AWS (ECS Fargate, EC2, RDS, S3, IAM, CloudWatch) · Docker · Terraform · GitHub Actions · Jenkins</td>
</tr>
<tr>
  <td><b>Testing</b></td>
  <td>JUnit 5 · Mockito · Cypress · Jest · SonarQube</td>
</tr>
<tr>
  <td><b>Architecture</b></td>
  <td>Microservices · Event-driven systems · API design · Idempotent processing · Multi-tenant systems · RAG</td>
</tr>
</table>

<br/>

## Activity

<div align="center">

<img height="150" src="https://github-readme-stats.vercel.app/api?username=Sriram-Mullapudi&show_icons=true&hide_border=true&bg_color=0B0E14&title_color=5B8EF6&icon_color=00D4AA&text_color=8892A4&hide_title=true&rank_icon=github&include_all_commits=true&count_private=true&cache_seconds=1800" alt="GitHub stats" />
&nbsp;
<img height="150" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Sriram-Mullapudi&layout=compact&hide_border=true&bg_color=0B0E14&title_color=5B8EF6&text_color=8892A4&langs_count=6&cache_seconds=1800" alt="Top languages" />

</div>

<br/>

---

<div align="center">
<sub>

**Open to Full-Stack and Backend Software Engineer roles** &nbsp;·&nbsp; Tampa, FL &nbsp;·&nbsp; open to relocation

[Email](mailto:srirammullapudi20@gmail.com) &nbsp;·&nbsp; [LinkedIn](https://linkedin.com/in/srirammullapudi) &nbsp;·&nbsp; [GitHub](https://github.com/Sriram-Mullapudi)

</sub>
</div>
