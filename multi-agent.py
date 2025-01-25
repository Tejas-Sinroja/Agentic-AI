from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.file import FileTools
from phi.tools.python import PythonTools
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.playground import Playground,serve_playground_app


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

python_agent = Agent(
    name='python agent',
    model = Groq(id='llama-3.3-70b-versatile'),
    description='Your task  to help user to manage python code',
    tools=[PythonTools()],
    show_tool_calls=True,
    instructions='Generate the clear and user demanded code'

)

multi_agent = Agent(
    model = Groq(id='llama-3.3-70b-versatile'),
    team=[python_agent,file_agent],
    instructions='handle files in the directory also modify the current file if needed',
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

multi_agent.print_response('get the file name ''list_operations.py'' from the directory and replace the inner content with tuple examples ')
