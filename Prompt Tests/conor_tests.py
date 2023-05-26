import openai

openai.api_key = 'Your API Key'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.75,
    )
    return response.choices[0].message["content"]

sentiment = "Therapist"

user_sheet = """
I am sad and lonley!
"""

prompt = f"""
YOur role is to act as a {sentiment} to the user
provide valuable advice based on the users mood
as defined in the fact sheet

User fact sheet: ```{user_sheet}```
"""
response = get_completion(prompt)
