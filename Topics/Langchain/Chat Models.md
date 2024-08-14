# Chat Models:

   - **Definition:** Chat models are a type of language model that process a sequence of messages as inputs and produce chat messages as outputs. Unlike traditional LLMs that handle plain text, chat models are designed to handle multi-turn conversations, supporting distinct roles for different parts of the conversation (e.g., AI responses, user queries, and system instructions).
   - **Features:**
     - **Role Assignment:** Helps distinguish between different types of messages (AI, user, system).
     - **Compatibility:** Although chat models primarily handle message sequences, LangChain’s wrappers allow them to accept plain text inputs as well. When a string input is provided, it is converted into a `HumanMessage` before being processed by the underlying model.
   - **Integration:** LangChain does not host its own chat models but integrates with third-party providers.
   - **Standardized Parameters:**
     - `model`: Name of the model.
     - `temperature`: Sampling temperature to control output randomness.
     - `timeout`: Request timeout.
     - `max_tokens`: Maximum number of tokens to generate.
     - `stop`: Default stop sequences.
     - `max_retries`: Maximum number of retries for requests.
     - `api_key`: API key for the model provider.
     - `base_url`: Endpoint for sending requests.
   - **Notes:**
     - Standard parameters are only applicable if the model provider supports them.
     - These parameters are enforced only on integrations with dedicated packages (e.g., `langchain-openai`, `langchain-anthropic`) and not on models within `langchain-community`.
     - ChatModels may accept additional, model-specific parameters.

   - **Tool Calling:** Some chat models are fine-tuned for tool calling, making them better suited for such tasks compared to non-fine-tuned models. These are recommended for use cases involving tool interaction.

## Multimodality:
   - **Definition:** Multimodal chat models are capable of handling various types of inputs such as images, audio, and video. Although these models are still emerging and not yet standardized, they represent the frontier of LLM capabilities.
   - **LangChain's Approach:**
     - **Lightweight Abstractions:** Given the evolving nature of multimodal models, LangChain’s abstractions are designed to be flexible, with plans to refine them as the field develops.
     - **Input Formats:** Most chat models supporting multimodal inputs use formats similar to OpenAI’s content blocks, particularly for image inputs. Models like Gemini, which handle video and other byte inputs, support native, model-specific formats.
   - **Current Landscape:** Multimodal outputs are less common, and APIs are still evolving to accommodate these features.

### Using Chat and Multimodal Models:
   - For detailed guidance on using chat and multimodal models, developers should refer to the specific how-to guides provided by LangChain. A full list of model providers with multimodal capabilities is also available for reference. 

   Link: https://python.langchain.com/v0.2/docs/how_to/#multimodal
         https://python.langchain.com/v0.2/docs/integrations/chat/#advanced-features

This summary encapsulates the essential components and considerations when working with chat and multimodal models in LangChain, offering insight into how to leverage these tools in your applications.