from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# set `<your-endpoint>` and `<your-key>` variables with the values from the Azure portal
endpoint = "https://my-ai-doc-int-01.cognitiveservices.azure.com/"
key = "aacdfdb47d0c42e4b92ea75294b0e5fe"

docUrl = "https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence/blob/main/Labfiles/01-prebuild-models/sample-invoice/sample-invoice.pdf?raw=truehttps://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2021/02/19/ML-1955-2.jpg"

# create your `DocumentAnalysisClient` instance and `AzureKeyCredential` variable
document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, 
    credential=AzureKeyCredential(key))

poller = document_analysis_client.begin_analyze_document_from_url(
    "prebuilt-document", docUrl)

result = poller.result()