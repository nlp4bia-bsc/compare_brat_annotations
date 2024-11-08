from utils.load_and_parse_files import load_annotations
from utils.get_metrics import get_metrics 

def get_unique_entity_mentions(annotations_dict):
    unique_entity_mentions = set()
    for annotations in annotations_dict.values():
        for annotation in annotations:
            entity_mention = (annotation[1])  # (entity type)
            unique_entity_mentions.add(entity_mention)
    return unique_entity_mentions


def compare_annotations_main(gold_folder_path: str, predictions_folder_path: str):
    gold_standard = load_annotations(gold_folder_path)
    predictions = load_annotations(predictions_folder_path)

    print("\n---------------------------------\nINFORMATION on annotations of Gold Standard and Predictions .ann files")
    gold_annotation_counts = sum(len(annotations) for annotations in gold_standard.values())
    pred_annotation_counts = sum(len(annotations) for annotations in predictions.values())
    gold_entities = set()
    for annotations in gold_standard.values():
        for annotation in annotations:
            gold_entities.add(annotation[1]) # annotation[1] is the entity
    
    pred_entities = set()
    for annotations in predictions.values():
        for annotation in annotations:
            pred_entities.add(annotation[1])

    
    print(f"Number of annotations for Gold Standard Annotations: {gold_annotation_counts}")
    print(f"Number of annotations for Predictions: {pred_annotation_counts}")

    print(f"Entities for Gold Standard Annotations: {get_unique_entity_mentions(gold_standard)}")
    print(f"Entities for Predictions: {get_unique_entity_mentions(gold_standard)}")


    print(f"Total number of unique entities in Gold Standard: {len(gold_entities)}")
    print(f"Total number of unique entities in Predictions: {len(pred_entities)}")


    metrics = get_metrics(gold_standard, predictions)
    

    print("\n---------------------------------\nMETRICS SUMMARY:\n")

    print("Overall Metrics:")
    print(f"Exact Match: {metrics['overall']['exact_match']}")
    print(f"Partial Match: {metrics['overall']['partial_match']}")

    print("\nMicro-Averaged Metrics for Exact Match:")
    print(metrics['micro'])
    print("\nPer-Entity Metrics for Exact Match:")
    for entity, metric in metrics['per_entity'].items():
        print(f"\nEntity Type: {entity}")
        print(f"  True Positives: {metric['true_positives']}")
        print(f"  False Positives: {metric['false_positives']}")
        print(f"  False Negatives: {metric['false_negatives']}")
        print(f"  Precision: {metric['precision']:.4f}")
        print(f"  Recall: {metric['recall']:.4f}")
        print(f"  F1 Score: {metric['f1_score']:.4f}")

    print("---------------------------------")