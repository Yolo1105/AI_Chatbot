# AI Chatbot Integration with Rasa and GPT-2 for NYU HPC

This README outlines the development and operation of an AI chatbot that integrates Rasa's robust dialogue management with GPT-2's advanced text generation capabilities. The chatbot is specifically designed for interacting with the NYU High Performance Computing (HPC) system, providing an engaging and efficient user experience.

## Overview

The AI chatbot leverages Rasa for its ability to handle intent recognition, entity extraction, and dialogue management, alongside GPT-2, which enhances the chatbot’s capacity for generating dynamic, context-aware responses. This setup aims to deliver a high level of interaction quality and user satisfaction by blending predefined interaction patterns with the ability to generate spontaneous, human-like responses.

## Components

### Rasa

**Features:**
- **Intent Recognition**: Determines user intentions through natural language processing.
- **Entity Extraction**: Identifies key information within the user’s input.
- **Dialogue Management**: Controls the conversation flow based on user input and defined dialogue paths.

**Benefits:**
- **Customizable**: Can be tailored to specific needs, making it ideal for specialized domains like HPC.
- **Scalable**: Handles increasing complexity without degrading user interaction quality.
- **Context-Aware**: Maintains conversational context over multiple interactions, ensuring coherent dialogue progression.

### GPT-2 (Transformers)

**Features:**
- **Text Generation**: Capable of generating text that is contextually relevant to the user's current interaction.
- **Flexibility**: Trained on a diverse corpus, allowing for a wide range of discussion topics.

**Benefits:**
- **Human-Like Interaction**: Enhances user engagement with responses that mimic human conversational patterns.
- **Dynamic Responses**: Generates responses on-the-fly, ideal for queries that fall outside static scripts.

## Integration Strategy

### Initial Processing by Rasa
Rasa begins the interaction by processing user inputs to ascertain intents and extract entities, forming a basis for response strategies.

### Advanced Response Generation with GPT-2
For more complex queries, especially those requiring in-depth knowledge of the NYU HPC system, GPT-2 steps in to generate nuanced responses.

### Hybrid Interaction Model
Utilizes structured dialogue management via Rasa for routine interactions and employs GPT-2 for creative and complex response generation.

## Rasa Framework Training Guide

This guide provides a detailed walkthrough for setting up, training, and deploying a Rasa-based chatbot. It explains the architecture of Rasa, the role of each configuration file, the process of preparing your data, and how to interact with your chatbot for refining and testing.

### How Rasa Works

Rasa operates using two main components to create a sophisticated chatbot:

1. **Natural Language Understanding (NLU)**:
   - **Purpose**: The NLU component is responsible for interpreting user input. It analyzes text to determine the user's intent and extract relevant entities.
   - **Training Data**: The NLU model is trained using examples provided in the `data/nlu.yml` file, where each intent is accompanied by various user utterances that exemplify that intent.

2. **Dialogue Management**:
   - **Purpose**: This component manages the flow of the conversation. It decides the next action the bot should take based on the current state of the conversation and the history of the interaction.
   - **Training Data**: The dialogue management component is trained using data from the `data/stories.yml` file (which provides example conversation paths) and the `data/rules.yml` file (which specifies strict behaviors for certain situations).

### Model Training and Output

- **Process**: Training combines NLU and dialogue management models using data from `nlu.yml`, `stories.yml`, `rules.yml`, and `domain.yml`.
- **Output Files**: The trained models are saved in the `models` directory. Each file is named with a timestamp and a unique name, making it easy to organize and identify different versions of trained models.

## Configuration Files Overview

### Essential Training Data Files

The essential files required for training your Rasa chatbot are located in the `data` folder:

- `data/nlu.yml`: Contains examples of user utterances mapped to intents for training the NLU component.
- `data/rules.yml`: Specifies strict behavior rules that dictate how the bot should respond in certain scenarios.
- `data/stories.yml`: Provides example conversational flows that the dialogue management model uses for training.

### Configuration and Domain Definition

