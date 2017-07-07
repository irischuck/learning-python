from sys import exit
# make a dictionary of people and their relationship to Harry Potter

people = {'james': 'father',
            'lily': 'mother',
            'ron': 'male friend',
            'hermione': 'female friend',
            'ginny': 'love interest lol',
}

def start():
        print "To learn more about how Harry Potter is related to others, pick a name:"
        print "James, Lily, Ron, Hermione, or Ginny?"
        print "To exit out, type 'quit'"
        answer_time()

def answer_time():
        choice = raw_input("> ")
        if choice.lower() in people.keys():
            print "%s is Harry's" % choice.capitalize(), people[choice] + "."
            print "If you want to find out more, type another name."
            answer_time()
        elif choice == "quit":
            exit(0)
        else:
            print "That isn't an option. Type another name."
            answer_time()
        start()

start()
