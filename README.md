# Athlyze
A practical and scientific approach towards your physique.
Agentic RAG for the Personalized Fitness and Nutrition

## Project Overview
Existing fitness applications rely on limited algorithms and static models, neglecting advanced machine learning and NLP techniques. Athlyze proposes a novel methodology to address these gaps by leveraging cutting-edge technology for personalized fitness and nutrition recommendations.

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

### Methodology
Athlyze employs a three-step research methodology:
1. Gather comprehensive user data
   - Demographics
   - Dietary habits
   - Limitations
   - Exercise routines
   - Goals
2. Integrate data with vector database of research paper embeddings
   - Use NLP-based semantic search
   - Generate evidence-backed insights
3. Utilize machine learning models
   - Regression analysis for caloric predictions
   - Clustering algorithms for user segmentation
   - Adaptive recommendation systems

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

## Technology Stack
* Google Cloud Platform (GCP)
* GEMINI AI: google-2.0-flashthinking
* Langflow
* AstraDB
* TensorFlow
* PyTorch
* Streamlit

## Project Timeline
* Week 2 [January 21 – January 27]: Study Agentic RAG methods
* Week 3 [January 28 – February 3]: Design vector database schema
* Week 4 [February 4 – February 10]: Implement APIs using Langflow
* Week 5 [February 11 – February 17]: Collect user data
* Week 6 [February 18 – February 24]: Build ML recommendation model
* Week 7 [February 25 – March 2]: Development buffer
* Week 8 [March 3 – March 9]: System integration and initial testing
* Week 9 [March 10 – March 16]: Refine database retrieval
* Week 10 [March 17 – March 23]: Expand research database
* Week 11 [March 24 – March 30]: Platform optimization
* Week 12 [April 1 – April 14]: Project documentation
* Week 13 [April 15 – April 28]: Final submission preparation

## Future Research Directions
* Refine retrieval methods
* Optimize recommendation models
* Expand research database
* Conduct iterative user testing

## References
1. Bochicchio et al., "Comprehensiveness of AI Exercise Recommendations," JMIR Form. Res., 2024
2. Arens-Volland et al., "Personalized Nutrition," Eur. J. Nutr., 2023
3. Pereira et al., "Nutritional Genomics," Nutrients, 2023
4. Mao et al., "Nutrition and Fitness Recommendations," Nutrients, 2023

## Contact
**Author**: Nishchay Patel
**Institution**: Georgia State University
**Email**: npatel237@student.gsu.edu
