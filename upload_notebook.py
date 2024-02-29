from azure.identity import DefaultAzureCredential
from azure.synapse.notebook import NotebookClient

workspace_url = os.environ.get("SYNAPSE_WORKSPACE_URL")
client_id = os.environ.get("SYNAPSE_CLIENT_ID")
client_secret = os.environ.get("SYNAPSE_CLIENT_SECRET")
tenant_id = os.environ.get("SYNAPSE_TENANT_ID")

credential = DefaultAzureCredential(
    authority="https://login.microsoftonline.com/" + tenant_id,
    client_id=client_id,
    client_secret=client_secret,
)

notebook_path = "addition.ipynb"

with NotebookClient(workspace_url, notebook_path, credential) as notebook_client:
    notebook_client.upload()
