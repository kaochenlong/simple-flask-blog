from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

STYLES = "text-xl w-full md:w-1/2 p-2 border border-gray-900 rounded-sm"


class PostForm(Form):
    title = StringField(
        "標題",
        validators=[InputRequired()],
        render_kw={"placeholder": "請填寫標題", "class": STYLES},
    )
    content = TextAreaField(
        "內文", render_kw={"placeholder": "文章內容", "class": STYLES}
    )
