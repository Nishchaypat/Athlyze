# Athlyze – A Personalized Fitness and Nutrition Platform

## Table of Contents

1.  [Project Overview](#1-project-overview)
2.  [Project Structure](#2-project-structure)
3.  [Prerequisites](#3-prerequisites)
4.  [Installation & Setup](#4-installation--setup)
5.  [Configuration](#5-configuration)
6.  [Running the Application](#6-running-the-application)
7.  [Features](#7-features)
8.  [Development](#8-development)
9.  [Documentation & References](#9-documentation--references)
10. [Performance Metrics](#10-performance-metrics)
11. [Troubleshooting](#11-troubleshooting)
12. [Contact](#12-contact)

---

## 1. Project Overview

Athlyze is an Agentic RAG–based personalized fitness and nutrition guidance system. It integrates scientific literature via a vector database and employs multi-agent workflows to generate personalized, research-backed plans. Key capabilities include:

* **User Profiling:** Captures demographics, dietary habits, and exercise routines.
* **Semantic Retrieval:** Uses adaptive, Agentic chunking and Google Gemini through LangFlow and AstraDB to extract relevant research (e.g., muscle development, nutrition).
* **Personalized Generation:** Produces structured weekly fitness and nutrition schedules, summarized into actionable guidelines with JSON schema enforcement.

Under the hood, Athlyze orchestrates four agentic stages (Section V.D in the paper) to:

1.  Dynamic Query Generation
2.  Plan Synthesis
3.  Guideline Extraction
4.  Schema-Constrained Output

---

## 2. Project Structure

```
athlyze/
├── api_flows_slow_method/
│   ├── nutrition_flow_api.py
│   └── training_flow_api.py
├── app/
│   ├── database/
│   │   ├── your_nutrition_plan.json
│   │   ├── your_nutrition_principles.json
│   │   ├── your_training_plan.json
│   │   └── your_training_principles.json
│   ├── flow/
│   │   ├── Chatbot.json
│   │   ├── Muscle.json
│   │   └── Nutrition.json
│   ├── local_flows/
│   │   ├── chatbot_local.py
│   │   ├── nutrition_flow_local.py
│   │   └── training_flow_local.py
│   ├── pages/
│   │   ├── Calendar.py
│   │   ├── Chat.py
│   │   ├── Nutrition.py
│   │   ├── Nutrition Principles.py
│   │   ├── Profile.py
│   │   └── Training Priciples.py  # Note: Typo in original, kept as is. Should be 'Principles'
│   └── Home.py
├── data_preprocessing/
│   ├── agentic_chunker.py
│   ├── chunking.ipynb
│   ├── data_clean.ipynb
│   ├── dataPreprocessing.ipynb
│   ├── different_approach.ipynb
│   ├── embeddingGenerator.ipynb
│   └── embedVisuals.ipynb
├── testing/
│   ├── test_cases.py
│   └── test_nutrition_flow.py
├── visuals/
│   ├── API_flow_time.png
│   ├── Local_flow_time.png
│   ├── corr_embedding.png
│   └── embedding_similarities.png
├── Final_Paper.pdf
├── Final_Presentation.pptx
└── requirements.txt
```

---

## 3. Prerequisites

Before proceeding, ensure you have:

* **Python 3.11+**
    ```bash
    python --version
    ```
* **pip** (bundled with recent Python).
* **Git**
* **Streamlit**
* **LangFlow**
* **Google Cloud Account** (for Gemini API)
* **AstraDB Account**

Note: Refer the requirements.txt
---

## 4. Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Nishchaypat/Athlyze.git
    cd Athlyze
    ```

2.  **Create & Activate Virtual Environment**
    * macOS/Linux:
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```
    * Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Verify LangFlow & AstraDB CLI**
    Follow the official docs to install, log in and steup:
    * LangFlow: [https://docs.langflow.org](https://docs.langflow.org)
    * AstraDB: [https://docs.datastax.com](https://docs.datastax.com/)

---

## 5. Configuration

Create a `.env` file in the project root with your credentials:

```python
# config.py
GEMINI_API_KEY       = "YOUR_GEMINI_API_KEY"
ASTRA_DB_APPLICATION_TOKEN = "YOUR_ASTRA_DB_TOKEN"
ASTRA_DB_API_ENDPOINT      = "YOUR_ASTRA_DB_DB_ID" # e.g., https://<db_id>-<region>.apps.astra.datastax.com
ASTRA_USER_ID              = "YOUR_ASTRA_DB_USERNAME" # Often 'token' when using application token
```

---

## 6. Running the Application

1.  **Launch the Backend & Frontend**
    ```bash
    streamlit run app/Home.py
    ```
2.  **Installs your flows under local_flows/ from export option in Langflow**

3.  **Access Locally**
    * Main Interface: [http://localhost:8501](http://localhost:8501)
    * Navigate through pages:
        * Profile
        * Nutrition Plan
        * Training Plan
        * Calendar
        * Chat

 4. **API Endpoints** (if running separately/online):
    * `POST /api/train` – Returns JSON structure S<sub>m</sub> for training.
    * `POST /api/nutrition` – Returns JSON structure S<sub>n</sub> for nutrition.

---

## 7. Features

* **Nutrition Planning**
    * Customized meal plans
    * Nutritional principles
    * Diet tracking
    * Research-backed recommendations
* **Training Programs**
    * Personalized workout schedules
    * Exercise principles
    * Progress tracking
    * Resistance training focus
* **Interactive Features**
    * Chat interface for questions
    * Calendar integration
    * Profile management
    * Progress visualization

---

## 8. Development

* **Data Processing**
    Jupyter notebooks in `data_preprocessing/` handle:
    * Data cleaning
    * Embedding generation
    * Chunking optimization
    * Visualization generation

---

## 9. Documentation & References

For the scientific foundations and implementation rationale, consult `Final_Paper.pdf`. Key references include:

* Retrieval-Augmented Generation fundamentals
* Agentic chunking strategies
* Embedding dimensionality and quality analyses

Additional papers are stored in the `research_papers/` directories (e.g., `nutrition_research_papers/` and `muscle_research_papers/`) to support transparency and reproducibility.

Also available:

* `Final_Presentation.pptx` - Project overview

---

## 10. Performance Metrics

* See `nutrition_test_performance.csv` for API performance data.
* Visualizations are available in the `visuals/` directory, including `API_flow_time.png` and `Local_flow_time.png`.

---

## 11. Troubleshooting

| Issue                 | Solution                                                                                                                               |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| Dependency errors     | Verify `pip install -r requirements.txt`; ensure Python 3.11 is active in your virtual environment.                                       |
| API authentication    | Check that keys in `config.py` match your Gemini and AstraDB account settings; review LangFlow logs for specific API errors.            |
| Slow response times   | Confirm GCP region proximity; consider batching settings and concurrent API request limits (per Section VI of the paper).               |
| Data mismatch         | Re-run preprocessing notebooks in `data_preprocessing/` to regenerate embeddings; inspect `agentic_chunker.py` parameters and logic. |

---

**Project submitted to Dr. Yanqing Zhang for Artificial Intelligence (CSc 4810)**

## 12. Contact

For support or questions, please reach out:

**Nishchay Patel**
Georgia State University, Department of Computer Science
* **Email:** [npatel237@student.gsu.edu](mailto:npatel237@student.gsu.edu)
* **Website:** [www.nishchaypatel.com](http://www.nishchaypatel.com)
