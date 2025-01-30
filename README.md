# Commit Explainer AI

`commit_explainer_ai` is a command-line tool that helps you prepend AI-generated comments to your commit messages based on the staged changes in your Git repository.

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

To use the `commit_explainer` tool, you need to have a valid API key for the AI service and the necessary configurations. There is an example "prepare-commit-msg" file under the folder "examples"

### Command

```sh
./commit_explainer.py prepend_task_to_commit_msg --msg-file <path_to_commit_msg_file> --commit-source <commit_source> --model <model_name> --base-url <base_url> --api-key <api_key> --branch-prefixes <branch_prefixes>
