#!/usr/bin/env python
# -*- coding: utf-8 -*-

import  commit_explainer_util as util
import click
import sys

@click.Group
def cli():
    pass

@cli.command()
@click.option("--model", required=True, default="deepseek-ai/DeepSeek-V3")
@click.option("--base-url", required=True, default="https://api.hyperbolic.xyz/v1")
@click.option("--api-key", required=True)
def commit_explainer(model, base_url, api_key):
    input_string = sys.stdin.read().strip()
    if not input_string:
        click.echo("No input provided!")
        return

    click.echo("--> Executing explainer")
    click.echo(input_string)
    explanation = util.execute_chat_completion(base_url=base_url, api_key=api_key, model=model,
                                               diff_content=input_string)

    click.echo("--> Result of commit explanation")
    click.echo(explanation.strip())

@cli.command()
@click.option("--msg-file", required=True)
@click.option("--commit-source", required=True)
@click.option("--model", required=True, default="deepseek-ai/DeepSeek-V3")
@click.option("--base-url", required=True, default="https://api.hyperbolic.xyz/v1")
@click.option("--api-key", required=True)
@click.option("--branch-prefixes", required=True, default="feature/,bugfix/")
def prepend_task_to_commit_msg(msg_file, commit_source, model, base_url, api_key, branch_prefixes):
    print_header(f"APPEND AI GENERATED COMMENT TO COMMIT: commit source={commit_source}")

    if commit_source != "message":
        click.echo("Commit message is not supplied by user!")
        return

    branch_name = util.check_if_task_branch(branch_prefixes)

    if not branch_name:
        click.echo("It is not a task branch")
        return

    commit_msg = util.read_file(msg_file)

    if commit_msg:
        commit_msg = commit_msg.strip()
    else:
        commit_msg = ""

    diff_content = util.diff_staged_changes()

    explanation = util.execute_chat_completion(base_url=base_url, api_key=api_key, model=model,
                                               diff_content=diff_content)

    final_commit_msg = commit_msg+ "\n[AUTO]\n" + explanation

    util.write_file(msg_file, final_commit_msg)

def print_header(title):
    click.echo("---------------------------------------------------------------")
    click.echo(title)
    click.echo("---------------------------------------------------------------")


if __name__ == '__main__':
    cli()