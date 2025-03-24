from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os
import uuid
from typing import List, Dict, Union, Optional
from dotenv import load_dotenv
from rich import print

load_dotenv()

class AgenticChunker:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the AgenticChunker with configuration."""
        self.chunks: Dict[str, Dict] = {}
        self.id_truncate_limit = 5
        self.generate_new_metadata_ind = True
        self.print_logging = True

        # Get API key from parameter or environment
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("Google API key is required")

        # Initialize the model
        self.llm = GoogleGenerativeAI(
            model="gemini-1.0-pro",
            google_api_key=self.api_key,
            temperature=0.1
        )

    def add_propositions(self, propositions: List[str]) -> None:
        """Add multiple propositions to chunks."""
        for proposition in propositions:
            if proposition and isinstance(proposition, str):
                self.add_proposition(proposition.strip())

    def add_proposition(self, proposition: str) -> None:
        """Add a single proposition to an existing or new chunk."""
        if not proposition:
            return

        if self.print_logging:
            print(f"\nAdding: '{proposition}'")

        if not self.chunks:
            self._create_new_chunk(proposition)
            return

        chunk_id = self._find_relevant_chunk(proposition)
        if chunk_id:
            self.add_proposition_to_chunk(chunk_id, proposition)
        else:
            self._create_new_chunk(proposition)

    def _create_new_chunk(self, proposition: str) -> None:
        """Create a new chunk with the given proposition."""
        try:
            new_chunk_id = str(uuid.uuid4())[:self.id_truncate_limit]
            new_chunk_summary = self._get_new_chunk_summary(proposition)
            new_chunk_title = self._get_new_chunk_title(new_chunk_summary)

            self.chunks[new_chunk_id] = {
                'chunk_id': new_chunk_id,
                'propositions': [proposition],
                'title': new_chunk_title,
                'summary': new_chunk_summary,
                'chunk_index': len(self.chunks),
                'metadata': self._generate_metadata(proposition)
            }

            if self.print_logging:
                print(f"Created new chunk ({new_chunk_id}): {new_chunk_title}")

        except Exception as e:
            print(f"Error creating new chunk: {e}")
            raise

    def _get_new_chunk_summary(self, proposition: str) -> str:
        """Generate a summary for a new chunk."""
        try:
            prompt = ChatPromptTemplate.from_messages([
                ("system", "Generate a concise summary of the following scientific proposition, "
                          "focusing on key findings and implications."),
                ("user", f"Proposition: {proposition}")
            ])
            
            response = self.llm.invoke(prompt.format_prompt().to_messages())
            return response.content if response.content else "No summary generated"
            
        except Exception as e:
            print(f"Error generating summary: {e}")
            return "Summary generation failed"

    def _get_new_chunk_title(self, summary: str) -> str:
        """Generate a title for a chunk based on its summary."""
        try:
            prompt = ChatPromptTemplate.from_messages([
                ("system", "Generate a brief, descriptive title (5-7 words) for this research summary."),
                ("user", f"Summary: {summary}")
            ])
            
            response = self.llm.invoke(prompt.format_prompt().to_messages())
            return response.content if response.content else "Untitled Chunk"
            
        except Exception as e:
            print(f"Error generating title: {e}")
            return "Untitled Chunk"

    def _generate_metadata(self, proposition: str) -> Dict:
        """Generate metadata for a chunk based on its content."""
        return {
            'source': 'research_paper',
            'content_type': 'scientific_finding',
            'creation_time': str(uuid.uuid1()),
        }

    def _find_relevant_chunk(self, proposition: str) -> Optional[str]:
        """Find the most relevant existing chunk for a proposition."""
        try:
            if not self.chunks:
                return None

            # Compare proposition with existing chunks
            for chunk_id, chunk in self.chunks.items():
                existing_props = ' '.join(chunk['propositions'])
                
                # Create a prompt to check relevance
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "Determine if these statements are closely related (yes/no)."),
                    ("user", f"Statement 1: {existing_props}\nStatement 2: {proposition}")
                ])
                
                response = self.llm.invoke(prompt.format_prompt().to_messages())
                
                if response.content and 'yes' in response.content.lower():
                    return chunk_id
                    
            return None
            
        except Exception as e:
            print(f"Error finding relevant chunk: {e}")
            return None

    def get_chunks(self, get_type: str = 'dict') -> Union[Dict, List[str]]:
        """Get chunks in the specified format."""
        if get_type == 'dict':
            return self.chunks
        elif get_type == 'list_of_strings':
            return [" ".join(chunk['propositions']) for chunk in self.chunks.values()]
        else:
            raise ValueError("Invalid get_type. Use 'dict' or 'list_of_strings'")

    def save_chunks_to_file(self, file_path: str) -> None:
        """Save chunks to a file with error handling."""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                for chunk_id, chunk in self.chunks.items():
                    file.write(f"Chunk ID: {chunk_id}\n")
                    file.write(f"Title: {chunk['title']}\n")
                    file.write(f"Summary: {chunk['summary']}\n")
                    file.write("Propositions:\n")
                    for prop in chunk['propositions']:
                        file.write(f"- {prop}\n")
                    file.write(f"Metadata: {chunk['metadata']}\n")
                    file.write("\n---\n\n")
                    
        except Exception as e:
            print(f"Error saving chunks to file: {e}")
            raise