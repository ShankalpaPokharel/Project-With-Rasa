# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
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

# from typing import Any, Text, Dict, List
# from datetime import datetime

# #ActionGetTime inherit the Rasa's 'Action' class
# class ActionGetTime(Action):
#     def name(self) -> Text:
#         return "action_get_time"
#     def run(self,dispatcher:CollectingDispatcher,
#             tracker : Tracker,
#             domain: Dict[Text,Any],
#             ) -> List[Dict[Text,Any]]:
#         current_time = datetime.now().strftime("%H:%M:%S")
#         dispatcher.utter_message(text=f"The current time is {current_time}")
#         return []

from typing import Any, Text, Dict, List
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetTime(Action):
    def name(self) -> Text:
        return "action_get_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        current_time = datetime.now().strftime("%H:%M:%S")
        # dispatcher.utter_message(template="utter_current_time",current_time=current_time)
        dispatcher.utter_message(template="utter_current_time", current_time=current_time)
        return []



