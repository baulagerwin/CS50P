from .add_subject import add_subject
from .add_subjects import add_multiple_subjects
from ..components import go_back

def add_subject_menu_list():
    return [
        {
            "todo": "Single subject",
            "match": "single",
            "unmatches": ["multiple", "back"],
            "function": add_subject
        },
        {
            "todo": "Multiple subjects",
            "match": "multiple",
            "unmatches": ["single", "back"],
            "function": add_multiple_subjects
        },
        {
            "todo": "Go back",
            "match": "back",
            "unmatches": ["single", "multiple"],
            "function": go_back
        },
    ]