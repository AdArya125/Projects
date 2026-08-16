# Project Portfolio

A curated collection of my academic, research, and personal software projects.

This repository serves as a central index to all of my major projects. Each project is maintained either in its own dedicated repository (full source, docs, and results) or as a subfolder here for smaller, self-contained work.

---

## About

**Name:** Aditya Arya <br>
**Institution:** Indian Institute of Technology Delhi <br>
**Program:** Master of Technology (M.Tech.) <br>
**Department:** Computer Science and Engineering <br> 

**Areas of Interest**
- Artificial Intelligence and Machine Learning
- Distributed Systems
- Data Science
- Systems Programming
- Algorithms
- Parallel Programming

---

# M.Tech Coursework

## Semester I

### COL7203 - Logic for Computer Science
##### Professor - [Vaishnavi Sundararajan](https://vaishs.github.io/)

| Title | Description | Technologies | Repository |
|---------|-------------|--------------|------------|
| **Intuitionistic propositional logic** | Automatic theorem proving, verification methods, formal methods | Lean 4 | [Repository](https://github.com/AdArya125/formalizing-logic-in-lean) |




### COL7333 - Introduction to Artificial Intelligence
##### Professor - [Mausam](https://www.cse.iitd.ac.in/~mausam/)


| Project | Description | Technologies | Repository |
|---------|-------------|--------------|------------|
| Assignment 1 | Search/solver-based assignment for COL7333 | C++ | [Repository](https://github.com/AdArya125/AI_assignment_1) |
| Assignment 2 | Build a Game-Playing Agent that plays Stones & Rivers Board Game using Adversarial Search | Python | [Repository](https://github.com/AdArya125/AI_assignment_2) |
| Assignment 3 | Formulation of the City Metro Planning problem as a SAT problem, solved using MiniSat, with decoding/visualization of the output | Python | [Repository](https://github.com/AdArya125/AI_assignment_3) |

#### Related Independent Work
*(not a COL7333 assignment - included here since it applies AI search algorithms)*

| Project | Description | Technologies | Repository |
|---------|-------------|--------------|------------|
| **Automated Cracking of Substitution Ciphers** | Cracks monoalphabetic substitution ciphers using AI search: a statistical English language model (uni/bi/tri/quad-gram + word frequencies) scores candidates, an initial key estimate comes from the Hungarian algorithm on bigram cost matrices, then local/global optimization search refines the key by maximizing decryption likelihood | Python | [Repository](https://github.com/AdArya125/Substitution-Ciphers-Cracking) |

---

## COD7001  - Systems Concepts (Cornerstone Project)
##### Professor - [Kolin Paul](https://kolinpaul.github.io/)

| Assignment | Description | Repository |
|-------------|--------------|------------|
| **Unix Shell** | First project of the Cornerstone sequence - a Unix shell implementation covering `fork`/`exec`, process lifecycle, and file descriptor inheritance | [Repository](https://github.com/AdArya125/Unix-Shell-Cornerstone-P1) |
| **Minimal Debugger** | A ptrace-based debugger supporting breakpoint insertion/removal, register dumps, single-stepping, and a CLI command interface | [Repository](https://github.com/AdArya125/Minimal-Debugger-Cornerstone-P2) |
| **Parser (Flex & Bison)** | Parser for a small C-like language built with Flex/Bison; produces an AST and catches syntax and semantic errors. Team project with Chirag Kathpalia, under Prof. Kolin Paul | [Repository](https://github.com/AdArya125/PARSER-USING-FLEX-BISON-Cornerstone-P3) |
| **Bytecode Virtual Machine** | A custom stack-based bytecode VM - instruction dispatch, arithmetic/control-flow opcodes, and an evolving stack design (unified stack → separate data/control frames) | [Repository](https://github.com/AdArya125/Bytecode-Virtual-Machine-Cornerstone-P4) |

#### Capstone Projects

| Project | Description | Repository |
|-------------|--------------|------------|
| **NEXUS** – Unified Execution Environment | A complete language runtime for a custom scripting language - compiler, assembler, and disassembler feeding into the custom bytecode VM - unified with the custom shell, parser, and garbage collector into one system that manages the full lifecycle of user programs and enables end-to-end debugging and memory analysis | [Repository](https://github.com/AdArya125/NEXUS-Unified-Execution-Environment) |
| **PULSE** – User-Level Resource-Aware Runtime | A user-space execution environment that schedules lightweight coroutine tasks (`M:N` or `M:1` mode) via `swapcontext()`-based context switching, with a polled resource monitor driving adaptive scheduling across FIFO/round-robin/priority/resource-aware policies. Ships with live terminal (ncurses) and web dashboards | [Repository](https://github.com/AdArya125/PULSE-Systems_Cornerstone_Project_Resource_Manager-COD7001) |

---

## Semester II

### COL7880 — Introduction to Parallel and Distributed Programming
##### Professor - [Subodh Sharma](https://subodhvsharma.github.io/)
 
| Project | Description | Technologies | Repository |
|---------|-------------|--------------|------------|
| **Assignment 1** – Parallel Order-Book Processing | Processes a stream of bit-packed, bit-stuffed exchange order packets in parallel with OpenMP: memoized parallel decoding, task-based overlapping live display snapshots, thread-local aggregation for per-stock order statistics, and a reduction-based total traded amount | C++, OpenMP | [Repository](https://github.com/AdArya125/OpenMP-Order-Book-Processing-COL7880-A1) |
| **Assignment 2** – GPU-Accelerated Nearest Neighbours & K-Means | Exact KNN (tiled all-pairs CUDA kernel, register-resident per-thread max-heap), Approximate KNN (grid-based cell search trading bounded accuracy for speed), and K-Means (OpenMP-parallel Lloyd's algorithm) benchmarked against a CPU baseline — up to ~330× speedup on exact KNN | C++, CUDA, OpenMP | [Repository](https://github.com/AdArya125/CUDA-KNN-KMeans-COL7880-A2) |
| **Assignment 3** – Budgeted Maximum Weight Clique | Exact Branch & Bound solver for the Budgeted Maximum Weight Clique problem, parallelized across MPI ranks with dynamic work-unit distribution (round-robin dispatch of shallow B&B snapshots) and global bound sharing via `MPI_Allreduce`; uses structural (graph-coloring) and resource (fractional knapsack) pruning bounds with bitset adjacency | C++, MPI | [Repository](https://github.com/AdArya125/MPI-Budgeted-Max-Weight-Clique) |
### COL7560 - Machine Learning for Networked Systems
##### Professor - [Tarun Mangla](https://tarunmangla.github.io/)

| Project | Description | Technologies | Repository |
|---------|-------------|--------------|------------|
| **VideoNOC** | Our own video-conferencing Network Operations Center project, rewritten as a session-first v2: groups raw network flows into sessions correctly first, then visualizes them, with ML kept as a supporting layer rather than the main focus. Carries forward the lower-layer packet extraction/RTP-audit/flow-assembly components from our v1 while rebuilding sessionization and the dashboard cleanly | Python | [Repository](https://github.com/AdArya125/VideoNOC) |

---

# B.Tech Projects

### Final Projects

| Project | Description | Technologies | Repository |
|---------|-------------|--------------|------------|
| **AI Agent powered by Tools** *(B.Tech Final Project)* | An end-to-end AI agent powered by Claude 3.5 Haiku, orchestrated with LangChain, LangGraph, and IBM Watsonx Flows. Dynamically invokes tools (Wikipedia, YouTube transcripts, Google Books, currency conversion, REST/GraphQL APIs) for context-aware responses via a Next.js chat interface | Next.js, TypeScript, Tailwind, Convex, Clerk, LangChain, LangGraph, Claude 3.5 Haiku, IBM Watsonx | [Repository](https://github.com/AdArya125/AI-Agent-powered-by-Tools) |
| **Speech Emotion Recognition (SER)** *(B.Tech Specialization Final Project)* | Classifies emotion from spoken audio using a three-model comparative architecture - fine-tuned Wav2Vec 2.0, a 1D Temporal CNN, and a Sequential LSTM - trained on a unified 12,000+ sample corpus (RAVDESS, CREMA-D, TESS, SAVEE). Includes a real-time Flask dashboard for live microphone testing with model switching. Best result: 77.32% test accuracy (Wav2Vec 2.0) | Python, PyTorch, Wav2Vec 2.0, Flask, Docker | [Repository](https://github.com/AdArya125/Speech-emotion-recognition) |

### Mini Projects
*(smaller B.Tech projects, kept as subfolders in this repository)*

| Project | Description | Technologies | Location |
|---------|-------------|--------------|----------|
| **Biometric Attendance System** | Fingerprint-based attendance system on Arduino Nano - enroll/verify/delete modes with passcode-protected admin actions, fingerprint sensor + LCD + HC-05 Bluetooth module | Arduino, C++ | [Folder](./Biometric%20attendence%20System) |
| **Sentiment Analysis - BlackCoffer** | Scrapes article text from a list of URLs and computes sentiment (positive/negative/polarity/subjectivity) and readability metrics (avg. sentence length, % complex words, FOG index), exporting results to Excel | Python, BeautifulSoup, Pandas | [Folder](./Sentiment%20Analysis%20-%20BlackCoffer) |
| **Web Scraping - GitHub Repositories** | Given a GitHub Collection link, scrapes every included repository's metadata (owner, name, stars, forks, language, description) into a CSV | Python, BeautifulSoup | [Folder](./Web%20Scrapping%20-%20Github%20Repositories) |

---

# Systems Programming

| Project | Description | Technologies | Repository |
|---------|-------------|--------------|------------|
| **eBPF API Latency Profiler** | A standalone Linux observability tool that captures HTTP/1.1 traffic at the socket layer using eBPF, with no application modification required. A socket-filter eBPF program streams TCP segment metadata into a ring buffer; a userspace pipeline (collector → correlator → enricher → output) reconstructs per-connection HTTP/1.1 request/response pairs, enriches events with PID/process/container via `/proc`, and emits per-request latency as a JSONL stream | C, eBPF, libbpf, Docker | [Repository](https://github.com/AdArya125/eBPF-API-Latency-Profiler) |
| **MatMul-Bench** – Dense Matrix Multiplication Optimization & Performance Study | A systems performance study tracking dense matrix multiplication from a naive O(N³) baseline through loop reordering, cache blocking, OpenMP multithreading, AVX2 SIMD (FMA3), CUDA (naive + shared-memory tiled), MPI, and hybrid MPI+OpenMP - up to ~377x speedup over naive on GPU. Empirically verified with Linux `perf` hardware counters (IPC, cache requests), Valgrind Cachegrind (L1 miss rates), and NVIDIA Nsight Compute (SM occupancy, throughput) | C++, CUDA, OpenMP, MPI, AVX2 | [Repository](https://github.com/AdArya125/MatMul-Bench-Dense-Matrix-Multiplication-Optimization-Performance-Study) |
| **Serverless / FaaS Platform** | A miniature Function-as-a-Service platform built from scratch: register a function, invoke via CLI/HTTP, get a result with real cold/warm starts, a runtime lifecycle state machine, scale-to-zero, self-healing recovery on dead runtimes, SQLite-backed persistence, Prometheus metrics, and a pluggable Docker/Kubernetes execution backend | C++, Docker, Kubernetes, SQLite, Prometheus | [Repository](https://github.com/AdArya125/Serverless-FaaS-Platform) |
| **Custom System Call** | Adds custom syscalls to a Linux kernel (6.6.39) built from source, boots via a static-BusyBox QEMU initramfs, and verifies invocation through `dmesg` | C, Linux Kernel, QEMU | [Repository](https://github.com/AdArya125/Custom_System_Call) |

---

# MLOps

A self-directed MLOps learning series - progressing from CI and Docker fundamentals through experiment tracking, data versioning, and Kubernetes-based monitoring to a full end-to-end capstone.

| Project | Description | Technologies | Repository |
|---------|-------------|--------------|------------|
| **MLOps Capstone Project** | Full MLOps pipeline for a sentiment analysis model on the IMDB dataset - MLflow (via DagsHub) experiment tracking, DVC data versioning, Flask serving, GitHub Actions CI/CD, Docker/DockerHub, AWS S3 + ECR | Python, MLflow, DVC, Flask, Docker, AWS | [Repository](https://github.com/AdArya125/MLOPS-Capstone-Project) |
| **Prometheus & Grafana on Minikube** | Deploys a Flask app with a metrics endpoint to Minikube, scrapes it with Prometheus, and visualizes it in Grafana | Python, Prometheus, Grafana, Kubernetes | [Repository](https://github.com/AdArya125/MLOPS-Prometheus-Grafana-Minikube) |
| **Prometheus & Grafana Notes** | Notes on observability in microservices - monitoring vs. observability, telemetry data, push vs. scrape metric collection | Prometheus, Grafana | [Repository](https://github.com/AdArya125/MLOPS-PRometheus-and-Graphana-Notes) |
| **Kubernetes Mini Project** | Notes/mini-implementation on incorporating Kubernetes into a GitHub Actions + ECR CI/CD workflow | Kubernetes | [Repository](https://github.com/AdArya125/K8S-Kubernetes-Mini-Project) |
| **Kubernetes Theory** | Beginner-friendly notes on distributed computing fundamentals, Kubernetes internals (API server, etcd, kubelet, kube-proxy), and microservices for MLOps | - | [Repository](https://github.com/AdArya125/MLOPS-Kubernetes-Theory) |
| **Vehicle Price Prediction** *(MLOps Project 1)* | End-to-end ML pipeline predicting vehicle prices - templated project structure, MongoDB Atlas ingestion, data validation/transformation, model training + evaluation with push to S3, Flask API deployed via Docker on EC2, GitHub Actions CI/CD | Python, MongoDB, Docker, AWS (S3, EC2), Flask | [Repository](https://github.com/AdArya125/MLOPS-Project-1) |
| **MLOps Docker Repo** | Docker fundamentals implemented via a project demo | Docker, Python | [Repository](https://github.com/AdArya125/MLOPS-Docker-Repo) |
| **MLOps CI** | Streamlit power-calculator app with pytest unit tests and a GitHub Actions CI workflow that runs tests on every push/PR | Python, Streamlit, GitHub Actions | [Repository](https://github.com/AdArya125/MLOPS-CI) |
| **Experiments with MLflow** | Experiment tracking demonstration using MLflow | Python, MLflow | [Repository](https://github.com/AdArya125/MLOPS-Experiments-with-MLFlow) |
| **Complete ML Pipeline** | Modular, reproducible SMS spam-classification pipeline (Random Forest) - DVC-versioned stages (ingestion → preprocessing → feature engineering → training → evaluation), DVCLive metrics tracking, AWS S3 remote | Python, DVC, DVCLive, AWS S3 | [Repository](https://github.com/AdArya125/MLOPS-Complete-ML-Pipeline) |
| **DVC Data Versioning** | Git + DVC workflow for versioning a generated CSV dataset across multiple revisions, using a local folder to simulate remote (S3) storage | Python, DVC | [Repository](https://github.com/AdArya125/MLOPS-DVC-DataVersion) |

---

# Open Source & Technical Writing

| Repository | Description | Topics | Link |
|------------|-------------|--------|------|
| **Primer to Machine Learning** | A structured repository covering machine learning fundamentals, algorithms, and practical implementations from mathematical foundations to deep learning | Python, Machine Learning, Deep Learning, NLP, Data Science, Reinforcement Learning | [Repository](https://github.com/AdArya125/Primer-to-Machine-Learning) |

---

# Technology Stack

## Programming Languages
- C++, C
- Python
- TypeScript / JavaScript
- Lean 4
- SQL

## Machine Learning & AI
- PyTorch, TensorFlow, Scikit-learn
- NumPy, Pandas, Matplotlib
- Wav2Vec 2.0 / Hugging Face Transformers
- MLflow, DVC
- LLM tool-calling / AI agents (Claude, LangChain, LangGraph, IBM Watsonx)

## Systems & Cloud
- Linux (kernel internals, syscalls)
- eBPF / libbpf
- Docker, Kubernetes
- QEMU
- Prometheus, Grafana
- SQLite, MongoDB
- AWS (IAM, S3, EC2, ECR)

## Web & App Development
- Next.js, Flask, Streamlit
- Tailwind CSS
- Convex, Clerk

## Hardware / Embedded
- Arduino

## Development Tools
- Git, GitHub, GitHub Actions
- Visual Studio Code, Jupyter Notebook

---

# Repository Organization

```
Project Portfolio
│
├── M.Tech Coursework
│   ├── Semester I  (COL7203, COD7001 Cornerstone: assignments + NEXUS/PULSE capstones)
│   └── Semester II (COL7333 + related independent work, COL7560)
├── B.Tech Projects
│   ├── Final Projects
│   └── Mini Projects (subfolders in this repository)
├── Systems Programming
├── MLOps
└── Open Source & Technical Writing
```

---

# Repository Naming Convention

Naming isn't fully uniform across repos, but there are consistent patterns by category:

- **Cornerstone Project (COD7001) assignments** use the suffix `-Cornerstone-P<n>`, e.g. `Unix-Shell-Cornerstone-P1`, `Bytecode-Virtual-Machine-Cornerstone-P4`.
- **MLOps learning-series repos** are prefixed `MLOPS-`, e.g. `MLOPS-CI`, `MLOPS-Complete-ML-Pipeline`.
- **AI coursework assignments (COL7333)** follow `AI_assignment_<n>`.
- Standalone systems/ML projects (e.g. `Serverless-FaaS-Platform`, `Speech-emotion-recognition`, `Substitution-Ciphers-Cracking`, `eBPF-API-Latency-Profiler`, `MatMul-Bench-Dense-Matrix-Multiplication-Optimization-Performance-Study`) use a descriptive project name with no course-code prefix.

---

# License

Each project repository contains its own license and documentation.

---

# Contact

**GitHub:** https://github.com/AdArya125

**LinkedIn:** https://www.linkedin.com/in/adarya125/

**Email:** adarya125@gmail.com
