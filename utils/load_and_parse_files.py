import os
from typing import List, Dict, Tuple, Generator
from collections import defaultdict

# Type definitions
AnnotationEntry = Tuple[str, str, Tuple[int, int], str]  # (term_id, entity, (start, end), text)
AnnotationsDict = Dict[str, List[AnnotationEntry]]  # file_id -> list of annotations

# Parse annotation files
def parse_annotation_file(filepath: str) -> Generator[AnnotationEntry, None, None]:
    """
    Parses a single annotation file --> get each entry as a tuple.
    Expected BRAT format per line: term_id, entity start end, text 
    """
    with open(filepath, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            parts = line.strip().split('\t')
            if len(parts) != 3:
                print(f"Skipping line {line_num} in {filepath}: expected 3 parts, got {len(parts)}")
                continue
            
            try:
                term_id = parts[0] 
                type_and_offsets = parts[1]
                text = parts[2]
                
                # Parse entity and offsets
                type_and_offsets_parts = type_and_offsets.split()
                entity = type_and_offsets_parts[0]
                start = int(type_and_offsets_parts[1])
                end = int(type_and_offsets_parts[2])
                
                yield (term_id, entity, (start, end), text)
            except ValueError as e:
                print(f"Error parsing line {line_num} in {filepath}: {e}")
                continue

# Unified function to load annotations from folder (retrieved from args in main.py)
def load_annotations(folder_path: str) -> AnnotationsDict:
    """
    Loads all .ann annotation files from the specified folder.
    Returns a dictionary with file_id as keys and lists of annotations as values.
    """
    annotations = {}
    for filename in os.listdir(folder_path):
        if not filename.endswith('.ann'):  # Only process .ann files
            continue
        filepath = os.path.join(folder_path, filename)
        file_id = os.path.splitext(filename)[0]  # remove extension
        annotations[file_id] = list(parse_annotation_file(filepath))
    return annotations
