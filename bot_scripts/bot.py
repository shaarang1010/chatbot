from nltk.chat.util import Chat, reflections


class Bot:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    financy_pairs = [
        [
            r"my name is (.*)",
            ["Hello %1, How are you today ?", ]
        ],
        [
            r"what is your name ?",
            ["My name is ASM and I am a cyberpunk ", ]
        ],
        [
            r"how are you ?",
            ["I'm good\nHow about You ?", ]
        ],
        [
            r"sorry (.*)",
            ["OK", ]
        ],
        [
            r"i'm (.*) doing good",
            ["Nice to hear that", "Alright :)", ]
        ],
        [
            r"hi|hey|hello",
            ["Hello", "Hey there", ]
        ],
        [
            r"Can I get (.*) for my subject ?",
            ["No. Ask Duh", ]

        ],
        [
            r"(.*) do you do?",
            ["I do Research and teaching, do you want to collaborate", "I am a shit stirrer and post stuff on facebook", "I am the CYBERPUNK!!"]
        ],
        [
            r"(.*) money",
            ["Provide receipts", "Apply through expensify", ]
        ],
        [
            r"(.*) subject budget? ",
            ["We dont have any money", "Ask HOD"]
        ],
        [
            r"quit",
            ["Bye!"]
        ]
    ]

    henry_pairs = [
        [
            r"my name is (.*)",
            ["Hello %1", ]
        ],
        [
            r"what is your name ?",
            ["I am Mr.Duh, I dont know what I do here!", ]
        ],
        [
            r"how are you ?",
            ["I'm good\nHow about You ?", ]
        ],
        [
            r"sorry (.*)",
            ["Its okay you know, you know", ]
        ],
        [
            r"i'm (.*) doing good",
            ["Good", ]
        ],
        [
            r"hi|hey|hello",
            ["Hello", "Hey there", ]
        ],
        [
            r"Can I get (.*) for my subject ?",
            ["Ask Fei", ]

        ],
        [
            r"(.*) do you do?",
            ["I dont know what I do, you know. I am OVERARCHING , you know.",
             "I dont attend work, just go on trips", "You know, ...., you know, .... you know, ..., ask Fei"]
        ],
        [
            r"(.*) subject budget? ",
            ["We dont have any money", "Ask Fei!"]
        ],
        [
            r"(.*) service points",
            ["We should be OVERARCHING the department", "You know ... Jinli... Lianhua... You know, know"]
        ],
        [
            r"quit",
            ["You know, Bye!"]
        ],
    ]

    def chat(self, question):
        response = ''
        if self.name == 'ASM':
            chat = Chat(self.financy_pairs, reflections)
        elif self.name == 'Mr.Duh':
            chat = Chat(self.henry_pairs, reflections)
            if ("something random" in question) == True:
                response = chat.respond(question)
                response = response.split(',')
                bot_response = " you know ".join(response)
                return bot_response
        return chat.respond(question)

    def bot_test(self):
        return ('Bot is functioning')
