from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor

from api.ai.llms import get_openai_llm

from api.ai.tools import (
    send_me_email,
    get_unread_emails,
    research_email
)

EMAIL_TOOLS_LIST = [
    send_me_email,
    get_unread_emails
]


def get_email_agent():
    model = get_openai_llm()
    agent = create_react_agent(
        model=model,  
        tools=EMAIL_TOOLS_LIST,  
        prompt="You are a helpful assistant for managing my email inbox for generating, sending, and reviewing emails.",
        name="email_agent"
    )

    return agent


def get_research_agent():
    model = get_openai_llm()
    agent = create_react_agent(
        model=model,  
        tools=[research_email],
        prompt = """
You are an expert research assistant.

Before writing your answer, ensure you have covered the important aspects of the user's request.

Your final output must:
- answer the user's question completely,
- be factually accurate,
- be concise,
- be well structured,
- be suitable for sending as an email,
- generate a clear email subject and body.
""",
        name='research_agent',
    )

    return agent

# supe = get_supervisor()
# supe.invoke({"messages": [{"role": "user", "content": "Find out how to create a latte then email me the results."}]})
def get_supervisor():
    llm = get_openai_llm()
    email_agent = get_email_agent()
    research_agent = get_research_agent()

    supe = create_supervisor(
        agents=[email_agent, research_agent],
        model = llm,
         prompt=(
    "You supervise two agents:\n"
    "- research_agent: researches topics and prepares email drafts.\n"
    "- email_agent: sends and manages emails.\n\n"
    "If a user's request requires multiple steps, invoke the agents in sequence.\n"
    "For example, if the user asks to research a topic and email the results, "
    "first call research_agent, then call email_agent with the generated subject "
    "and body. Only finish after all requested tasks have been completed."
),
       
    ).compile( )
    return supe