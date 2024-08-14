# Runnable Interface

The `Runnable` interface is like a set of rules or guidelines that makes it easy to build and connect different pieces of a larger system. Imagine you're building a complex machine out of different parts, like a car engine. Each part has to fit with the others in a certain way for the engine to work. The `Runnable` interface is like a set of standards that ensures all the parts can work together smoothly.

### What Does the Runnable Interface Do?

1. **Standard Functions**: The `Runnable` interface provides standard ways to use different parts of the system. These include:
   - **invoke**: This is like turning the key to start the engine. You give it some input (like turning the key), and it does its job.
   - **batch**: Imagine you want to start several engines at once. This function lets you handle multiple inputs at the same time.
   - **stream**: Instead of getting the result all at once, this function lets you get the result piece by piece, like watching a movie one scene at a time.

2. **Async Versions**: There are also "async" versions of these functions, which are like having a helper who can do things in the background while you focus on something else.

3. **Flexible Parts**: Different components (or parts of the system) can have different types of inputs and outputs. For example:
   - **Prompt**: Think of this as the question you ask the system. You give it some information, and it turns that into a format the system can understand.
   - **ChatModel**: This is like a chatbot. You ask it a question, and it responds with an answer.
   - **LLM (Large Language Model)**: This is a powerful tool that can generate text based on what you ask it.
   - **Retriever**: This part searches for information, like a librarian finding books based on your request.

4. **Schemas**: Each component also has a blueprint that shows what kind of input it needs and what kind of output it will give. This makes it easier to understand how to use each part and connect it to others.

In short, the `Runnable` interface makes it easy to connect different parts of a system, ensuring they work together smoothly and efficiently.