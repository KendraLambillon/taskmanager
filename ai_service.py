import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):

    if not client.api_key:
        return ["Error: The API key of OpenAI is not set"]
    
    try:
        prompt = f"""Break down the following complex task into a list of 3 to 5 actionable subtasks

        Task: {description}

        Format response:
        - Subtask 1
        - Subtask 2
        - Subtask 3
        - etc.
        
        Answer only with the list of subtasks, one per line, starting each line ...
        """
        params = {
            "model": "gpt-4.1-mini",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that breaks down complex tasks into simple actionable subtasks."},
                {"role": "user", "content": prompt}
            ],
            "max_completion_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "minimal"
        }

        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        return subtasks if subtasks else ["Error: No subtasks generated"]


    except Exception as e:
        return [f"Error: {str(e)}"]