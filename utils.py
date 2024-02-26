from pathlib import Path
import os
import json

GT_FILE = Path(os.path.join(os.path.dirname(__file__), 'GT'))
RESULTS_PATH = Path(os.path.join(os.path.dirname(__file__), 'Tickets'))

def jsons_to_jsonl(jsons_path: Path, jsonl_path: Path) -> None:
    """Converts a folder with json files to a single jsonl file."""
    with open(jsonl_path, 'w') as jsonl:
        for json_file in jsons_path.glob("*.json"):
            
            with open(json_file, 'r') as file:
                text = json.load(file)
                metadata = json.dumps({'text': text, 'file_name': json_file.name.split("-")[0]+".jpg"})
                jsonl.write(metadata + "\n")

if __name__ == "__main__":
    jsons_to_jsonl(GT_FILE, RESULTS_PATH.joinpath("metadata.jsonl"))
