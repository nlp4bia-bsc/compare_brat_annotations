
from typing import Dict, Tuple,List, Any
from collections import defaultdict


# Type definitions
AnnotationEntry = Tuple[str, str, Tuple[int, int], str]  # (term_id, entity, (start, end), text)
AnnotationsDict = Dict[str, List[AnnotationEntry]]  # file_id -> list of annotations

Metrics = Dict[str, float]  # Dictionary for metrics: precision, recall, f1



# Exact match counter using set intersections
def count_exact_matches(gold_terms: List[AnnotationEntry], pred_terms: List[AnnotationEntry]) -> int:
    gold_set = {(entry[1], entry[2], entry[3]) for entry in gold_terms}  # (entity, span, text)
    pred_set = {(entry[1], entry[2], entry[3]) for entry in pred_terms}
    return len(gold_set & pred_set)  # Intersection for exact matches

# Partial match counter
def count_partial_matches(gold_terms: List[AnnotationEntry], pred_terms: List[AnnotationEntry]) -> int:
    partial_matches = 0
    gold_dict = {(entry[1], entry[2]): entry[3] for entry in gold_terms}  # (entity, span) -> text
    for pred in pred_terms:
        key = (pred[1], pred[2])  # (entity, span)
        if key in gold_dict and pred[3] in gold_dict[key]:  # Check if pred text is found in gold text
            partial_matches += 1
    return partial_matches

# Calculate precision, recall, and F1 score
def calculate_metrics(true_positive: int, total_pred: int, total_gold: int) -> Metrics:
    precision = true_positive / total_pred if total_pred else 0
    recall = true_positive / total_gold if total_gold else 0
    f1_score = (2 * precision * recall) / (precision + recall) if precision + recall else 0
    return {"precision": precision, "recall": recall, "f1_score": f1_score}

# Calculate micro averaged precision, recall, and F1
def calculate_micro_metrics(gold_standard: AnnotationsDict, predictions: AnnotationsDict) -> Metrics:
    total_true_positive = 0
    total_gold = sum(len(terms) for terms in gold_standard.values())
    total_pred = sum(len(terms) for terms in predictions.values())

    for file_id, gold_terms in gold_standard.items():
        pred_terms = predictions.get(file_id, [])
        total_true_positive += count_exact_matches(gold_terms, pred_terms)

    return calculate_metrics(total_true_positive, total_pred, total_gold)




# New function to calculate per-entity metrics
def calculate_per_entity_metrics(gold_standard: AnnotationsDict, predictions: AnnotationsDict) -> Dict[str, Dict[str, float]]:
    entity_counts = defaultdict(lambda: {'true_positives': 0, 'false_positives': 0, 'false_negatives': 0})

    for file_id in gold_standard:
        gold_terms = gold_standard[file_id]
        pred_terms = predictions.get(file_id, [])

        gold_entities = defaultdict(set)
        for entry in gold_terms:
            entity = entry[1]
            span_text = (entry[2], entry[3])
            gold_entities[entity].add(span_text)

        pred_entities = defaultdict(set)
        for entry in pred_terms:
            entity = entry[1]
            span_text = (entry[2], entry[3])
            pred_entities[entity].add(span_text)

        all_entities = set(gold_entities.keys()) | set(pred_entities.keys())

        for entity in all_entities:
            gold_set = gold_entities.get(entity, set())
            pred_set = pred_entities.get(entity, set())

            tp = len(gold_set & pred_set)
            fp = len(pred_set - gold_set)
            fn = len(gold_set - pred_set)

            entity_counts[entity]['true_positives'] += tp
            entity_counts[entity]['false_positives'] += fp
            entity_counts[entity]['false_negatives'] += fn


    # Compute precision, recall, and F1 score for each entity type
    entity_metrics = {}
    for entity, counts in entity_counts.items():
        tp = counts['true_positives']
        fp = counts['false_positives']
        fn = counts['false_negatives']

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        entity_metrics[entity] = {
            'true_positives': tp,
            'false_positives': fp,
            'false_negatives': fn,
            'precision': precision,
            'recall': recall,
            'f1_score': f1_score
        }

    return entity_metrics
