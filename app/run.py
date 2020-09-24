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
        title="Home"
    )


@app.route("/about/")
def about():
    """About Page."""
    return render_template(
        'page-template.html',
        title="About"
    )


@app.route("/contact/")
def contact():
    """Contact Page."""
    return render_template(
        'page-template.html',
        title="Contact"
    )


@app.errorhandler(404)
def page_not_found(e):
    """Not Found Page."""
    return render_template(
        'page-template.html',
        title="Not Found"
    )


if __name__ == "__main__":
    app.run()
