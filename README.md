# metadata
Metadata examples and their schemas for data procured by waste package monitoring, digital twin, decision dashboard. Part of the [H2020 Predis project](https://predis-h2020.eu/predis-project/), [work package 7](https://predis-h2020.eu/work-packages/), subtask 7.4.

## Usage
Metadata and schemas that are used to validate and track waste package sensor measurements, digital twin model output. 

## Installation / run tests
* First clone the repository. 
* Then install a conda environment using the provided environment file
```
conda env create --prefix ./conda-env -f environment.yml 
```
You could also use mamba (which is usually much faster).

* Activate the environment
```
conda activate ./conda-env
```
* Execute either the tests using 
```
python -m pytest .
```

## Contributing with development

The [Pull Request Workflow](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) is used. Below is a summary of the necessary steps you need to take:

1. Clone this repository
2. Create a branch branch named after what's being done (`lower-case-with-hyphens`)
3. Add your changes and commit
4. Make a pull request to `predis-h2020/metadata`, targeting the `main` branch
