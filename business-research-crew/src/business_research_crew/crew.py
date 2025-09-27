from dotenv import load_dotenv
import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, SerperScrapeWebsiteTool, FileWriterTool
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

load_dotenv()

@CrewBase
class BusinessResearchCrew():

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'], # type: ignore[index]
            verbose=True
        )

    @agent
    def red_team(self) -> Agent:
        return Agent(
            config=self.agents_config['red_team'], # type: ignore[index]
            verbose=True
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'], # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
            tools=[SerperDevTool(), SerperScrapeWebsiteTool(), FileWriterTool()]
        )

    @task
    def analyzing_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyzing_task'] # type: ignore[index]
        )

    @task
    def validating_task(self) -> Task:
        return Task(
            config=self.tasks_config['validating_task'] # type: ignore[index]
        )

    @task
    def checking_market_task(self) -> Task:
        return Task(
            config=self.tasks_config['checking_market_task'], # type: ignore[index]
            tools=[SerperDevTool(), SerperScrapeWebsiteTool()]
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'], # type: ignore[index]
            tools=[FileWriterTool()]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            manager_llm=os.getenv("MODEL"),
            verbose=True,
            output_log_file="logs.txt",
            max_rpm=30
        )
