import subprocess

import openai

SYSTEM_CONTENT = "You are a software developer who is expert on GIT source code management system"
USER_CONTENT = "Summarize the changes as a commit message. Summary should begin with the imperative mood. Each piece of summary should be separated by a new line with a dash at the beginning. The commit changes are below:\n"

def execute_chat_completion(*, base_url, api_key, model, diff_content):
    client = openai.OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_CONTENT},
            {"role": "user", "content": USER_CONTENT + diff_content},
        ],
        temperature=0.7,
        max_tokens=1024 * 10
    )

    response = chat_completion.choices[0].message.content
    client.close()
    return response

def read_file(msg_file):
    msg = None

    with open(msg_file) as file:
        msg = file.read()

    if msg:
        msg = msg.strip()

    return msg

def write_file(msg_file, msg):
    with open(msg_file, "w") as file:
        file.write(msg)

def check_if_task_branch(branch_prefixes):
    branch = check_if_branch_exists()
    if not branch:
        return None

    for prefix in branch_prefixes.split(","):
        if branch.startswith(prefix.strip()):
            return branch

    return None

# git methods
def diff_staged_changes():
    return run_shell_command("git diff --staged")

def check_if_branch_exists():
    branch_name = read_git_branch_name()

    if not branch_name:
        return None
    else:
        return branch_name

def read_git_branch_name():
    return run_shell_command("echo $(git symbolic-ref --short HEAD 2> /dev/null)")

# Executing commands
def run_shell_command(command, capture_output=True):
    completed_process = subprocess.run(command, shell=True, capture_output=capture_output)
    ensure_command_execution_successful(completed_process)

    if capture_output:
        return completed_process.stdout.decode("UTF-8").strip()
    else:
        return ""


def ensure_command_execution_successful(completed_process):
    if completed_process.returncode != 0:
        print("Shell command failed!")

        if completed_process.stdout:
            print(completed_process.stdout.decode("UTF-8"))

        if completed_process.stderr:
            print(completed_process.stderr.decode("UTF-8"))

        exit(completed_process.returncode)