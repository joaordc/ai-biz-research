#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from business_research_crew.crew import BusinessResearchCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """

    print('-----------------------------------------------------------')
    print("|               Welcome to AI Biz Research!               |")
    print('-----------------------------------------------------------\n')
    topic = input("Insert a topic: ")
    subtopic = input("Insert a subtopic: ")
    print("Great. Starting a research about ", topic, ", focusing on ", subtopic)

    inputs = {
        'topic': topic,
        'sub-topic': subtopic,
        'current_year': str(datetime.now().year)
    }
    
    try:
        BusinessResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        BusinessResearchCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BusinessResearchCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        BusinessResearchCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
