Readme by Hari Thapliyal

## Steps for running running ollama local and accessing api code.
1. Install ollama
2. download all the models you want to experiment from https://ollama.com/search. for example: 
	- ollama run qwen2.5-coder
	- ollama run deepseek-coder-v2:16b
	- check what models are avilable.
	```
	ollama list
	NAME                        ID              SIZE      MODIFIED
	llama2:latest               78e26419b446    3.8 GB    45 hours ago
	mxbai-embed-large:latest    468836162de7    669 MB    45 hours ago
	deepseek-llm:7b             9aab369a853b    4.0 GB    2 days ago
	qwen2.5-coder:latest        2b0496514337    4.7 GB    2 days ago
	```
3. launch code .
4. from terminal 
	```
		python ollama-server
	```
5. To test service from terminal. Start another terminal and use this command.
	```
	curl -X POST http://localhost:5000/api/generate -H "Content-Type: application/json" -d "{\"prompt\": \"What is AI?\"}"
	```
6. To test server using python use 
	```
	python test-ollama-localapi.py
	```
	
## Steps for running locally using virtual environment.
1. create a virtual env 
2. install torch and transformers
3. activate environment
4. run from terminal or command prompt.
	```
	python ollama-via-huggingface.py
	```