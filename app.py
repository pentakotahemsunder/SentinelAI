from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="API-KEY")

model = genai.GenerativeModel("gemini-2.5-flash")


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        skills = request.form.get("skills", "")
        goal = request.form.get("goal", "")
        hours = request.form.get("hours", "")

        prompt = f"""
You are Sentinel AI.

Current Skills:
{skills}

Career Goal:
{goal}

Available Hours Per Week:
{hours}

Respond EXACTLY in this format:

SKILL GAP:
...

ROADMAP:
...

FUTURE SELF:
...

PROJECTS:
...

CERTIFICATIONS:
...

CAREER ADVICE:
...

Use bullet points and short paragraphs.
Do NOT use markdown symbols like **, ##, *, or ---.
"""

        try:
            response = model.generate_content(prompt)
            result = response.text

            return render_template(
                "index.html",
                result=result
            )

        except Exception as e:
            return render_template(
                "index.html",
                result=f"Error: {str(e)}"
            )

    return render_template("index.html", result="")
    

if __name__ == "__main__":
    app.run(debug=True)
