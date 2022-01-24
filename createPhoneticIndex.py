import os
import phoneticConfig as cfg

from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    ComplexField,
    CorsOptions,
    SearchIndex,
    ScoringProfile,
    SearchFieldDataType,
    SimpleField,
    SearchableField
)

# # export search_endpoint="https://ngenpocazcog01.search.windows.net"
# # export search_api_key="<your search api key>"
# Connection information about Cognitive Saerch
endpoint = "https://ngenpocazcog02.search.windows.net"
key = "D41E7ECB602B85461ED4B0834F9E399B"

def create_index():

    client = SearchIndexClient(endpoint, AzureKeyCredential(key))

    print("Starting Index Creation")

    name = cfg.index_name
    fields = [
        SimpleField(name="name_key", type=SearchFieldDataType.String, key=True),
        SearchableField(name="nameoriginal", type=SearchFieldDataType.String, filterable=True, analyzer_name="en.lucene"),
        SearchableField(name=cfg.indexField["name"], type=SearchFieldDataType.String, filterable=True, analyzer_name=cfg.indexField["analyzer_name"])
    ]
    cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)

    analyzers = [
        {
            "name":"doubleMetaphone",
            "@odata.type":"#Microsoft.Azure.Search.CustomAnalyzer",
            "tokenizer":"microsoft_language_tokenizer",
            "tokenFilters": [ "lowercase", "asciifolding", "doubleMetaphone" ]
        },
        {
            "name":"beiderMorse",
            "@odata.type":"#Microsoft.Azure.Search.CustomAnalyzer",
            "tokenizer":"microsoft_language_tokenizer",
            "tokenFilters": [ "lowercase", "asciifolding", "beiderMorse" ]
        },
        {
            "name":"caverphone1",
            "@odata.type":"#Microsoft.Azure.Search.CustomAnalyzer",
            "tokenizer":"microsoft_language_tokenizer",
            "tokenFilters": [ "lowercase", "asciifolding", "caverphone1" ]
        },
        {
            "name":"caverphone2",
            "@odata.type":"#Microsoft.Azure.Search.CustomAnalyzer",
            "tokenizer":"microsoft_language_tokenizer",
            "tokenFilters": [ "lowercase", "asciifolding", "caverphone2" ]
        },
        {
            "name":"cologne",
            "@odata.type":"#Microsoft.Azure.Search.CustomAnalyzer",
            "tokenizer":"microsoft_language_tokenizer",
            "tokenFilters": [ "lowercase", "asciifolding", "cologne" ]
        },
        {
            "name":"haasePhonetik",
            "@odata.type":"#Microsoft.Azure.Search.CustomAnalyzer",
            "tokenizer":"microsoft_language_tokenizer",
            "tokenFilters": [ "lowercase", "asciifolding", "haasePhonetik" ]
        },
        {
            "name":"koelnerPhonetik",
            "@odata.type":"#Microsoft.Azure.Search.CustomAnalyzer",
            "tokenizer":"microsoft_language_tokenizer",
            "tokenFilters": [ "lowercase", "asciifolding", "koelnerPhonetik" ]
        },
        {
            "name":"metaphone",
            "@odata.type":"#Microsoft.Azure.Search.CustomAnalyzer",
            "tokenizer":"microsoft_language_tokenizer",
            "tokenFilters": [ "lowercase", "asciifolding", "metaphone" ]
        },
        {
            "name":"nysiis",
            "@odata.type":"#Microsoft.Azure.Search.CustomAnalyzer",
            "tokenizer":"microsoft_language_tokenizer",
            "tokenFilters": [ "lowercase", "asciifolding", "nysiis" ]
        },
        {
            "name":"refinedSoundex",
            "@odata.type":"#Microsoft.Azure.Search.CustomAnalyzer",
            "tokenizer":"microsoft_language_tokenizer",
            "tokenFilters": [ "lowercase", "asciifolding", "refinedSoundex" ]
        },
        {
            "name":"soundex",
            "@odata.type":"#Microsoft.Azure.Search.CustomAnalyzer",
            "tokenizer":"microsoft_language_tokenizer",
            "tokenFilters": [ "lowercase", "asciifolding", "soundex" ]
        }
    ]

    tokenfilters = [
        {  
            "name":"doubleMetaphone",  
            "@odata.type":"#Microsoft.Azure.Search.PhoneticTokenFilter",  
            "encoder":"doubleMetaphone"
        },
        {  
            "name":"beiderMorse",  
            "@odata.type":"#Microsoft.Azure.Search.PhoneticTokenFilter",  
            "encoder":"beiderMorse"
        },
        {  
            "name":"caverphone1",  
            "@odata.type":"#Microsoft.Azure.Search.PhoneticTokenFilter",  
            "encoder":"caverphone1"
        },
        {  
            "name":"caverphone2",  
            "@odata.type":"#Microsoft.Azure.Search.PhoneticTokenFilter",  
            "encoder":"caverphone2"
        },
        {  
            "name":"cologne",  
            "@odata.type":"#Microsoft.Azure.Search.PhoneticTokenFilter",  
            "encoder":"cologne"
        },
        {  
            "name":"haasePhonetik",  
            "@odata.type":"#Microsoft.Azure.Search.PhoneticTokenFilter",  
            "encoder":"haasePhonetik"
        },
        {  
            "name":"koelnerPhonetik",  
            "@odata.type":"#Microsoft.Azure.Search.PhoneticTokenFilter",  
            "encoder":"koelnerPhonetik"
        },
        {  
            "name":"metaphone",  
            "@odata.type":"#Microsoft.Azure.Search.PhoneticTokenFilter",  
            "encoder":"metaphone"
        },
        {  
            "name":"nysiis",  
            "@odata.type":"#Microsoft.Azure.Search.PhoneticTokenFilter",  
            "encoder":"nysiis"
        },
        {  
            "name":"refinedSoundex",  
            "@odata.type":"#Microsoft.Azure.Search.PhoneticTokenFilter",  
            "encoder":"refinedSoundex"
        },
        {  
            "name":"soundex",  
            "@odata.type":"#Microsoft.Azure.Search.PhoneticTokenFilter",  
            "encoder":"soundex"
        }
    ]

    index = SearchIndex(
        name=name,
        fields=fields,
        cors_options=cors_options,
        token_filters=tokenfilters,
        analyzers=analyzers)

    client.delete_index(name)
    result = client.create_or_update_index(index=index)

    print("Completed index Creation")


if __name__ == '__main__':
    create_index()