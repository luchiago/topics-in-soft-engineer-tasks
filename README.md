# Topics in Software Engineer tasks

This repository contains python scripts to make requests, retrieve and process some data from Github with [Github API](https://docs.github.com/en/rest)

It was made with REST API V3 from Github, Python 3.8 and requests lib

## Setup

First, verify if you have Python 3.6 or higher installed and pip

Create a virtualenv following this [tutorial](https://tutorial.djangogirls.org/en/django_installation/#virtual-environment)

After that, with the virtualenv activated, run this command: `pip install -r requirements.txt`

Finally, run `cp .env.sample .env` and fill the `.env` file with the required info

For the `GITHUB_OAUTH_TOKEN`, follow this [steps](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

For the `REPO`, put the repository in this format, for example: `spring-projects/spring-boot`

Get the total issues count from the repository manually, is the sum of all issues (open and closed) and pull requests (open and closed).

Get the total of commits from the repository manually, I recommend that you get from principal branch (master or main)

## Running

If everything is ok with your installation, run this command on the terminal:

```shell
make
```
