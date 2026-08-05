Today 10:15 AM
Sriram_Mullapudi_FSE.pdf
PDF
You are an expert GitHub profile designer, branding strategist, and senior software engineer.

I am going to upload my resume and (optionally) my current GitHub profile README.

Your task is to completely redesign ONLY my GitHub profile homepage (README.md).

Do NOT focus on my repositories. I only care about making my profile homepage look world-class and premium.

## Goals
- Make it look like a top 1% GitHub profile.
- Keep it professional but visually impressive.
- Make recruiters immediately understand who I am.
- Optimize for software engineering jobs.
- Showcase my experience without exaggerating anything.
- Every statement must come from my resume.
- If something isn't in my resume, ask before adding it.

## Design Requirements

Create a beautiful GitHub README using:

- Modern layout
- Clean spacing
- Professional typography
- Consistent color theme
- High-quality badges
- Icons
- SVG animations
- Typing animation
- Animated headers
- Wave divider
- Animated contribution snake
- GitHub Readme Stats
- Top Languages
- Streak Stats
- Visitor Counter
- Trophy section
- Technology stack with icons
- Contact section
- Social links
- Call-to-action

Use GitHub-compatible Markdown and HTML only.

## Include sections like

1. Hero Banner
2. Animated Greeting
3. Short Professional Introduction
4. About Me
5. Current Focus
6. Tech Stack
7. Skills
8. Experience Highlights
9. Projects (only if on resume)
10. GitHub Statistics
11. Languages
12. Achievements
13. Certifications
14. Education
15. Connect With Me
16. Fun Facts (only if supported by my resume)
17. Footer

## Animations

Use animations such as:

- Capsule Render banner
- Readme Typing SVG
- Animated wave footer
- GitHub contribution snake animation
- Floating icons where possible
- GIFs only if they remain professional
- Dynamic badges
- Shields.io badges
- Readme Stats
- Streak Stats
- Activity Graph
- Visitor Counter

Use the most modern GitHub README techniques that still work today.

## Code Quality

Generate:

- One complete README.md
- Proper Markdown
- Proper HTML
- Comments explaining where I need to replace usernames, links, and IDs
- Keep everything organized
- No broken links
- Mobile-friendly layout

## Branding

The overall style should feel like:

- Apple
- Stripe
- Linear
- Vercel
- GitHub Premium

Minimal, elegant, and highly polished.

## Extra

After generating the README:

1. Explain every animation used.
2. Explain how to enable the GitHub contribution snake.
3. Explain how to enable GitHub Actions if required.
4. Suggest optional improvements.
5. Suggest a matching GitHub banner.
6. Recommend a color palette.
7. Recommend fonts.
8. Recommend profile badges.
9. Recommend profile widgets.

Finally, rate the profile from 1–10 and continue improving it until it reaches a 10/10 premium GitHub profile.


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

<sub>Java 17 · Spring Boot · React · PostgreSQL/pgvector · Redis · ECS Fargate · Terraform · GitHub Actions (OIDC)</sub>

### Offline-First Point-of-Sale System

An installable Windows POS that keeps selling when the network doesn't — offline sales, refunds, inventory, promotions, loyalty, and shift reconciliation. Pricing, promotion, and authorization rules live in the **Rust** core rather than the UI; transaction integrity is held by atomic SQLite operations, RBAC, Argon2 PIN hashing, append-only audit logs, and duplicate-payment controls.

<sub>Rust · Tauri 2 · SQLite · React · TypeScript</sub>

<br/>

<details>
<summary><b>More projects</b></summary>
<br/>

