from ..components import go_back_with_arg
from .add_qna import add_qna
from .add_multiple_qna import add_multiple_qna

def add_qna_menu_list():
    return [
        {
            "todo": "Single Q&A",
            "match": "single",
            "unmatches": ["multiple", "back"],
            "function": add_qna
        },
        {
            "todo": "Multiple Q&A",
            "match": "multiple",
            "unmatches": ["single", "back"],
            "function": add_multiple_qna
        },
        {
            "todo": "Go back",
            "match": "back",
            "unmatches": ["single", "multiple"],
            "function": go_back_with_arg
        }
    ]