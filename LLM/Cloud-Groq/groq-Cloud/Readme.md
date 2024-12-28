# About this Work

## Intro to GroqCloud 
- GroqCloud is one of the fastest cloud for LLM models.
- What are the differnt LLM it supports?
- How to use this?

## Groq with Langchain
- How to use langchain_groq to create LLM instance, using ChatGroq
```
llm = ChatGroq(groq_api_key= groq_api_key, model_name = "llama3-70b-8192")
```
- Use Groq for single question and answer.
- Use Groq for chatting
- Displaying output in Markdown format.

## Introduction ChromaDB
- ChromaDB is a Vector Database
- How to creat in memory and persistant Vector database?
- How to create multiple datasets?
- How to query a dataset or collection?

## Generating Cold Mails 
- Using GroqCloud LLM generating emails.
- We have our work portfolio in a dataset, that mentions skills and portfolio link.
- Using WebBasedLoader to read contents form webpages. langchain_community.document_loaders import WebBaseLoader
```
loader = WebBaseLoader("https://your-url-to-read-page")
```
- Creating prompttemplate using langchain_core.prompts import PromptTemplate
```
prompt_extract = PromptTemplate.from_template(
    """
    ### Scraped Text from Website:
    {page_data}
    ### Instruction:
    The scrapped text is from the career's page of a website.
    Your job is to extract the job postings and return them in JSON format containting following keys: Role, Experience, Skills, and Description.
    Only return the valid JSON.
    ### Vadlid JSON (No Preamble):
    """
)
```
- creating langchain: 
```
chain_extract = prompt_extract | llm
resp = chain_extract.invoke(input = {'page_data':page_data})
```
- Converting output into json format.
```
json_parser = JsonOutputParser()
json_resp = json_parser.parse(resp.content)
```
- Creating vector database based on the your portfolio skills 
- Searching vector database for the portolio links, based on the skills need in job posting 
- Create a prompt for email 
- Create langchain 
- Invoke langchain 

