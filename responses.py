from random import randint

correct = ["Correct! One more...",
"Fabuolous! Let's have another.",
"That's amazing! Let's continue.",
"Keep it up that way!",
"You're doing great.",
"That is insane. You are amazing,",
"Superb. Keep going!",
"You are on your way, man!",
"You are making us proud, buddy.",
"Hey, have one more on your way.",
"You are so good at this.",
"Let's have some more!",
"Can you do more? Definetly!"
]

try_again = ["Let's try again, shall we?",
"I bet you can do it this time.",
"That is not quite right.",
"Maybe you can do it this time?",
"Hey, don't feel down. Try again.",
"You should have another guess at this.",
"I am sorry, but this is incorrect. Shall we try one more time?"]

class Fetch(object):
    def correct(self):
        return correct[randint(0,len(correct)-1)]

    def try_again(self):
        return try_again[randint(0,len(try_again)-1)]

fetcher = Fetch()