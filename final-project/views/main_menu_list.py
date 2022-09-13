from .review_subject import review_subject
from .add_subject.add_subject_menu import add_subject_menu
from .search_subject import search_subject
from .view_subjects import view_subjects
from .update_subject import update_subject
from .delete_subject import delete_subject

def subject_menu():
    return [
        {
            "todo": "Review a subject",
            "match": "review",
            "unmatches": ["add", "search", "view", "update", "delete", "exit"],
            "function": review_subject
        },
        {
            "todo": "Add a subject",
            "match": "add",
            "unmatches": ["review", "search", "view", "update", "delete", "exit"],
            "function": add_subject_menu
        },
        {
            "todo": "Search a subject",
            "match": "search",
            "unmatches": ["review", "add", "view", "update", "delete", "exit"],
            "function": search_subject
        },
        {
            "todo": "View subjects",
            "match": "view",
            "unmatches": ["review", "add", "search", "update", "delete", "exit"],
            "function": view_subjects
        },
        {
            "todo": "Update a subject",
            "match": "update",
            "unmatches": ["review", "add", "search", "view", "delete", "exit"],
            "function": update_subject
        },
        {
            "todo": "Delete a subject",
            "match": "delete",
            "unmatches": ["review", "add", "search", "view", "update", "exit"],
            "function": delete_subject
        },
        {
            "todo": "Exit",
            "match": "exit",
            "unmatches": ["review", "add", "search", "view", "update", "delete"],
            "function": exit
        },
    ]