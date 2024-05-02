# Get Slack user icon.
Export user icon in slack service.

# Environment

- OS: Windows 11 23H2
- python: 3.11.1
- requests: 2.31.0
- urllib3: 2.2.1

## Get OAuth token
To execute the Slack Web API, create a Slack App and obtain an OAuth token.

1. Create a Slack App. Open the app creation page and click on "Create New App."
<img src="./images/create.png" alt="Create New App">

2. Select "From an app manifest" and paste the contents of manifest.yaml, then follow the instructions.
<img src="./images/from-manifest.png" width="500px" alt="From an app manifest">
<img src="./images/paste-manifest.png" width="500px" alt="Paste manifest">

3. On the Basic Information page of the created app, click on "Install to Workspace" and select the workspace where you want to install it.
<img src="./images/install.png" alt="Install to Workspace">

4. Keep a note of the User OAuth Token on the OAuth & Permissions page.
<img src="./images/token.png" alt="User OAuth Token">

# How to use

```sh
# argv 1 : API key
# ex.)

$ python getUsersIcon.py xoxp-XXXXXXXXXXXXX-XXXXXXXXXXXXX-XXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# user_icon/[user_id].jpg

```