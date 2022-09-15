from .add_qna import add_qna
from .view_qna import view_qna
from .update_qna import update_qna
from .delete_qna import delete_qna

def search_subject_menu_list():
  return [
    {
      "todo": "Add Q&A",
      "match": "add",
      "unmatches": ["view", "update", "delete"],
      "function": add_qna
    },
    {
      "todo": "View Q&A",
      "match": "view",
      "unmatches": ["add", "update", "delete"],
      "function": view_qna
    },
    {
      "todo": "Update Q&A",
      "match": "update",
      "unmatches": ["add", "view", "delete"],
      "function": update_qna
    },
    {
      "todo": "Delete Q&A",
      "match": "delete",
      "unmatches": ["add", "view", "update"],
      "function": delete_qna
    }
  ]