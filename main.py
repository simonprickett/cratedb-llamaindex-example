import openai
import os
import sqlalchemy as sa

from dotenv import load_dotenv
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.langchain import LangchainEmbedding
from llama_index.core.utilities.sql_wrapper import SQLDatabase
from langchain_openai import AzureOpenAIEmbeddings
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.core import Settings

load_dotenv()

openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.azure_endpoint = os.getenv("OPENAI_AZURE_ENDPOINT")
openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = AzureOpenAI(
    engine=os.getenv("LLM_INSTANCE"), 
    azure_endpoint=os.getenv("OPENAI_AZURE_ENDPOINT"),
    api_key = os.getenv("OPENAI_API_KEY"), # TODO rename to include Azure.
    api_version = os.getenv("OPENAI_API_VERSION"), # TODO rename to include Azure.
    model=os.getenv("LLM_NAME"), 
    temperature=0.0
)

Settings.llm = llm
Settings.embed_model = LangchainEmbedding(
    AzureOpenAIEmbeddings(
        azure_endpoint=os.getenv("OPENAI_AZURE_ENDPOINT"),
        deployment_id=os.getenv("EMBEDDING_MODEL_INSTANCE")
    )
)

print(os.getenv("CRATEDB_URL"))
print("Creating SQLAlchemy engine...")
engine_crate = sa.create_engine(os.getenv("CRATEDB_URL"))
print("Connecting to CrateDB...")
engine_crate.connect()
print("Creating SQLDatabase instance...")
sql_database = SQLDatabase(engine_crate, include_tables=[os.getenv("CRATEDB_TABLE_NAME")])
print("Creating QueryEngine...")
query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=[os.getenv("CRATEDB_TABLE_NAME")],
    llm = llm
)

print("Running query...")

query_str = "What is the average value for sensor 1?"
answer = query_engine.query(query_str)
print(answer.get_formatted_sources())
print("Query was:", query_str)
print("Answer was:", answer)
print(answer.metadata)