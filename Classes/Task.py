from crewai import Task
from typing import Optional

class TaskCreator():
    def __init__(self, agent = None):
        self.agent = agent

    def create(self, description, expected_output, **kwargs):
        task_config = {
            "description": description,
            "expected_output": expected_output,
            **kwargs
        }

        if self.agent:
            task_config["agent"] = self.agent

        if  kwargs.get('tools'):
            task_config["output_file"] = kwargs["output_file"]
        
        return Task(**task_config)