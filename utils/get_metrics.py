
from typing import Dict, Tuple,List, Any
from utils.metric_functions import count_exact_matches, count_partial_matches, calculate_metrics, calculate_micro_metrics, calculate_per_entity_metrics


# Type definitions
AnnotationEntry = Tuple[str, str, Tuple[int, int], str]  # (term_id, entity, (start, end), text)
AnnotationsDict = Dict[str, List[AnnotationEntry]]  # file_id -> list of annotations

Metrics = Dict[str, float]  # Dictionary for metrics: precision, recall, f1


# Main function to calculate overall and per entity metrics
def get_metrics(gold_standard: AnnotationsDict, predictions: AnnotationsDict) -> Dict[str, Any]:
    # Calculate exact and partial matches across all files
    total_exact_matches = sum(count_exact_matches(gold_standard[file_id], predictions.get(file_id, []))
                              for file_id in gold_standard)
    total_partial_matches = sum(count_partial_matches(gold_standard[file_id], predictions.get(file_id, []))
                                for file_id in gold_standard)
    total_gold = sum(len(gold_terms) for gold_terms in gold_standard.values())
    total_pred = sum(len(pred_terms) for pred_terms in predictions.values())

    # Calculate overall metrics
    overall_metrics = {
        "exact_match": calculate_metrics(total_exact_matches, total_pred, total_gold),
        "partial_match": calculate_metrics(total_partial_matches, total_pred, total_gold)
    }
    
    # Calculate micro-averaged metrics
    micro_metrics = calculate_micro_metrics(gold_standard, predictions) ## Considering exact matches! 

    # Calculate per-entity metrics
    entity_metrics = calculate_per_entity_metrics(gold_standard, predictions) ## Considering exact matches! 

    return {
        "overall": overall_metrics,
        "micro": micro_metrics,
        "per_entity": entity_metrics
    }