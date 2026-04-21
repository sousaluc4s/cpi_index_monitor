# cli.py
import argparse
from cpi_index_monitor.runner import run_cpi

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "source",
        choices=["cpi"],
        help="Source to run"
    )

    args = parser.parse_args()

    if args.source == "cpi":
        run_cpi()