| Project | What it solves | Stack |
|:--------|:---------------|:------|
| [**Event-Driven Integration Service**](https://github.com/Sriram-Mullapudi) | Async pipeline with idempotent processing, exponential-backoff retry, and DLQ routing | Spring Boot AWS SQS PostgreSQL Docker |
| [**Task Management Platform**](https://github.com/Sriram-Mullapudi) | Full-stack app — JWT auth, API versioning, pagination, OpenAPI docs, concurrent schema design | React Spring Boot PostgreSQL Docker |
| [**Cargo Booker Pro**](https://github.com/Sriram-Mullapudi/cargo-booker-pro) | Logistics booking workflows, shipment tracking, invoicing, admin panel | Python Django SQLite |
| [**Fairness-Income-Prediction**](https://github.com/Sriram-Mullapudi/Fairness-Income-Prediction) | Measuring disparate impact in income classification models | Python Scikit-learn Pandas |
| [**Leaf Disease Detection**](https://github.com/Sriram-Mullapudi/Leaf-Disease-Detection) | Transfer learning for classification on small labeled datasets | Python PyTorch |
| [**Schnorr Digital Signature**](https://github.com/Sriram-Mullapudi/Schnorr-Digital-Signature) | Full Schnorr scheme from scratch — keygen, signing, verification | C Number Theory |
| [**HORS Digital Signature**](https://github.com/Sriram-Mullapudi/HORS-Digital-Signature) | Hash-to-Obtain-Random-Subset stateless one-time signatures | C Hash Functions |
| [**Omnidroid DP Algorithm**](https://github.com/Sriram-Mullapudi/Omnidroid-DP-Algorithm) | Optimal scheduling under robot control constraints via dynamic programming | Python Algorithms |

</details>

<br/>

## Experience

**Software Engineer, Full Stack — Payments Platform** · JPMorgan Chase & Co. &nbsp;<sub>Mar 2025 – May 2026 · Tampa, FL</sub>

- Built Java 17 and Spring Boot services for payment validation, routing, and status tracking across a distributed platform handling **10M+ transactions annually**.
- Migrated synchronous validation flows to event-driven **Kafka workflows processing 500K+ events daily** — idempotent consumers, recovery paths, and downstream failure isolation cut end-to-end latency **30%**.
- Shipped React, TypeScript, and Redux Toolkit investigation dashboards used daily by **150+ operations analysts**, replacing manual application-log searches with live payment status and failure detail.
- Raised automated test coverage from **65% to 85%+** with JUnit 5, Mockito, and Cypress, and enforced SonarQube quality gates across Jenkins and GitHub Actions pipelines.
- Designed Oracle and PostgreSQL schemas and data-access layers for payment validation, routing, and status workflows.

<br/>

**Associate Software Engineer** · Accenture &nbsp;<sub>Oct 2021 – Jul 2024 · Chennai, India</sub>

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
How to fix?

Great — this confirms the workflow generated the cards successfully.

Now copy only the raw GitHub URLs into your main README.md. Do not copy the headings like ## github_dark, the setup instructions, or the triple-backtick code fences.

Replace your current analytics section with this:

## GitHub analytics

<div align="center">

<a href="https://github.com/vn7n24fzkq/github-profile-summary-cards">
  <img
    width="96%"
    src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/0-profile-details.svg"
    alt="GitHub profile contribution summary"
  />
</a>

<br/><br/>

<a href="https://github.com/vn7n24fzkq/github-profile-summary-cards">
  <img
    width="48%"
    src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/1-repos-per-language.svg"
    alt="Repositories by language"
  />
</a>
<a href="https://github.com/vn7n24fzkq/github-profile-summary-cards">
  <img
    width="48%"
    src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/2-most-commit-language.svg"
    alt="Most-used commit languages"
  />
</a>

<br/><br/>

<a href="https://github.com/vn7n24fzkq/github-profile-summary-cards">
  <img
    width="48%"
    src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/3-stats.svg"
    alt="GitHub repository statistics"
  />
</a>
<a href="https://github.com/vn7n24fzkq/github-profile-summary-cards">
  <img
    width="48%"
    src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/4-productive-time.svg"
    alt="Contribution activity by time of day"
  />
</a>

<br/><br/>

<img
  width="96%"
  src="https://github-readme-activity-graph.vercel.app/graph?username=Sriram-Mullapudi&bg_color=0B0E14&color=CBD5E1&line=2563EB&point=2DD4BF&area=true&area_color=1E3A8A&hide_border=true&custom_title=Contribution%20Activity"
  alt="GitHub contribution activity graph"
/>

</div>

Then:

Open the root README.md
Click the pencil icon
Delete the old broken analytics block
Paste the block above
Remove all visible setup text such as “Before these local cards can display...”
Commit with:
Fix profile analytics display

Then hard-refresh your public profile with:

Ctrl + Shift + R

The cards should now display correctly.

Skip to content
Sriram-Mullapudi
User navigation
Overview
Repositories
15
 (15)
Projects
Packages
Stars
4
 (4)

Sriram-Mullapudi
Sriram-Mullapudi/README.md
Sriram Mullapudi — Full-Stack Software Engineer

 Email LinkedIn GitHub



Profile views
Engineering reliable systems at scale
I am a full-stack software engineer with 4+ years of experience building Java and Spring Boot services and React applications for high-volume payment and identity systems.

My work includes Kafka workflows processing 500K+ events per day on a platform handling 10M+ annual transactions, a 30% reduction in end-to-end latency, and React/TypeScript dashboards[...]

10M+
annual transactions	500K+
daily Kafka events	30%
latency reduction	150+
daily dashboard users
About me
role: Full-Stack Software Engineer
experience: 4+ years
core_stack:
  - Java 17
  - Spring Boot
  - React
  - TypeScript
  - Kafka
  - AWS
engineering_focus:
  - Distributed payment systems
  - Event-driven workflows
  - Identity and access management
  - Full-stack operational tooling
education: M.S. in Computer Science, University of South Florida
gpa: 3.96 / 4.00
mobility: Open to relocation
Current focus
Designing Java 17 and Spring Boot services for validation, routing, status tracking, and multi-tenant systems.
Building React, TypeScript, and Redux Toolkit interfaces that turn operational data into usable workflows.
Developing event-driven systems with idempotent processing, recovery paths, and downstream failure isolation.
Applying AWS, Docker, Terraform, GitHub Actions, and Jenkins to deployment and delivery workflows.
Technology stack
Languages
Java, TypeScript, JavaScript, Rust, Python, and C
Frontend
React, Next.js, Redux, Tailwind CSS, Material UI, HTML, and CSS
Backend & data
Spring, Node.js, Express, PostgreSQL, MySQL, Redis, SQLite, and Kafka
Cloud, delivery & tooling
AWS, Docker, Terraform, GitHub Actions, Jenkins, Git, and Linux
Complete skills matrix
Experience highlights
JPMorgan Chase & Co. — Software Engineer, Full Stack
Payments Platform · Tampa, Florida · March 2025 – May 2026

Developed Java 17 and Spring Boot services for payment validation, routing, and status tracking across a distributed platform handling 10M+ transactions annually.
Migrated synchronous validation flows to Kafka workflows processing 500K+ events daily, reducing end-to-end latency by 30%.
Built React, TypeScript, and Redux Toolkit investigation dashboards used daily by 150+ operations analysts.
Increased automated test coverage from 65% to 85%+ and enforced SonarQube quality gates in Jenkins and GitHub Actions pipelines.
Designed Oracle and PostgreSQL schemas and data-access layers for payment workflows.
Accenture — Associate Software Engineer
Chennai, India · October 2021 – July 2024

Implemented Okta-based OAuth 2.0/JWT authentication and Spring Security RBAC for applications serving 25K+ users.
Automated user provisioning, role assignment, and access management through Microsoft Graph and Google Workspace APIs.
Helped migrate backend services to AWS, contributing to a 15% reduction in production incidents.
Tuned MySQL and PostgreSQL queries, reducing high-volume REST endpoint response times by 20%.
Increased backend test coverage to 80%+ and mentored three junior engineers.
Selected projects
Multi-Tenant Knowledge Search Platform
A hybrid retrieval system combining pgvector HNSW search, PostgreSQL full-text search, and Reciprocal Rank Fusion.

Highlights

Citation-backed answers streamed over Server-Sent Events
Keyword-search fallback when the LLM service is unavailable
JWT and refresh-token authentication with RBAC
Owner-scoped queries, execution tracing, and append-only audit records
ECS Fargate, RDS, ElastiCache, ALB, Secrets Manager, Terraform, and GitHub Actions with OIDC
Java 17 Spring Boot React PostgreSQL pgvector Redis AWS Docker Terraform

Offline-First Point-of-Sale System
An installable Windows point-of-sale application supporting offline sales, refunds, inventory, promotions, loyalty, and shift reconciliation.

Highlights

Business and authorization rules centralized in the Rust backend
Atomic SQLite operations for transaction integrity
RBAC and Argon2 PIN hashing
Append-only audit logs
Duplicate-payment controls
Rust Tauri 2 SQLite React TypeScript

GitHub analytics
GitHub profile contribution summary


Repositories by language Most-used commit languages


GitHub repository statistics Contribution activity by time of day


GitHub contribution activity graph

profile-summary-card-output/ └── github_dark/ ├── 0-profile-details.svg ├── 1-repos-per-language.svg ├── 2-most-commit-language.svg ├── 3-stats.svg └── 4-productive-time.svg

Check the Code tab of your profile repository. If profile-summary-card-output is not present, the new analytics workflow has not generated or committed the files yet.

Also delete every remaining URL containing either of these domains from README.md:

github-readme-stats.vercel.app streak-stats.demolab.com

Achievements & certification
GitHub profile trophies
AWS Certified Cloud Practitioner — Amazon Web Services; credential verifiable on Credly.
Outstanding Performer at Accenture — recognized for team-level initiatives and deliverables.
LeetCode — 1,436 problems solved across data structures and algorithms; global rank 8,791.
Education
University of South Florida
Master of Science in Computer Science · GPA: 3.96 / 4.00

Contribution journey
The animated contribution snake will appear here after the included workflow is enabled.
Let’s connect
I build full-stack software with Java, Spring Boot, React, Kafka, and AWS—with an emphasis on reliability, performance, and usable operational workflows.


Start a conversation by email Connect on LinkedIn



Open to relocation



PinnedLoading
 Cargo-Booker-Pro Public
Full-stack Django logistics app — book shipments, track in real time, generate invoices

 HTML  1

122 contributions in the last year
Contribution Graph
Day of Week	AugustAug	SeptemberSep	OctoberOct	NovemberNov	DecemberDec	JanuaryJan	FebruaryFeb	MarchMar	AprilApr	MayMay	JuneJun	JulyJul
SundaySun																																																					
MondayMon																																																					
TuesdayTue																																																					
WednesdayWed																																																					
ThursdayThu																																																					
FridayFri																																																					
SaturdaySat																																																					
Learn how we count contributions
Less
No contributions.
Low contributions.
Medium-low contributions.
Medium-high contributions.
High contributions.
More
Contribution activity
August 2026
Sriram-Mullapudi/Sriram-Mullapudi
11 commits
Loading
Seeing something unexpected? Take a look at the GitHub profile guide.

Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information

The analytics workflow is working now. What remains is README cleanup.

The lines such as “GitHub profile contribution summary” may simply be image alternative text in the page text you copied. The real problem is that setup instructions are still visible to visitors.

Remove the unwanted instructions
Open your profile repository.
Open README.md.
Click the pencil icon.
Press Ctrl + F.
Search for:
profile-summary-card-output/
Delete this entire visible block:
profile-summary-card-output/
└── github_dark/
    ├── 0-profile-details.svg
    ├── 1-repos-per-language.svg
    ├── 2-most-commit-language.svg
    ├── 3-stats.svg
    └── 4-productive-time.svg

Check the Code tab of your profile repository. If profile-summary-card-output is not present, the new analytics workflow has not generated or committed the files yet.

Also delete every remaining URL containing either of these domains from README.md:

github-readme-stats.vercel.app
streak-stats.demolab.com

Do not delete the analytics image tags above it.

Replace the analytics section cleanly

Your final section should look like this:

## GitHub analytics

<div align="center">

<img
  width="96%"
  src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/0-profile-details.svg"
  alt="GitHub profile contribution summary"
/>

<br/><br/>

<img
  width="48%"
  src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/1-repos-per-language.svg"
  alt="Repositories by language"
/>
<img
  width="48%"
  src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/2-most-commit-language.svg"
  alt="Most-used commit languages"
/>

<br/><br/>

<img
  width="48%"
  src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/3-stats.svg"
  alt="GitHub repository statistics"
/>
<img
  width="48%"
  src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/4-productive-time.svg"
  alt="Contribution activity by time of day"
/>

<br/><br/>

<img
  width="96%"
  src="https://github-readme-activity-graph.vercel.app/graph?username=Sriram-Mullapudi&bg_color=0B0E14&color=CBD5E1&line=2563EB&point=2DD4BF&area=true&area_color=1E3A8A&hide_border=true&custom_title=Contribution%20Activity"
  alt="GitHub contribution activity graph"
/>

</div>
Remove the snake placeholder

Your README currently says:

The animated contribution snake will appear here after the included workflow is enabled.

Since your snake workflow already exists, either replace that placeholder with your existing snake image or remove the entire Contribution journey section temporarily.

For a cleaner profile right now, delete:

## Contribution journey

<div align="center">
<sub>The animated contribution snake will appear here after the included workflow is enabled.</sub>
</div>
Delete the accidental file

From the repository root, delete the separate file named:

Delete

It is not part of your README and should not remain in the repository.

Save

Commit the changes with:

Clean up profile README

Then refresh the public profile with:

Ctrl + Shift + R

After these changes, the visible setup instructions and unfinished snake message will be gone, leaving only the polished profile content and analytics.

Pasted markdown.md
File
Give me the updated 
Worked for 17s

Here is the cleaned and updated README. It repairs the truncated typing animation and introduction, uses the generated analytics SVGs, removes all public setup instructions, and removes the unfinished snake placeholder.

README_updated.md

Replace your repository’s current README.md with this file, then commit with:

Clean up and finalize profile README

README_updated.md
Document

README_updated.md

<!-- GitHub Profile README for Sriram Mullapudi Profile repository: Sriram-Mullapudi/Sriram-Mullapudi Optional links still requiring confirmation: - Replace YOUR_LEETCODE_USERNAME before enabling the LeetCode badge. - Replace YOUR_CREDLY_CREDENTIAL_URL before enabling the AWS credential badge. -->

<!-- ============================== HERO ============================== -->




<div align="center">

<a href="https://readme-typing-svg.demolab.com"> <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=20&duration=2800&pause=900&color=60A5FA&center=true&vCenter=true&repeat=true&width=780&height=42&lines=Java+%2B+Spring+Boot+services+for+high-volume+systems;React+%2B+TypeScript+applications+for+operational+workflows;Kafka+pipelines+processing+500K%2B+events+per+day;Reliable+software+for+payments%2C+identity%2C+and+data" alt="Java and Spring Boot services; React and TypeScript applications; Kafka pipelines; reliable systems" /> </a>

<br/>

<a href="mailto:srirammullapudi20@gmail.com"> <img src="https://img.shields.io/badge/Email-0B0E14?style=for-the-badge&logo=gmail&logoColor=60A5FA" alt="Email" /> </a> <a href="https://linkedin.com/in/srirammullapudi"> <img src="https://img.shields.io/badge/LinkedIn-0B0E14?style=for-the-badge&logo=linkedin&logoColor=60A5FA" alt="LinkedIn" /> </a> <a href="https://github.com/Sriram-Mullapudi"> <img src="https://img.shields.io/badge/GitHub-0B0E14?style=for-the-badge&logo=github&logoColor=F8FAFC" alt="GitHub" /> </a>

<!-- Replace YOUR_LEETCODE_USERNAME, then uncomment this badge. <a href="https://leetcode.com/u/YOUR_LEETCODE_USERNAME/"> <img src="https://img.shields.io/badge/LeetCode-0B0E14?style=for-the-badge&logo=leetcode&logoColor=F59E0B" alt="LeetCode" /> </a> -->

<!-- Replace YOUR_CREDLY_CREDENTIAL_URL, then uncomment this badge. <a href="YOUR_CREDLY_CREDENTIAL_URL"> <img src="https://img.shields.io/badge/AWS_Certified-0B0E14?style=for-the-badge&logo=amazonwebservices&logoColor=FF9900" alt="AWS Certified Cloud Practitioner" /> </a> -->

<br/><br/>

<img src="https://komarev.com/ghpvc/?username=Sriram-Mullapudi&style=flat-square&color=2563EB&label=PROFILE+VIEWS" alt="Profile views" />

</div>

<!-- =========================== INTRODUCTION ========================== -->

Engineering reliable systems at scale

I am a full-stack software engineer with 4+ years of experience building Java and Spring Boot services and React applications for high-volume payment and identity systems.

My work includes Kafka workflows processing 500K+ events per day on a platform handling 10M+ annual transactions, a 30% reduction in end-to-end latency, and React/TypeScript dashboards used daily by 150+ operations analysts.

<table> <tr> <td width="25%" align="center"><strong>10M+</strong><br/><sub>annual transactions</sub></td> <td width="25%" align="center"><strong>500K+</strong><br/><sub>daily Kafka events</sub></td> <td width="25%" align="center"><strong>30%</strong><br/><sub>latency reduction</sub></td> <td width="25%" align="center"><strong>150+</strong><br/><sub>daily dashboard users</sub></td> </tr> </table>

<!-- ============================== ABOUT ============================== -->

About me
role: Full-Stack Software Engineer
experience: 4+ years
core_stack:
  - Java 17
  - Spring Boot
  - React
  - TypeScript
  - Kafka
  - AWS
engineering_focus:
  - Distributed payment systems
  - Event-driven workflows
  - Identity and access management
  - Full-stack operational tooling
education: M.S. in Computer Science, University of South Florida
gpa: 3.96 / 4.00
mobility: Open to relocation
Current focus
Designing Java 17 and Spring Boot services for validation, routing, status tracking, and multi-tenant systems.
Building React, TypeScript, and Redux Toolkit interfaces that turn operational data into usable workflows.
Developing event-driven systems with idempotent processing, recovery paths, and downstream failure isolation.
Applying AWS, Docker, Terraform, GitHub Actions, and Jenkins to deployment and delivery workflows.

<!-- =========================== TECHNOLOGY ============================ -->

Technology stack

<div align="center">

Languages

<img src="https://skillicons.dev/icons?i=java,ts,js,rust,python,c&theme=dark" alt="Java, TypeScript, JavaScript, Rust, Python, and C" />

Frontend

<img src="https://skillicons.dev/icons?i=react,nextjs,redux,tailwind,materialui,html,css&theme=dark" alt="React, Next.js, Redux, Tailwind CSS, Material UI, HTML, and CSS" />

Backend & data

<img src="https://skillicons.dev/icons?i=spring,nodejs,express,postgres,mysql,redis,sqlite,kafka&theme=dark" alt="Spring, Node.js, Express, PostgreSQL, MySQL, Redis, SQLite, and Kafka" />

Cloud, delivery & tooling

<img src="https://skillicons.dev/icons?i=aws,docker,terraform,githubactions,jenkins,git,linux&theme=dark" alt="AWS, Docker, Terraform, GitHub Actions, Jenkins, Git, and Linux" />

</div>

<details> <summary><strong>Complete skills matrix</strong></summary> <br/>

Area	Skills
Languages	Java, TypeScript, JavaScript, SQL, Rust, Python, C
Frontend	React, Next.js, Redux Toolkit, Tailwind CSS, MUI, HTML, CSS
Backend	Spring Boot, Spring Security, Spring Data JPA, Hibernate, Node.js, Express.js, REST APIs, GraphQL, Kafka, OAuth 2.0, JWT
Data	PostgreSQL, Oracle, MySQL, Redis, SQLite, pgvector
Cloud & DevOps	AWS ECS Fargate, EC2, RDS, S3, IAM, CloudWatch, Docker, Terraform, GitHub Actions, Jenkins, CI/CD
Testing & Tools	JUnit 5, Mockito, Cypress, Jest, SonarQube, Git, Linux
Architecture	Microservices, event-driven systems, API design, idempotent processing, multi-tenant systems, RAG

</details>

<!-- ============================ EXPERIENCE =========================== -->

Experience highlights
JPMorgan Chase & Co. — Software Engineer, Full Stack

<sub>Payments Platform · Tampa, Florida · March 2025 – May 2026</sub>

Developed Java 17 and Spring Boot services for payment validation, routing, and status tracking across a distributed platform handling 10M+ transactions annually.
Migrated synchronous validation flows to Kafka workflows processing 500K+ events daily, reducing end-to-end latency by 30%.
Built React, TypeScript, and Redux Toolkit investigation dashboards used daily by 150+ operations analysts.
Increased automated test coverage from 65% to 85%+ and enforced SonarQube quality gates in Jenkins and GitHub Actions pipelines.
Designed Oracle and PostgreSQL schemas and data-access layers for payment workflows.
Accenture — Associate Software Engineer

<sub>Chennai, India · October 2021 – July 2024</sub>

Implemented Okta-based OAuth 2.0/JWT authentication and Spring Security RBAC for applications serving 25K+ users.
Automated user provisioning, role assignment, and access management through Microsoft Graph and Google Workspace APIs.
Helped migrate backend services to AWS, contributing to a 15% reduction in production incidents.
Tuned MySQL and PostgreSQL queries, reducing high-volume REST endpoint response times by 20%.
Increased backend test coverage to 80%+ and mentored three junior engineers.

<!-- ============================= PROJECTS ============================ -->

Selected projects

<table> <tr> <td width="50%" valign="top">

Multi-Tenant Knowledge Search Platform

A hybrid retrieval system combining pgvector HNSW search, PostgreSQL full-text search, and Reciprocal Rank Fusion.

Highlights

Citation-backed answers streamed over Server-Sent Events
Keyword-search fallback when the LLM service is unavailable
JWT and refresh-token authentication with RBAC
Owner-scoped queries, execution tracing, and append-only audit records
ECS Fargate, RDS, ElastiCache, ALB, Secrets Manager, Terraform, and GitHub Actions with OIDC

Java 17 Spring Boot React PostgreSQL pgvector Redis AWS Docker Terraform

<!-- Add the repository URL only after confirming the exact public repository: [View project →](https://github.com/Sriram-Mullapudi/REPOSITORY_NAME) -->

</td> <td width="50%" valign="top">

Offline-First Point-of-Sale System

An installable Windows point-of-sale application supporting offline sales, refunds, inventory, promotions, loyalty, and shift reconciliation.

Highlights

Business and authorization rules centralized in the Rust backend
Atomic SQLite operations for transaction integrity
RBAC and Argon2 PIN hashing
Append-only audit logs
Duplicate-payment controls

Rust Tauri 2 SQLite React TypeScript

<!-- Add the repository URL only after confirming the exact public repository: [View project →](https://github.com/Sriram-Mullapudi/REPOSITORY_NAME) -->

</td> </tr> </table>

<!-- ============================== STATS ============================== -->

GitHub analytics

<div align="center">

<img width="96%" src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/0-profile-details.svg" alt="GitHub profile contribution summary" />

<br/><br/>

<img width="48%" src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/1-repos-per-language.svg" alt="Repositories by language" />
<img width="48%" src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/2-most-commit-language.svg" alt="Most-used commit languages" />

<br/><br/>

<img width="48%" src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/3-stats.svg" alt="GitHub repository statistics" />
<img width="48%" src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/4-productive-time.svg" alt="Contribution activity by time of day" />

<br/><br/>

<img width="96%" src="https://github-readme-activity-graph.vercel.app/graph?username=Sriram-Mullapudi&bg_color=0B0E14&color=CBD5E1&line=2563EB&point=2DD4BF&area=true&area_color=1E3A8A&hide_border=true&custom_title=Contribution%20Activity" alt="GitHub contribution activity graph" />

</div>

<!-- =========================== ACHIEVEMENTS ========================== -->

Achievements & certification

<div align="center">

<img width="96%" src="https://github-profile-trophy.vercel.app/?username=Sriram-Mullapudi&theme=algolia&no-frame=true&no-bg=true&margin-w=8&margin-h=8&column=6" alt="GitHub profile trophies" />

</div>

AWS Certified Cloud Practitioner — Amazon Web Services; credential verifiable on Credly.
Outstanding Performer at Accenture — recognized for team-level initiatives and deliverables.
LeetCode — 1,436 problems solved across data structures and algorithms; global rank 8,791.

<!-- ============================ EDUCATION ============================ -->

Education
University of South Florida

Master of Science in Computer Science · GPA: 3.96 / 4.00

<!-- ============================== CTA ================================ -->

Let’s connect

<div align="center">

I build full-stack software with Java, Spring Boot, React, Kafka, and AWS—with an emphasis on reliability, performance, and usable operational workflows.

<br/>

<a href="mailto:srirammullapudi20@gmail.com"> <img src="https://img.shields.io/badge/Start_a_conversation-2563EB?style=for-the-badge&logo=gmail&logoColor=white" alt="Start a conversation by email" /> </a> <a href="https://linkedin.com/in/srirammullapudi"> <img src="https://img.shields.io/badge/Connect_on_LinkedIn-0B0E14?style=for-the-badge&logo=linkedin&logoColor=60A5FA" alt="Connect on LinkedIn" /> </a>

<br/><br/>

Open to relocation

</div>

<!-- ============================= FOOTER ============================== -->

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:0B0E14,45:111827,100:2563EB" alt="" />

README_updated.md

<!-- GitHub Profile README for Sriram Mullapudi Profile repository: Sriram-Mullapudi/Sriram-Mullapudi Optional links still requiring confirmation: - Replace YOUR_LEETCODE_USERNAME before enabling the LeetCode badge. - Replace YOUR_CREDLY_CREDENTIAL_URL before enabling the AWS credential badge. -->

<!-- ============================== HERO ============================== -->




<div align="center">

<a href="https://readme-typing-svg.demolab.com"> <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=20&duration=2800&pause=900&color=60A5FA&center=true&vCenter=true&repeat=true&width=780&height=42&lines=Java+%2B+Spring+Boot+services+for+high-volume+systems;React+%2B+TypeScript+applications+for+operational+workflows;Kafka+pipelines+processing+500K%2B+events+per+day;Reliable+software+for+payments%2C+identity%2C+and+data" alt="Java and Spring Boot services; React and TypeScript applications; Kafka pipelines; reliable systems" /> </a>

<br/>

<a href="mailto:srirammullapudi20@gmail.com"> <img src="https://img.shields.io/badge/Email-0B0E14?style=for-the-badge&logo=gmail&logoColor=60A5FA" alt="Email" /> </a> <a href="https://linkedin.com/in/srirammullapudi"> <img src="https://img.shields.io/badge/LinkedIn-0B0E14?style=for-the-badge&logo=linkedin&logoColor=60A5FA" alt="LinkedIn" /> </a> <a href="https://github.com/Sriram-Mullapudi"> <img src="https://img.shields.io/badge/GitHub-0B0E14?style=for-the-badge&logo=github&logoColor=F8FAFC" alt="GitHub" /> </a>

<!-- Replace YOUR_LEETCODE_USERNAME, then uncomment this badge. <a href="https://leetcode.com/u/YOUR_LEETCODE_USERNAME/"> <img src="https://img.shields.io/badge/LeetCode-0B0E14?style=for-the-badge&logo=leetcode&logoColor=F59E0B" alt="LeetCode" /> </a> -->

<!-- Replace YOUR_CREDLY_CREDENTIAL_URL, then uncomment this badge. <a href="YOUR_CREDLY_CREDENTIAL_URL"> <img src="https://img.shields.io/badge/AWS_Certified-0B0E14?style=for-the-badge&logo=amazonwebservices&logoColor=FF9900" alt="AWS Certified Cloud Practitioner" /> </a> -->

<br/><br/>

<img src="https://komarev.com/ghpvc/?username=Sriram-Mullapudi&style=flat-square&color=2563EB&label=PROFILE+VIEWS" alt="Profile views" />

</div>

<!-- =========================== INTRODUCTION ========================== -->

Engineering reliable systems at scale

I am a full-stack software engineer with 4+ years of experience building Java and Spring Boot services and React applications for high-volume payment and identity systems.

My work includes Kafka workflows processing 500K+ events per day on a platform handling 10M+ annual transactions, a 30% reduction in end-to-end latency, and React/TypeScript dashboards used daily by 150+ operations analysts.

<table> <tr> <td width="25%" align="center"><strong>10M+</strong><br/><sub>annual transactions</sub></td> <td width="25%" align="center"><strong>500K+</strong><br/><sub>daily Kafka events</sub></td> <td width="25%" align="center"><strong>30%</strong><br/><sub>latency reduction</sub></td> <td width="25%" align="center"><strong>150+</strong><br/><sub>daily dashboard users</sub></td> </tr> </table>

<!-- ============================== ABOUT ============================== -->

About me
role: Full-Stack Software Engineer
experience: 4+ years
core_stack:
  - Java 17
  - Spring Boot
  - React
  - TypeScript
  - Kafka
  - AWS
engineering_focus:
  - Distributed payment systems
  - Event-driven workflows
  - Identity and access management
  - Full-stack operational tooling
education: M.S. in Computer Science, University of South Florida
gpa: 3.96 / 4.00
mobility: Open to relocation
Current focus
Designing Java 17 and Spring Boot services for validation, routing, status tracking, and multi-tenant systems.
Building React, TypeScript, and Redux Toolkit interfaces that turn operational data into usable workflows.
Developing event-driven systems with idempotent processing, recovery paths, and downstream failure isolation.
Applying AWS, Docker, Terraform, GitHub Actions, and Jenkins to deployment and delivery workflows.

<!-- =========================== TECHNOLOGY ============================ -->

Technology stack

<div align="center">

Languages

<img src="https://skillicons.dev/icons?i=java,ts,js,rust,python,c&theme=dark" alt="Java, TypeScript, JavaScript, Rust, Python, and C" />

Frontend

<img src="https://skillicons.dev/icons?i=react,nextjs,redux,tailwind,materialui,html,css&theme=dark" alt="React, Next.js, Redux, Tailwind CSS, Material UI, HTML, and CSS" />

Backend & data

<img src="https://skillicons.dev/icons?i=spring,nodejs,express,postgres,mysql,redis,sqlite,kafka&theme=dark" alt="Spring, Node.js, Express, PostgreSQL, MySQL, Redis, SQLite, and Kafka" />

Cloud, delivery & tooling

<img src="https://skillicons.dev/icons?i=aws,docker,terraform,githubactions,jenkins,git,linux&theme=dark" alt="AWS, Docker, Terraform, GitHub Actions, Jenkins, Git, and Linux" />

</div>

<details> <summary><strong>Complete skills matrix</strong></summary> <br/>

Area	Skills
Languages	Java, TypeScript, JavaScript, SQL, Rust, Python, C
Frontend	React, Next.js, Redux Toolkit, Tailwind CSS, MUI, HTML, CSS
Backend	Spring Boot, Spring Security, Spring Data JPA, Hibernate, Node.js, Express.js, REST APIs, GraphQL, Kafka, OAuth 2.0, JWT
Data	PostgreSQL, Oracle, MySQL, Redis, SQLite, pgvector
Cloud & DevOps	AWS ECS Fargate, EC2, RDS, S3, IAM, CloudWatch, Docker, Terraform, GitHub Actions, Jenkins, CI/CD
Testing & Tools	JUnit 5, Mockito, Cypress, Jest, SonarQube, Git, Linux
Architecture	Microservices, event-driven systems, API design, idempotent processing, multi-tenant systems, RAG

</details>

<!-- ============================ EXPERIENCE =========================== -->

Experience highlights
JPMorgan Chase & Co. — Software Engineer, Full Stack

<sub>Payments Platform · Tampa, Florida · March 2025 – May 2026</sub>

Developed Java 17 and Spring Boot services for payment validation, routing, and status tracking across a distributed platform handling 10M+ transactions annually.
Migrated synchronous validation flows to Kafka workflows processing 500K+ events daily, reducing end-to-end latency by 30%.
Built React, TypeScript, and Redux Toolkit investigation dashboards used daily by 150+ operations analysts.
Increased automated test coverage from 65% to 85%+ and enforced SonarQube quality gates in Jenkins and GitHub Actions pipelines.
Designed Oracle and PostgreSQL schemas and data-access layers for payment workflows.
Accenture — Associate Software Engineer

<sub>Chennai, India · October 2021 – July 2024</sub>

Implemented Okta-based OAuth 2.0/JWT authentication and Spring Security RBAC for applications serving 25K+ users.
Automated user provisioning, role assignment, and access management through Microsoft Graph and Google Workspace APIs.
Helped migrate backend services to AWS, contributing to a 15% reduction in production incidents.
Tuned MySQL and PostgreSQL queries, reducing high-volume REST endpoint response times by 20%.
Increased backend test coverage to 80%+ and mentored three junior engineers.

<!-- ============================= PROJECTS ============================ -->

Selected projects

<table> <tr> <td width="50%" valign="top">

Multi-Tenant Knowledge Search Platform

A hybrid retrieval system combining pgvector HNSW search, PostgreSQL full-text search, and Reciprocal Rank Fusion.

Highlights

Citation-backed answers streamed over Server-Sent Events
Keyword-search fallback when the LLM service is unavailable
JWT and refresh-token authentication with RBAC
Owner-scoped queries, execution tracing, and append-only audit records
ECS Fargate, RDS, ElastiCache, ALB, Secrets Manager, Terraform, and GitHub Actions with OIDC

Java 17 Spring Boot React PostgreSQL pgvector Redis AWS Docker Terraform

<!-- Add the repository URL only after confirming the exact public repository: [View project →](https://github.com/Sriram-Mullapudi/REPOSITORY_NAME) -->

</td> <td width="50%" valign="top">

Offline-First Point-of-Sale System

An installable Windows point-of-sale application supporting offline sales, refunds, inventory, promotions, loyalty, and shift reconciliation.

Highlights

Business and authorization rules centralized in the Rust backend
Atomic SQLite operations for transaction integrity
RBAC and Argon2 PIN hashing
Append-only audit logs
Duplicate-payment controls

Rust Tauri 2 SQLite React TypeScript

<!-- Add the repository URL only after confirming the exact public repository: [View project →](https://github.com/Sriram-Mullapudi/REPOSITORY_NAME) -->

</td> </tr> </table>

<!-- ============================== STATS ============================== -->

GitHub analytics

<div align="center">

<img width="96%" src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/0-profile-details.svg" alt="GitHub profile contribution summary" />

<br/><br/>

<img width="48%" src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/1-repos-per-language.svg" alt="Repositories by language" />
<img width="48%" src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/2-most-commit-language.svg" alt="Most-used commit languages" />

<br/><br/>

<img width="48%" src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/3-stats.svg" alt="GitHub repository statistics" />
<img width="48%" src="https://raw.githubusercontent.com/Sriram-Mullapudi/Sriram-Mullapudi/main/profile-summary-card-output/github_dark/4-productive-time.svg" alt="Contribution activity by time of day" />

<br/><br/>

<img width="96%" src="https://github-readme-activity-graph.vercel.app/graph?username=Sriram-Mullapudi&bg_color=0B0E14&color=CBD5E1&line=2563EB&point=2DD4BF&area=true&area_color=1E3A8A&hide_border=true&custom_title=Contribution%20Activity" alt="GitHub contribution activity graph" />

</div>

<!-- =========================== ACHIEVEMENTS ========================== -->

Achievements & certification

<div align="center">

<img width="96%" src="https://github-profile-trophy.vercel.app/?username=Sriram-Mullapudi&theme=algolia&no-frame=true&no-bg=true&margin-w=8&margin-h=8&column=6" alt="GitHub profile trophies" />

</div>

AWS Certified Cloud Practitioner — Amazon Web Services; credential verifiable on Credly.
Outstanding Performer at Accenture — recognized for team-level initiatives and deliverables.
LeetCode — 1,436 problems solved across data structures and algorithms; global rank 8,791.

<!-- ============================ EDUCATION ============================ -->

Education
University of South Florida

Master of Science in Computer Science · GPA: 3.96 / 4.00

<!-- ============================== CTA ================================ -->

Let’s connect

<div align="center">

I build full-stack software with Java, Spring Boot, React, Kafka, and AWS—with an emphasis on reliability, performance, and usable operational workflows.

<br/>

<a href="mailto:srirammullapudi20@gmail.com"> <img src="https://img.shields.io/badge/Start_a_conversation-2563EB?style=for-the-badge&logo=gmail&logoColor=white" alt="Start a conversation by email" /> </a> <a href="https://linkedin.com/in/srirammullapudi"> <img src="https://img.shields.io/badge/Connect_on_LinkedIn-0B0E14?style=for-the-badge&logo=linkedin&logoColor=60A5FA" alt="Connect on LinkedIn" /> </a>

<br/><br/>

Open to relocation

</div>

<!-- ============================= FOOTER ============================== -->

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:0B0E14,45:111827,100:2563EB" alt="" />