- **`config.yml`**: This file defines the processing pipeline and policies that dictate how Rasa will process user input and manage conversations.
- **`domain.yml`**: This file lists the capabilities of your chatbot, including intents, entities, responses, slots, and actions.

## Detailed Training Process

### File Structure

Ensure your project directory is organized with the necessary files in their respective folders:

- `data/`: Includes `nlu.yml`, `rules.yml`, and `stories.yml`.
- `models/`: Stores the trained models.

### Steps for Model Training

1. **Prepare Data**: Format your data in YAML files within the `data` directory.
2. **Run Training Command**:

   ```bash
   rasa train
   ```

   This command compiles the data and trains both the NLU and dialogue management models.

### Model Training with `rasa train`

- **Command**: `rasa train`
- **Purpose**: This command initiates the training of both the NLU and dialogue management components.
- **How it Works**:
  1. **Data Compilation**: Rasa first compiles all the training data from your `nlu.yml`, `stories.yml`, and `rules.yml`.
  2. **Model Building**: It then uses this data to train the NLU model to recognize intents and entities and the dialogue management model to manage conversation flows.
  3. **Output**: The trained models are saved in the `models` directory. The filenames include a timestamp and a generated name, which helps in identifying and organizing different versions of trained models.

- **Main Goal**: The primary goal of `rasa train` is to create a coherent model that understands user inputs and can effectively manage a dialogue based on the training scenarios provided.
- **Outputs**: The output is a model (or set of models) that encapsulates the ability to parse and understand language as well as to make decisions about how to respond in various conversational contexts.

## Testing and Interaction Modes

### Interactive Testing with `rasa interactive`

- **Command**: `rasa interactive`
- **Purpose**: This mode is designed for more granular testing and improvement of your chatbot. It allows you to:
  - **Interactively Test**: Step through a conversation with the bot, seeing how it interprets and responds to inputs in real time.
  - **Correct Errors**: During the interactive session, you can correct the intents and entities recognized by the bot as well as modify the chosen dialogue actions.
  - **Refine Training Data**: Corrections and modifications made during interactive sessions can be saved directly back to the training data, helping to refine and improve the model’s accuracy and responsiveness.

- **Benefits of `rasa interactive`**:
  - **Detailed Debugging**: It provides a detailed view into how the bot is interpreting and responding to inputs, which is crucial for debugging and understanding specific failure points.
  - **Immediate Feedback**: Corrections and improvements are immediately reflected in the session, allowing for rapid iterative development.

### Example Workflow in Interactive Mode

1. **User Input Processing**: The user provides an input (e.g., "yes"), which the model classifies into an intent (e.g., `affirm`) with a certain confidence level.

2. **Dialogue Management**: The bot determines the appropriate action based on the identified intent and the current state of the conversation. This could be responding with a text message, querying a database, or any other predefined action.

3. **Action Proposal**: Before executing the determined action, Rasa interactive mode pauses to ask the developer if the proposed action (or intent recognition) is correct. This is especially useful in cases where the bot proposes to run a special action like `action_unlikely_intent`.

4. **Feedback Loop**: The developer can confirm (`Yes`) or deny (`No`) the bot's decision. This feedback is crucial for training:
   - **Yes**: Confirms the model's decision was correct, reinforcing this path.
   - **No**: Indicates an error, prompting the developer to correct the intent, provide the correct response, or adjust the dialogue flow.

### Dealing with `action_unlikely_intent`

- **Purpose**: This action is triggered when the bot detects that the predicted intent does not align well with the context of the conversation, based on past training data. It's part of the `UnexpecTEDIntentPolicy`, which aims to identify and handle unexpected or out-of-context user intents.
- **Developer's Role**: You need to assess whether the triggering of `action_unlikely_intent` is justified. If it is (i.e., the user's response was indeed unexpected), confirm it. If not, deny it and provide the correct intent or action, helping the model learn the correct behavior in similar situations.

## Using Feedback Correctly in Interactive Mode

When prompted to validate an action like `action_unlikely_intent`:

