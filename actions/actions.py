# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideDefinition(Action):
    def name(self):
        return "action_provide_definition"

    def run(self, dispatcher, tracker, domain):
        last_message = tracker.latest_message.get('text').lower()
        if 'gpu cluster' in last_message:
            response = "A GPU cluster consists of multiple GPUs used collectively to speed up computational tasks."
        elif 'high performance computing' in last_message or 'hpc' in last_message:
            response = "High performance computing (HPC) involves using supercomputers and parallel processing techniques for complex computational tasks."
        elif 'distributed computing' in last_message:
            response = "Distributed computing involves multiple computers working on a single problem at the same time, often over the internet."
        else:
            response = "I'm not sure how to answer that. Could you specify what definition you need?"
        
        dispatcher.utter_message(text=response)
        return []
