from .review_subject import review_subject
from .add_subject import add_subject
from .search_subject import search_subject
from .view_subject import view_subject
from .update_subject import update_subject
from .delete_subject import delete_subject

def search_menu():
    return [
        { 
            "match": "review",
            "unmatches": ["add", "search", "view", "update", "delete", "exit"],
            "function": review_subject
        },
        { 
            "match": "add",
            "unmatches": ["review", "search", "view", "update", "delete", "exit"],
            "function": add_subject
        },
        { 
            "match": "search",
            "unmatches": ["review", "add", "view", "update", "delete", "exit"],
            "function": search_subject
        },
        { 
            "match": "view",
            "unmatches": ["review", "add", "search", "update", "delete", "exit"],
            "function": view_subject
        },
        { 
            "match": "update",
            "unmatches": ["review", "add", "search", "view", "delete", "exit"],
            "function": update_subject
        },
        { 
            "match": "delete",
            "unmatches": ["review", "add", "search", "view", "update", "exit"],
            "function": delete_subject
        },
        { 
            "match": "exit",
            "unmatches": ["review", "add", "search", "view", "update", "delete"],
            "function": exit
        },
    ]
    
