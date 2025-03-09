import streamlit as st
import json
import requests
from dotenv import load_dotenv
import os
from cryptography.fernet import Fernet

_SYSTEM_MESSAGE = (
    "You Are User Experience Virtual Assistant Agent Over Digital Marketing Platform .Your task is to guide and answer all users questions in order to improve UX, It has to be clear and concise. \n"
    "I Will provide you with some keywords my search related to .\n"
    "Provide any kind of resources help ,suggestions and more navigation facilities over the platform"
)

class Encryption:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(self.key)

    def encrypt_env(self, input_file=".env.development", output_file=".env.development.enc"):
        """Encrypts the .env file."""
        try:
            with open(input_file, 'rb') as file:
                original = file.read()
            encrypted = self.fernet.encrypt(original)

            with open(output_file, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            st.success(f"Encrypted {input_file} to {output_file}")
        except FileNotFoundError:
            st.error(f"File {input_file} not found.")
        except Exception as e:
            st.error(f"Encryption failed: {e}")

    def decrypt_env(self, input_file=".env.development.enc", output_file=".env.development"):
        """Decrypts the .env.enc file."""
        try:
            with open(input_file, 'rb') as file:
                encrypted = file.read()
            decrypted = self.fernet.decrypt(encrypted)

            with open(output_file, 'wb') as decrypted_file:
                decrypted_file.write(decrypted)
            st.success(f"Decrypted {input_file} to {output_file}")
        except FileNotFoundError:
            st.error(f"File {input_file} not found.")
        except Exception as e:
            st.error(f"Decryption failed: {e}")

class LLMClient:
    def __init__(self):
        self.ai_config = self.load_ai_config()
        if self.ai_config:
            self.ai_platform = self.ai_config.get('ai_platform')
            if self.ai_platform == 'mendable':
                mendable_config = self.ai_config.get('mendable')
                if mendable_config:
                    self.workspace_id = mendable_config.get('workspace_id')
                    self.data_source_id = mendable_config.get('data_source_id')
                    self.model = mendable_config.get('model')

                    # Decrypt the .env file and load environment variables
                    encryption_key = os.environ.get("ENCRYPTION_KEY") # Get encryption key from environment.
                    if encryption_key:
                        encryption_client = Encryption(encryption_key.encode())
                        encryption_client.decrypt_env() # decrypt .env.development.enc to .env.development
                        load_dotenv() # Load the decrypted env variables
                        self.api_key = os.environ.get("MENDABLE_API_KEY") # Get API key from env.
                    else:
                        st.error("Encryption key not found in environment variables.")
                        self.api_key = None
                else:
                    st.error("Mendable configuration missing.")
                    self.api_key = None
            elif self.ai_platform == 'other':
                other_config = self.ai_config.get('other_ai')
                if other_config:
                    self.other_api_key = other_config.get('other_api_key')
                    self.other_model = other_config.get('other_model')
                else:
                    st.error("Other AI configuration missing.")
                    self.other_api_key = None
            else:
                st.error("Invalid ai_platform.")
                self.api_key = None
        else:
            self.api_key = None

    def load_ai_config(self):
        """Loads AI configuration from assets/data.json."""
        try:
            with open('assets/data.json', 'r') as f:
                config = json.load(f)
            return config
        except FileNotFoundError:
            st.error("assets/data.json not found.")
            return None
        except json.JSONDecodeError:
            st.error("Invalid JSON format in assets/data.json.")
            return None

    def query_mendable(self, query):
        """Queries the Mendable AI API."""
        if not self.api_key:
            st.error("Mendable API key not configured.")
            return None

        url = "https://api.mendable.ai/v1/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "workspace_id": self.workspace_id,
            "data_source_id": self.data_source_id,
            "messages": [{"role": "user", "content": query}, {"role": "system", "content": _SYSTEM_MESSAGE}],
            "model": self.model,
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            answer = result.get('choices', [{}])[0].get('message', {}).get('content')
            return answer
        except requests.exceptions.RequestException as e:
            st.error(f"Mendable API request failed: {e}")
            return None
        except (KeyError, IndexError) as e:
            st.error(f"Error parsing Mendable API response: {e}")
            return None

    def query_other(self, query):
        """Queries the 'other' AI API."""
        if not self.other_api_key:
            st.error("Other AI API key not configured.")
            return None
        url = "YOUR_OTHER_AI_API_ENDPOINT"
        headers = {
            "Authorization": f"Bearer {self.other_api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "prompt": query,
            "model": self.other_model
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            answer = result.get("choices", [{}])[0].get("text")
            return answer
        except requests.exceptions.RequestException as e:
            st.error(f"Other AI API request failed: {e}")
            return None
        except (KeyError, IndexError) as e:
            st.error(f"Error parsing Other AI API response: {e}")
            return None

    def query(self, query):
        """Queries the configured AI platform."""
        if self.ai_platform == 'mendable':
            return self.query_mendable(query)
        elif self.ai_platform == 'other':
            return self.query_other(query)
        else:
            st.error('Invalid ai platform.')
            return None