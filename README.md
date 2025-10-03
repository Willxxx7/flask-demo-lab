Flask Demo Lab

This project is a simple Flask web app to help you learn:

How to clone a project from GitHub

How to run a Flask server inside your VM/container

How to edit HTML and CSS and see your changes live

How to collaborate as a team using GitHub

1. Clone this repo

Open Git Bash (or your terminal inside Ubuntu Server) and run:

git clone git@github.com:Willxxx7/flask-demo-lab.git
cd flask-demo-lab


This makes a local copy of the GitHub repo on your machine.

2. Install requirements

Make sure Python 3 is installed in your container/VM. Then install Flask with:

pip install -r requirements.txt


This uses requirements.txt to install Flask and any other needed packages.

3. Run the Flask app

Run:

python app.py


Now open your browser and go to:

http://localhost:5000


You should see the demo web page.

4. Make a change

Try editing one of these files:

templates/index.html → change text, add a new heading, or insert a paragraph.

static/style.css → change colours, font size, or add formatting.

Save the file, then refresh your browser. You’ll see your changes immediately.

5. Upload your changes to GitHub

When you make changes, use the Git workflow:

git add .
git commit -m "Describe what you changed"
git push

What these commands mean:

git add . → stages all changes (prepares them to be saved).

git commit -m "message" → saves your changes locally with a message.

git push → sends your committed changes to GitHub so others can see them.

6. Get the latest updates from others

If another team member has pushed changes, you need to update your local copy:

git pull

What this means:

git pull → downloads the latest changes from GitHub and merges them into your project.

7. Collaboration tips

Work in teams of 4 (suggested).

Each student should try to add something small (text, style, or formatting).

Write commit messages that clearly describe your changes. Example:

"Added a welcome heading"

"Changed background colour to blue"

If Git shows a merge conflict, that means two people edited the same line. Work together to fix it.

✅ By completing this lab, you are learning real-world cloud collaboration skills:

Using GitHub like developers do.

Running Flask apps in containers/VMs like in cloud environments.

Editing code together as a team.