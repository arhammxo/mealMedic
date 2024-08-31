import anthropic

claude_api_key = "API_KEY"

client = anthropic.Anthropic(
    api_key=claude_api_key,
)

system_prompt = """
You are an expert cinema and show enthusiast with the knowledge of every TV show, web series, as well as anime series. Use your knowledge to help recommend the user to pick a random episode of a given show. Also consider the mood, plot specifics, and other aspects that the user may of may not mention.

Respond as an edgy genz person with ONLY ONE EPISODE unless asked to do otherwise. Also explain the episode in the same manner.
"""

base_prompt = """
Black Mirror
"""



def get_response_from_claude(prompt):
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1024,
        temperature=0.9,
        system=system_prompt,
        messages=[
            {"role": "user",
             "content":[
                {
                    "type": "text",
                    "text": prompt
                }
             ] 
                 
            }
        ]
    )
    print(response.content[0].text)

get_response_from_claude(base_prompt)
