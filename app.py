from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        skills = request.form.get("skills", "")
        goal = request.form.get("goal", "")
        hours = request.form.get("hours", "")

        if "cyber" in goal.lower():

            result = f"""
🔮 FUTURE SELF SIMULATION

In 12 months:

You have completed networking fundamentals,
Linux security training, and hands-on projects.

You are ready for entry-level Cybersecurity
Analyst roles and internships.


CAREER PATH: Cybersecurity Analyst

CURRENT SKILLS:
{skills}

AVAILABLE TIME:
{hours} hours/week

MISSING SKILLS:
- Networking
- SIEM
- Incident Response

30-DAY ROADMAP

Week 1:
Networking Basics

Week 2:
Linux Security

Week 3:
Wireshark

Week 4:
SOC Fundamentals

PROJECTS:
- Port Scanner
- Log Analyzer
- Vulnerability Scanner
"""

        elif "ai" in goal.lower():

            result = f"""
🔮 FUTURE SELF SIMULATION

In 12 months:

You have built AI projects,
learned machine learning,
and created a portfolio.

You are ready for AI Engineer
internships and junior roles.


CAREER PATH: AI Engineer

CURRENT SKILLS:
{skills}

AVAILABLE TIME:
{hours} hours/week

MISSING SKILLS:
- Machine Learning
- Statistics
- Deep Learning

30-DAY ROADMAP

Week 1:
Advanced Python

Week 2:
Machine Learning

Week 3:
Neural Networks

Week 4:
AI Project

PROJECTS:
- Chatbot
- Image Classifier
- Recommendation System
"""

        else:

            result = f"""
🔮 FUTURE SELF SIMULATION

Goal detected:
{goal}

Based on your available time and skills,
a custom learning path will be generated.

CURRENT SKILLS:
{skills}

AVAILABLE TIME:
{hours} hours/week

SUGGESTED PLAN

Week 1:
Research the field

Week 2:
Learn fundamentals

Week 3:
Practice projects

Week 4:
Build portfolio project
"""

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)