# AIbiz Reseach

Welcome to the AIBiz Research project (short for AI Business Research), powered by [crewAI](https://crewai.com). This multi-agent AI system aims to help entrepeneurs and hackthon participants quickly gather relevant market information and pre-validated ideas during their first hours of brainstorming. 

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Setting up 

Before running the project, you need to set up your environment variables. Create a file named `.env` in the root of your project and add the following keys:
- `MODEL`: We reccomend using the `gemini/gemini-2.0-flash-lite` model, for velocity and free pricing for a limited rate amount. 
- `GEMINI_API_KEY`, or the model equivalent api key
- `SERPER_API_KEY`: Set it up for free at the [Serper website](https://serper.dev/).


For more information in setting up the LLM model and LLM API keys, check the [crewAI documentation](https://docs.crewai.com/en/concepts/llms).

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This project will run and, as a final result, will create a `research.md` file and a `report.md` file. 