#!/usr/bin/env python3

import uuid,random

ALL_SKILLS=['cooking hello fresh meals.. lol','cleaning the houuse (total dont use a robot for it)', 'driving (i was sideswiped by a police van)', 'writing (still shit at english though)']

class Task():
    def __init__(self,skill_required,duration=1):
        self.id=uuid.uuid4()
        self.skill_required=skill_required
        self.duration=duration
        self.status='open'
class Agent():
    def __init__(self,name=None):
        self.uid=uuid.uuid4()
        self.name=name if name else str(self.uid)[:8]
        num_skills=random.randint(1,3)
        self.capabilities=random.sample(ALL_SKILLS, num_skills)
    def can_do(self,skill):
        return skill in self.capabilities

def main():
    agents=[Agent(f"agent{str(i)}") for i in range(10)]
    for agent in agents:
        print(f"{agent.name} can {agent.capabilities}")
    task=Task('cooking hello fresh meals.. lol')
    print(f"task {task.id} requires {task.skill_required}")
    for agent in agents:
        if agent.can_do(task.skill_required):
            print(f"{agent.name} can do the task")
    print("task complete")

if __name__=="__main__":
    main()