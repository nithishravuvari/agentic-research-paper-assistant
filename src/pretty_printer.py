# src/pretty_printer.py
from rich.console import Console, Group
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table

console = Console()


def pretty_print(answer: dict, mode: str = "detailed"):
    """
    Pretty prints the answer using Rich for better readability.
    Expects `answer` to be a dict with keys:
        - 'content' : str
        - 'references' : list of str
    """
    content = answer.get("content", "")
    references = sorted(set(answer.get("references", [])))  # remove duplicates

    # Build markdown for content
    md_content = Markdown(content)

    # Build references if present
    refs_md = None
    if references:
        refs_md = Markdown(
            "\n\n**References:**\n" + "\n".join(f"- {r}" for r in references)
        )

    if mode == "comparison":
        # If table-like structure exists, render table, else fallback to Markdown
        if "|" in content and "---" in content:
            rows = [row.strip() for row in content.split("\n") if row.strip()]
            headers = [h.strip() for h in rows[0].split("|") if h.strip()]
            table = Table(show_header=True, header_style="bold magenta")
            for h in headers:
                table.add_column(h)
            for row in rows[2:]:  # skip header + separator
                table.add_row(*[c.strip() for c in row.split("|") if c.strip()])
            body = table
        else:
            body = md_content

        if refs_md:
            console.print(
                Panel(
                    Group(body, refs_md),
                    title="Comparison Result",
                    border_style="blue",
                    expand=True,
                )
            )
        else:
            console.print(
                Panel(body, title="Comparison Result", border_style="blue", expand=True)
            )

    elif mode == "concise":
        if refs_md:
            console.print(
                Panel(
                    Group(md_content, refs_md),
                    title="Concise Summary",
                    border_style="green",
                    expand=True,
                )
            )
        else:
            console.print(
                Panel(md_content, title="Concise Summary", border_style="green", expand=True)
            )

    else:  # detailed
        if refs_md:
            console.print(
                Panel(
                    Group(md_content, refs_md),
                    title="Detailed Answer",
                    border_style="magenta",
                    expand=True,
                )
            )
        else:
            console.print(
                Panel(md_content, title="Detailed Answer", border_style="magenta", expand=True)
            )
