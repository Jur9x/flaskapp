from flask_appbuilder import ModelView
from flask_appbuilder.fields import QuerySelectField
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Person

class PersonView(ModelView):
    datamodel = SQLAInterface(Person)
    list_columns = ["id", "full_name", "birth"]
    show_template = "appbuilder/general/model/show_cascade.html"


db.create_all()

appbuilder.add_view(
    PersonView, "People", icon="fa-folder-open-o", category="People"
)

