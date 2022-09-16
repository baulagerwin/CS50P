from .components import go_back_with_arg
from .add_qna.add_qna_menu import add_qna_menu
from .view_qna import view_qna
from .update_qna import update_qna
from .delete_qna import delete_qna

def search_subject_menu_list():
  return [
    {
      "todo": "Add Q&A",
      "match": "add",
      "unmatches": ["view", "update", "delete", "back"],
      "function": add_qna_menu
    },
    {
      "todo": "View Q&A",
      "match": "view",
      "unmatches": ["add", "update", "delete", "back"],
      "function": view_qna
    },
    {
      "todo": "Update Q&A",
      "match": "update",
      "unmatches": ["add", "view", "delete", "back"],
      "function": update_qna
    },
    {
      "todo": "Delete Q&A",
      "match": "delete",
      "unmatches": ["add", "view", "update", "back"],
      "function": delete_qna
    },
    {
      "todo": "Go back",
      "match": "back",
      "unmatches": ["add", "view", "update", "delete"],
      "function": go_back_with_arg
    },
  ]