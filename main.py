from nltk.chat.util import Chat,reflections

QA = [
        [
            r"Hi|Hello|Hey",
            ["Hello.","Hey there.",]
        ],
        [
            r"what is the college time?",
            ["College Timing is from 9:00 am to 5:00 pm.",]
        ],
        [
            r"How many seats are there in (_*) Branch?",
            ["Generally, there are 60 seats in every branch. Except 'AIDS' has 30 seats.",]
        ],
        [
            r"Where is the college located",
            ["The college is locates at K.T. Marg, Vartak College Campus Vasai Road, Vasai-Virar, Maharashtra 401202."]
        ],
        [
            r"How many courses are there in college?",
            ["There are 8 courses in the college."]
        ],
        [
            r"How many departments are there in college?",
            ["1.COMPUTER ENGINEERING\n2.INFORMATION TECHNOLOGY\n3.ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING\n4.INSTRUMENTATION ENGINEERING\n5.COMPUTER SCIENCE AND ENGINEERING(DATA SCIENCE)\n6.CIVIL ENGINEERING\n7.ARTIFICIAL INTELLIGENCE AND DATA SCIENCE\n8.MECHANICAL ENGINEERING",]
        ],
        [
            r""
        ]
    ]
def bott():
    print("Hi,there. I'm Bot from Vidyavardhini's College of Engineering and Technology.\nType 'Quit' to leave the chat.")

    chat = Chat(QA,reflections)
    chat.converse()
if _name_ == "_main_":
    bott()