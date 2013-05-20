"""
Find and view messages in the qmail queue
"""
import os

def find_messages(directory='/var/qmail/queue/mess'):
    """
    Find messages in the qmail messages queue
    """
    messages = []
    directory_items = os.listdir(directory)
    for item in directory_items:
        item_path = "%s/%s" % (directory, item)
        if os.path.isdir(item_path):
            messages = messages + find_messages(item_path)
        else:
            messages.append(item_path)
    return messages

def output_messages(messages):
    """
    Given a list of messages, output them to screen one at a time
    """
    for message in messages:
        print message
        print "=" * 72
        print "".join(file(message))
        print "=" * 72
        raw_input("Press enter to continue: ")

if __name__ == '__main__':
    messages = find_messages()
    output_messages(messages)