- **Assess Context**: Understand the dialogue context to decide whether the bot's response was appropriate.
- **Provide Accurate Feedback**: Your corrections teach the model about correct and incorrect behaviors, crucial for its learning and adaptability.

## Implementing and Testing Custom Actions

### Overview of Custom Actions

In Rasa, custom actions allow you to define specific behaviors or functions that go beyond the basic capabilities provided out of the box. These custom actions can perform various tasks, such as running Python code to interact with external systems (APIs, databases, etc.), performing complex calculations, or dynamically generating responses based on the conversation context.

### Example Custom Action: `ActionHelloWorld`

In the `actions.py` file, a simple custom action is defined, named `ActionHelloWorld`. Here’s a breakdown of its components and functionality:

1. **Class Definition**:
   - The class `ActionHelloWorld` inherits from `Action`, a base class provided by Rasa that allows defining custom actions.

2. **Method `name()`**:
   - This method returns the name of the action, `"action_hello_world"`. This name is used in the Rasa domain file to refer to this specific action.

3. **Method `run()`**:
   - The `run()` method is where the action's logic is implemented. Whenever this action is triggered during a conversation, the code inside this method is executed.
   - **Parameters**:
     - `dispatcher`: Used to send messages back to the user. It can send text, images, buttons, and other elements.
     - `tracker`: Tracks the state of the conversation. It provides access to the conversation history, the current state, slot values, the latest message, and more.
     - `domain`: Contains the domain configuration, which includes intents, entities, slots, responses, and more actions.
   - **Example**: In this example, the `dispatcher.utter_message(text="Hello World!")` line sends a message "Hello World!" back to the user.

### How Custom Actions Relate to the Interactive Session

In an interactive session, when a custom action like `action_hello_world` is proposed by the dialogue management model:

1. **Action Proposal**:
   - Based on the conversation history and current state, Rasa might decide to execute `action_hello_world`.

2. **User Confirmation**:
   - In interactive mode, you will see a prompt asking if executing `action_hello_world` is the correct decision at this point in the conversation. Your response (`Yes` or `

No`) helps train the model on whether this action is appropriate in the current context.

3. **Execution and Feedback**:
   - If confirmed, the action is executed, and any output (like "Hello World!") is shown in the interactive session. This helps you see the immediate effect of the action and provides a chance to further correct and refine the model’s understanding and response strategies.

### Steps to Implement Custom Actions

1. **Define the Action**:
   - Write the Python code for the action in the `actions.py` file.

2. **Update the Domain File**:
   - Add the action name (`action_hello_world`) to the domain file under the `actions` section.

3. **Enable the Action Server**:
   - You'll need to run the action server alongside your Rasa server. This is typically done using the command:

     ```bash
     rasa run actions
     ```

   - This command starts the action server, which listens for action calls from the Rasa server.

4. **Test the Action**:
   - Use `rasa interactive` to test the action within a conversation to see how it performs and ensure it triggers under the right conditions.

## Conversion of Markdown Files to YAML

To integrate Markdown data into Rasa:

1. **Extract Information**: Manually or via a script, transform Markdown data into YAML format.
2. **Format Examples**:

   ```yaml
   nlu:
   - intent: greet
     examples: |
       - Hello
       - Hi there
   ```

## Additional Resources and Commands

### Test Without Training

For a quick functionality test without full training:

```bash
rasa interactive
```

### Comprehensive Training and Running

Once fully configured, you can use the following commands for training and running your chatbot:

```bash
rasa train
rasa shell
```

## Deployment and Operation

**Running the Chatbot**:
- Deploy the chatbot within the NYU HPC environment, ensuring it has access to necessary APIs and databases for retrieving HPC-specific data.


## Conclusion

This comprehensive guide and documentation ensure that the AI chatbot is not only functional but also a robust tool for facilitating user interaction with the NYU High Performance Computing system. By following the outlined steps, the chatbot will effectively support HPC users, improving their experience and efficiency in utilizing computational resources.