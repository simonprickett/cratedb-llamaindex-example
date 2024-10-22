# TODO

Status:

Gives a 404 when run, probably an Azure endpoint config issue?

```
...
  File "/Users/simon/source/projects/llamatutorial/venv/lib/python3.12/site-packages/openai/_base_client.py", line 1058, in _request
    raise self._make_status_error_from_response(err.response) from None
openai.NotFoundError: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}
```

This has been tested using Python 3.12.2 on macOS Sequoia 15.0.1.

Create and activate a virtual environment:

```
python -m venv venv
. venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Individual dependencies (using this as a scratchpad, will slim it down to the minimum requirements when it is working):

```bash
pip install python-dotenv
pip install openai
pip install sqlalchemy-crate
pip install llama-index
pip install langchain
pip install langchain-community
pip install langchain-openai
pip install llama-index-embeddings-langchain
pip install llama-index-llms-azure-openai
```

Example `.env` file:

```
TODO
```

Run the code:

```bash
python main.py
```

Expected output:

```bash
TODO
```