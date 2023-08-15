# NER Implementation by Francisco Ventura

Repo to showcase a basic Named Entity Recognition (NER) for multiple sentences involving the usage of Python, Flask and spaCy all together with a GitHub Actions workflow that runs a simple test on functions defined inside the `src/functions` directory. 

The template is configured to run on with either Codespaces + Docker, Docker on its own or on a local environment directly with the Conda package manager.

# Template Features

- Usage of the `pytest` package to run unit tests.
- Definition of a structure to that allows a team to better separate and manage new "data" projects.
- Ready to work with the `Fork-Branch-Pull` workflow to make contributions based on PR's from forks for each new feature.
- Implementation of `Docker` and Visual Studio Code `.devcontainers`
    - Set up of a complete environment for Codespaces
    - The ability to create docker-dev containers for Visual Studio Code
- Python package management using Conda Environments:
    - Installing dependencies with `conda` and `mamba`
    - Usage of an `environment.yml` file for defining new packages

# Requirements

Links to software required to work and run the code inside this repository.

- [Visual Studio Code](https://code.visualstudio.com/)
- [Anaconda](https://www.anaconda.com/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/download/win)

# Usage

## API Documentation

The API is created to only have one route to be executed, in which you will need to supply a JSON in a POST request to the route `http://localhost:5000/ner/spacy` and using the following schema:

```JSON
{
    "oraciones": [
        "sentence_1",
        "sentence_2",
        "...",
        "sentence_n"
    ]
}
```

Here is a `curl` command that can be run at the top-level directory to test the API with an input sample already made:

```bash
curl -X POST -H "Content-Type: application/json" -d @'data/raw/input_1.json' http://127.0.0.1:5000/ner/spacy
```

## Development Documentation

Taking the API Documentation in order to run the API, the first step will be to set up the development environment in any format preferred, followed by executing:

```bash
python app.py 
```

### Conda locally

#### Creation

Create a new conda environment from the `environment.yml` template:

```bash
conda env create -f environment.yml
conda activate template_env
```

#### Update

On each new package installation, please modify the `environment.yml` template to update dependencies and run:

```bash
conda deactivate # Important!
conda env update --name template_env --file environment.yml --prune
conda activate template_env
```

### Using Docker

#### Creation

Create a new environment with Docker from the `Dockerfile` + `environment.yml` template:

```bash
docker build -t python-notebook-img .
docker run -d -it --name pynotebooks_container -v "$(pwd)":/workspaces/python-notebooks-template -w /workspaces/python-notebooks-template python-notebook-img
```

#### Update

To update inside the container, the only command that needs to run is:

```bash
mamba env update -n base -f environment.yml
```

### Using Codespaces

#### Creation

For creation of an environment using conda the best way to do it is by going directly to [your codespaces](https://github.com/codespaces) on GitHub and creating one from the repo that uses this template.

#### Update

And the update is the same as the one on a docker container on each new package definition inside `environment.yml`:

```bash
mamba env update -n base -f environment.yml
```

# Template for this repo

```│
├── .devcontainer          <- Directory to store the dev container configuration for Visual Studio Code.
│   └── devcontainer.json  <- YML file that stores the settings for the creation of a dev container, both 
│                             the settings for Visual Studio Code and how to execute the environment creation.
│
├── .github / workflows    <- Route where GitHub Actions recognizes that a new Workflow needs to run.
│   └── template_ci.py     <- Simple Action that runs the only test stored under the "tests" directory.
│
├── data
│   ├── processed          <- The final version of data that passes through the code.
│   └── raw                <- The original data dump for functions and notebooks to use.
│
├── src                    <- Source code for use in this project.
│   ├── __init__.py        <- Makes src a Python module.
│   │
│   └── functions          <- Scripts of funtions to share in the project.
│       └── features.py
│
├── tests                  <- Source directory for all tests related work.
│   ├── __init__.py        <- Makes tests a Python module.
│   │
│   └── test_env_vars.py   <- The naming convetion for new tests depends on the script that is 
│                            going to be tested. The rule is to format "test_" + "name_of_file.py".
│
│── Dockerfile             <- Definition of how to create the image to run this repo as a dev container.
│
│── .env                   <- File to store local development variables.
│
│── pytest.ini             <- Config file for pytest to run test specific env variables.
│
│── pr_template.md         <- Markdown template for new PRs done to this repository (needs GitHub setup).
│
├── README.md              <- The top-level README file this project.
│
├── environment.yml        <- Package configuration for conda (like a requirements.txt for conda).
│
└── requirements.txt       <- In case anyone on the team wants to run "venv" environments.
```

# Useful Links

## Project Template

- [Project template in which this Repo is based on (GitHub Pages)](https://drivendata.github.io/cookiecutter-data-science/)

## Dev Containers

- [Introduction to dev containers - How to configure the entire env (GitHub Docs)](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)
- [Using Images, Dockerfiles, and Docker Compose (Development Containers)](https://containers.dev/guide/dockerfile)
- [Dev Containers: Getting Started (Microsoft)](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/devcontainers/)

## Testing

- [Good Integration Practices that we followed on this Repo (docs.pytest.org)](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html)
- [Get Started on Pytest (docs.pytest.org)](https://docs.pytest.org/en/7.1.x/getting-started.html)

## GitHub Actions

- [Set up of miniconda (GitHub Actions Marketplace)](https://github.com/marketplace/actions/setup-miniconda)
- [Automate your workflow from idea to production (GitHub)](https://github.com/features/actions)
