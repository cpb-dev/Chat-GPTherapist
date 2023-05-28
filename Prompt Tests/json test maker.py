import openai, json

openai.api_key = 'Your API Key'

prompt = "Your role is to create a JSON file for programming"

messages = [ { "role": "system", "content": prompt} ]

params = input("What are the parametors you want to test? \n")
message = f"Make a JSON file that has 20 entries with dummy data that resembles the structure for {params}"

messages.append(
    {"role": "user", "content": message}
)
chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages = messages
    )

reply = chat.choices[0].message.content
print(f"Done \n\n {reply}")

with open("sample.json", "w") as outfile:
    json.dump(reply, outfile)

test = input("OK?")
