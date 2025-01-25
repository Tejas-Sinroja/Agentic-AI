from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.file import FileTools
from dotenv import load_dotenv

load_dotenv()

file_agent = Agent(
    name='file handler',
    description='This is the tool for manage the directory of the project',               
    model = Groq(id='llama-3.3-70b-versatile'),
    tools=[FileTools()],
    show_tool_calls=True,
    instructions='Always help user to manage the files in directory if needed'
)

file_agent.print_response("Write about the files are available in the current directory")
