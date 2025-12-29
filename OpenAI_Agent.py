
import openai
import os
from typing import Dict, Any

class AgentAI:
    def __init__(self, api_key: str = None):
        """Initialize OpenAI client with API key"""
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided")
        openai.api_key = self.api_key

    def get_completion(self, prompt: str, model: str = "gpt-3.5-turbo", **kwargs) -> Dict[Any, Any]:
        """
        Get completion from OpenAI API
        Args:
            prompt: The prompt to send to the API
            model: The model to use (default: gpt-3.5-turbo)
            **kwargs: Additional parameters to pass to the API
        Returns:
            Dict containing the API response
        """
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return response
        except Exception as e:
            print(f"Error getting completion: {str(e)}")
            return {}

    def get_response_text(self, prompt: str, model: str = "gpt-3.5-turbo", **kwargs) -> str:
        """
        Get response text from OpenAI API
        Args:
            prompt: The prompt to send to the API
            model: The model to use (default: gpt-3.5-turbo)
            **kwargs: Additional parameters to pass to the API
        Returns:
            String containing the response text
        """
        response = self.get_completion(prompt, model, **kwargs)
        if response and "choices" in response:
            return response["choices"][0]["message"]["content"]
        return ""

    def chat(self, messages: list, model: str = "gpt-3.5-turbo", **kwargs) -> str:
        """Multi-turn conversation support"""
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                **kwargs
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Error in chat: {str(e)}")
            return ""