# Commit Explainer AI

`commit-explainer-ai` is a command-line tool that helps you append AI-generated comments to your commit messages based on the staged changes in your Git repository.
This tool summarize the changes made in the commit and present it in a human-friendly format.

e.g.
```
Author: <Author Name> <author_email> 
Date:   Thu Jan 30 23:03:35 2025 +0300

    [AUTO]
    Add a new line to the end of the file.
    - Include an additional line in sample.txt.
```

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```sh
    cd <project_directory>
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use the `commit_explainer` tool, you need to have a valid API key for an OpenAPI compliant AI service and the necessary configurations. There is an example "prepare-commit-msg" file under the folder "examples".
You may update that file according to your environment and copy it to under your git hooks folder.

### Command

```sh
./commit_explainer.py prepend_task_to_commit_msg --msg-file <path_to_commit_msg_file> --commit-source <commit_source> --model <model_name> --base-url <base_url> --api-key <api_key> --branch-prefixes <branch_prefixes>


