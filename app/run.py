import os
from flask import Flask, render_template
# from flask.templating import render_template

template_dir = os.path.abspath('templates')
app = Flask(
    __name__,
    template_folder=template_dir
)


@app.route("/")
@app.route("/home/")
def home():
    """Home Page."""
    return render_template(
        'page-template.html',
        title="Home",
        page_content="Welcome to Home Page"
    )


@app.route("/about/")
def about():
    """About Page."""
    return render_template(
        'page-template.html',
        title="About",
        page_content="About us content goes here"
    )


@app.route("/contact/")
def contact():
    """Contact Page."""
    return render_template(
        'page-template.html',
        title="Contact",
        page_content="Contact us content goes here"
    )


@app.errorhandler(404)
def page_not_found(e):
    """Not Found Page."""
    return render_template(
        'page-template.html',
        title="Not Found",
        page_content="Seems you are lost. Go back to home page"
    )


if __name__ == "__main__":
    app.run()
