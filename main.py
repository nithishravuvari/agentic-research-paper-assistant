# main.py
import argparse
from src.agentic_rag import run_agentic_rag
from src.pretty_printer import pretty_print

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, default="detailed", choices=["detailed", "concise", "comparison"])
    parser.add_argument("--rich", action="store_true", help="Pretty print output in terminal with Rich")
    args = parser.parse_args()

    query = "What are the main challenges and recent advances in Graph Neural Networks?"

    answer = run_agentic_rag(query, mode=args.mode)

    if args.rich:
        print("\n=== Agentic RAG Answer (Rich Mode) ===\n")
        pretty_print(answer, mode=args.mode)
    else:
        print(f"\n=== Agentic RAG Answer ({args.mode.capitalize()}) ===\n")
        print(answer)




