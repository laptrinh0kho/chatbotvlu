# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import feedparser

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
class ActionGetLottery(Action):

    def name(self) -> Text:
        return "action_get_lottery"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
        #url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
        #url = 'http://kqxs.net.vn/rss-feed/mien-nam-xsmn.rss'
        url = 'http://kqxs.me/rssfeed/xsMB.rss'
        # Tien hanh lay thong tin tu URL
        feed_cnt = feedparser.parse(url)
        #entry = feed_cnt.entries[1]
        #return_msg = entry.title
        # Lay ket qua so xo moi nhat
        first_node = feed_cnt['entries']
        # Lay thong tin ve ngay va chi tiet cac giai
        return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
        # Tra ve cho nguoi dung
        #dispatcher.utter_message(return_msg)
        dispatcher.utter_message(text=return_msg)
        #dispatcher.utter_message(text="Hello World!")
        return []

class ActionTuyenSinh(Action):

    def name(self) -> Text:
        return "action_tuyen_sinh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="https://tuyensinh.vanlanguni.edu.vn/")

        return []