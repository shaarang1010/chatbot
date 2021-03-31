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
            ["My name is Financy and I handle budgeting around here ", ]
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
            ["I do finance", "I do casuals", "I am the right hand!"]
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
            ["I dont know what I do, you know. I am just a clown, you know.",
             "I dont attend work, just go on trips", "You know, ...., you know, .... you know, ..., ask Fei"]
        ],
        [
            r"(.*) subject budget? ",
            ["We dont have any money", "Ask Fei!"]
        ],
        [
            r"(.*) something random",
            ["Sigh view am high neat, half to what. Sent late held than, set why wife our. If an blessing, building steepest. Agreement distrusts, mrs six affection, satisfied. Day blushes visitor end company old  prevent chapter. Consider declared out expenses her concerns. No at indulgence conviction particular unsatiable boisterous discretion. Direct enough off others, say eldest may exeter she. Possible all ignorant , supplied get settling,  marriage recurred.",]
        ],
        [
            r"quit",
            ["You know, Bye!"]
        ],
    ]

    def chat(self, question):
        response = ''
        if self.name == 'Financy':
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
