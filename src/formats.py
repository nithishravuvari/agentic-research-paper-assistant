# src/formats.py

from typing import Union, List


def format_references(ref_list: list) -> list:
    """
    Safely formats references into a list of strings for Rich/Markdown printing.
    Ensures each reference is a string (joins lists/tuples if needed).
    """
    formatted_refs = []
    for r in ref_list:
        if isinstance(r, str):
            formatted_refs.append(r.strip())
        elif isinstance(r, (list, tuple)):
            formatted_refs.append(" ".join(str(el).strip() for el in r))
        else:
            formatted_refs.append(str(r).strip())
    return formatted_refs


def format_answer(answer: Union[str, dict], mode: str = "detailed") -> dict:
    """
    Formats the answer depending on mode.
    Always returns a dict with keys:
      - 'content' : main text
      - 'references' : list of references
    """
    if isinstance(answer, str):
        content = answer
        references = []
    else:
        content = answer.get("content", "")
        references = answer.get("references", [])

    return {
        "content": content.strip(),
        "references": format_references(references)
    }
