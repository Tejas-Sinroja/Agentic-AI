from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.python import PythonTools
from dotenv import load_dotenv

load_dotenv()

python_agent = Agent(
    name='python agent',
    model = Groq(id='llama-3.3-70b-versatile'),
    description='Your task  to help user to manage python code',
    tools=[PythonTools()],
    show_tool_calls=True,
    instructions='Generate the clear and user demanded code'

)

python_agent.print_response("Write a python script for fibonacci series and display the result till the 10th number and then delete the created file name fibonacci")
