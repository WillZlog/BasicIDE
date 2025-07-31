#!/usr/bin/env python3
"""
AI Fixer Component
Uses OpenAI's GPT-4o API to fix code errors and provide suggestions
"""

import os
import json
import requests
from typing import Optional

class AIFixer:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.api_url = "https://api.openai.com/v1/chat/completions"
        self.model = "gpt-4o"
        
    def fix_code(self, code: str, language: str, error_output: str = "") -> Optional[str]:
        """
        Send code and error to OpenAI API for fixing
        
        Args:
            code: The code to fix
            language: Programming language
            error_output: Error output from running the code
            
        Returns:
            Fixed code or None if failed
        """
        if not self.api_key:
            return None
            
        try:
            # Prepare the prompt
            prompt = self._create_prompt(code, language, error_output)
            
            # Make API request
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": self.model,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful programming assistant. Fix the code provided and return ONLY the corrected code without any explanations or markdown formatting."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 2000,
                "temperature": 0.1
            }
            
            response = requests.post(self.api_url, headers=headers, json=data, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                fixed_code = result['choices'][0]['message']['content'].strip()
                
                # Remove markdown code blocks if present
                if fixed_code.startswith('```'):
                    lines = fixed_code.split('\n')
                    if len(lines) > 2:
                        fixed_code = '\n'.join(lines[1:-1])
                
                return fixed_code
            else:
                print(f"API Error: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"Error calling OpenAI API: {str(e)}")
            return None
            
    def _create_prompt(self, code: str, language: str, error_output: str) -> str:
        """Create a prompt for the AI to fix the code"""
        
        language_names = {
            'python': 'Python',
            'javascript': 'JavaScript',
            'csharp': 'C#',
            'html': 'HTML',
            'css': 'CSS',
            'json': 'JSON'
        }
        
        lang_name = language_names.get(language, language)
        
        prompt = f"""Please fix the following {lang_name} code. 

Code:
{code}

"""
        
        if error_output:
            prompt += f"""Error output:
{error_output}

"""
        
        prompt += f"""Please provide the corrected {lang_name} code that fixes any syntax errors, runtime errors, or logical issues. Return only the corrected code without any explanations or markdown formatting."""
        
        return prompt
        
    def set_api_key(self, api_key: str):
        """Set the OpenAI API key"""
        self.api_key = api_key
        
    def get_api_key_status(self) -> bool:
        """Check if API key is available"""
        return bool(self.api_key)
        
    def test_connection(self) -> bool:
        """Test the API connection"""
        if not self.api_key:
            return False
            
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": "Hello"
                    }
                ],
                "max_tokens": 10
            }
            
            response = requests.post(self.api_url, headers=headers, json=data, timeout=10)
            return response.status_code == 200
            
        except:
            return False 