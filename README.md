# Athlyze User Manual

Welcome to **Athlyze** – a personalized fitness and nutrition platform I developed, combining advanced AI and NLP techniques to deliver tailored recommendations. This guide will help you understand, install, and operate the system.

## Table of Contents

1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Installation and Setup](#installation-and-setup)
4. [Usage Instructions](#usage-instructions)
5. [Research Documentation](#research-documentation)
6. [Project Timeline and Future Directions](#project-timeline-and-future-directions)
7. [Troubleshooting](#troubleshooting)
8. [Contact](#contact)

## Project Overview

I built Athlyze to enhance existing fitness applications by leveraging cutting-edge AI tools and NLP techniques. The platform uses data-driven methodologies and a multi-agent system to:
- Analyze comprehensive user data including demographics, dietary habits, and exercise routines.
- Retrieve and integrate critical research insights using vector databases.
- Provide personalized recommendations through adaptive machine learning models.

Key components include:
- **APIs:** Located in the [api_flows_slow_method](api_flows_slow_method/) directory (e.g., `nutrition_flow_api.py` and `training_flow_api.py`).
- **Application:** The main app resides in [app](app/), featuring modules for data management, locally stored AI flows (acting as faster alternatives to API flows), pages, and public assets.
- **Data Preprocessing:** Found in [data_preprocessing](data_preprocessing/), this includes scripts like `agentic_chunker.py` and several notebooks for data cleaning and embedding generation.
- **Research Papers:** The directories [nutrition_research_papers](nutrition_research_papers/) and [resistant_research_papers](resistant_research_papers/) house the literature that informs the recommendation methodologies.
- **Visuals and Testing:** Additional assets and tests are available in visuals/ and testing/.

## System Architecture

The system is structured in layered modules:

- **User Interface:** Located in app/Home.py, this module supports authentication, profile management, and calendar integration.
- **Preprocessing Layer:** Handles text normalization, tokenization, and feature extraction.
- **Multi-Agent System:** 
  - **Query Understanding Agent:** Classifies intents and maps user goals.
  - **Personalized Retrieval Agent:** Combines user profile data and historical notes for context-aware recommendations.
  - **Research Paper Summarization Agent:** Searches and summarizes relevant research.
  - **Planning and Tracking Agent:** Analyzes goals and manages calendar events.
- **Generation and Output Modules:** Uses text generation (leveraging LangFlow and Google Gemini) to construct responses and updates.

For more technical details, please review the code in each respective directory.

## Installation and Setup

1. **Prerequisites:**  
   - Python 3.x  
   - AI tools and NLP libraries required as listed in requirements.txt
   - A virtual environment (recommended)
   - Langflow and AstraDB setup

2. **Installation Steps:**  
   - Clone the repository.
   - Install the required dependencies:
     ```sh
     pip install -r requirements.txt
     ```
   - Configure any necessary environment variables in the .env file:
     ```sh
      ASTRA_DB_APPLICATION_TOKEN = ''
      GEMINI_API_KEY = ''
      ATSRA_USER_ID = ''
      ASTRA_DB_API_ENDPOINT = ''
     ```
   - Establish Langflow and AstraDB as mentioned in the paper.
     

3. **Configuration:**  
   - Verify service configurations for AstraDB, Google Cloud Platform, and other integrations.
   - Check the inline code documentation for module-specific configurations.

## Usage Instructions

- **Starting the Application:**  
  Launch the platform by running the main application script (for example, the home module in app/Home.py).

- **API Endpoints:**  
  Use the endpoints available in the api_flows_slow_method directory, or use downloaded local_flows for faster execution.

- **Data Preprocessing:**  
  Open the notebooks in the data_preprocessing folder to execute tasks like data cleaning, chunking, and embedding generation, these needs to be uploaded to AstraDB.

## Research Documentation

For a comprehensive look at the research and methodologies behind Athlyze, refer to:
- Final_Paper.pdf – a full research document detailing the platform.
- Additional details on system design, vector database schema, and model explanations are available within the research papers in nutrition_research_papers and resistant_research_papers.

## Project Timeline and Future Directions

### Project Timeline
- **Weeks 2-4:** I conducted initial research and designed the APIs using LangFlow.
- **Weeks 5-7:** I handled data collection, developed ML models, and integrated the database.
- **Weeks 8-13:** I focused on system integration, testing, optimization, and submission.

## Troubleshooting

- **Installation Issues:**  
  Ensure all dependencies are installed, the Python version is correct, and environment variables are properly set.
- **API Errors:**  
  Check the logs in the VS Code output pane for any issues with endpoints.
- **Data Mismatches:**  
  Verify the preprocessing steps in data_preprocessing to ensure data integrity.

For further support, refer to the inline documentation in each module or contact me using the details below.

## Contact

**Developer:** Nishchay Patel  
**Institution:** Georgia State University  
**Email:** npatel237@student.gsu.edu
