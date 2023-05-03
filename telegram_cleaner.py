import os
import json

with open('result.json') as f:
    data = json.load(f)

# loop through the "messages" array and select the text with type "message"
messages = [msg["text"] if isinstance(msg["text"], str) else json.dumps(msg["text"])
            for msg in data["messages"] if msg["type"] == "message"]

# create a new file and write the selected text to it
with open('output.txt', 'w') as f:
    for message in messages:
        f.write(message)
        f.write('\n')

with open('output.txt', 'r') as f_in, open('new_file.txt', 'w') as f_out:
    for line in f_in:
        if not line.startswith('[') or not line.startswith(''):
            f_out.write(line)


if os.path.exists("output.txt"):
    os.remove("output.txt")
