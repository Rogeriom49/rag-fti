from crewai import Agent

class AgentCreator():
    def __init__(self, llm = None):
        self.llm = llm

    def create(self, role, goal, backstory, **kwargs):
        agent_config = {
            "role": role,
            "goal": goal,
            "backstory": backstory,
            "language": "pt-BR",
            **kwargs
        }

        if self.llm:
            agent_config["llm"] = self.llm

        if  kwargs.get('tools'):
            agent_config["tools"] = kwargs["tools"]
        
        
        return Agent(**agent_config)