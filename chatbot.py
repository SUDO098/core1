import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello! Welcome!", "Hi there!"]],
    [r"my name is (.*)", ["Hello %1!"]],
    [r"(.*)courses(.*)", ["We offer B.Tech, M.Tech, MBA"]],
    [r"(.*)admission(.*)", ["Admissions are open!"]],
    [r"(.*)fees(.*)", ["Fees approx ₹1,00,000"]],
    [r"(.*)placement(.*)", ["Top companies visit"]],
    [r"bye|exit", ["Goodbye!"]],
    [r"(.*)", ["Sorry, I didn't understand"]]
]

chatbot = Chat(pairs, reflections)
print("Chatbot started...")
chatbot.converse()
