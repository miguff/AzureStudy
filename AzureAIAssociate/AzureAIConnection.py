from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = "https://......"
project_client = AIProjectClient(            
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint)