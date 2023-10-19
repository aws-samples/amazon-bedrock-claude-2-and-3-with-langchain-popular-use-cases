## Amazon BedRock and Langchain for top 10 Generative AI (GenAI) use cases

This repo is inspired by [Greg Kamradt's Github repo](https://github.com/gkamradt/langchain-tutorials/tree/main). 

Notebook `Amazon Bedrock & Langchain Sample Solutions.ipynb` containing sample solutions using Amazon BedRock & Langchain for top 10 GenAI use cases

* **Text Generation**
* **Summarization** - One of the most common use case with LLM
* **Question and Answering Over Documents** - Use information held within documents to answer questions or query
* **Extraction** - Pull structured data from a body of text or an user query
* **Evaluation** - Understand the quality of output from your application
* **Querying Tabular Data** - Pull data from databases or other tabular source
* **Code Understanding** - Reason about and digest code
* **Chatbots** - A framework to have a back and forth interaction with a user combined with memory in a chat interface
* **Interacting with APIs** - Query APIs and interact with the outside world
* **Agents** - Use LLMs to make decisions about what to do next. Enable these decisions with tools.

## Demo apps

`investmate-ai` is a simple demo that allow user to upload a PDF (e.g. public financial statement of any company) and ask question about the content.

`personal-writer` is a simple demo that allow user to create multimodal content e.g. blog post with text & images

### Getting started
Set up environment variables by run the below in your terminal, using value from your own AWS account that has BedRock access

```
    export BWB_ENDPOINT_URL=<BedRock endpoint> #for example, https://bedrock.us-east-1.amazonaws.com
    export BWB_PROFILE_NAME=<AWS CLI profile>
    export BWB_REGION_NAME=<AWS region that has BedRock access> #for example, us-east-1 or us-west-2
```

Start the Streamlit app
```
cd <demo_app_folder>
streamlit run --server.port 8080 investmate_app.py
```

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

