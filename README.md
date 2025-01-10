# Athlyze
A practical and scientific approach towards your physique.

A Gentic Rag for all you gym bros




---

## System Architecture

### User Interface
* Authentication Service (User Login/Signup)
 * Profile Management
   * Notes
   * Goals  
   * Limitations
   * Nutrition Info
 * Calendar System
   * Planner
   * Tracker

### Preprocessing Layer 
* Text Normalization
* Tokenization
* Contextual Feature Extraction

### Multi-Agent System
* Agent 1: Query Understanding Agent
 * Intent Classification
 * Goal Mapping
* Agent 2: Personalized Retrieval Agent
 * Profile Data Integration
 * Historical Notes Analysis  
* Agent 3: Research Paper Summarization Agent
 * Search Research Database
 * Summarize Findings
* Agent 4: Planning and Tracking Agent
 * Analyze Goals
 * Generate Calendar Events  
 * Update Tracker

### Retriever Module
* Vector Store (Pinecone/FAISS)
 * Embedding Generation (using Google Gemini)

### Knowledge Base
* Research Papers (Exercise, Nutrition, Fitness)
* User Data (Profiles, Notes, Goals, Calendar)
* AI Models (Google Generative AI Gemini)

### Generation Module
* Text Generation (Response Construction using LangFlow)
 * Google Generative AI Gemini
 * Hugging Face Transformers

### Postprocessing Layer
* Summarization 
* Formatting
* Content Personalization

### Output Module
* Text Responses (Insights, Recommendations)
* Calendar Updates (New Events, Notifications)
* Personalized Notes (Goal Progress, New Findings)

---
