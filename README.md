# 🗒️ DESCRIPTION
This programme is designed to compare gold standard annotations in brat format with different predictions.

# ❓ HOW TO USE IT?
Clone the respository.
Use your Console and run the following once you are in the folder of the programme: \
&nbsp; $ python3 main.py "your/gold/annotations/folder/path" "your/predictions/annotations/folder/path"

# ⚠️ IMPORTANT NOTES
Input strings must be FOLDER paths with .ann files.
These files must keep the same name in both folders (gold and predictions) for the sake of comparison.
The programme will only compare .ann files, so you can have .conll, .txt and any extension files you want to. They will be ignored by programme.

See sample_input_data
📂 **Gold Standard Annotations Folder**  
&nbsp;&nbsp;&nbsp;&nbsp;├── file01.ann  
&nbsp;&nbsp;&nbsp;&nbsp;└── file01.txt  

📂 **Predicted Annotations Folder**  
&nbsp;&nbsp;&nbsp;&nbsp;├── file01.ann  
&nbsp;&nbsp;&nbsp;&nbsp;└── file01.txt  

# ℹ️ EXPECTED OUTPUT
```
Starting programme
 Computing metrics for:
"your/gold/annotations/folder/path" 
AND
"your/predictions/annotations/folder/path"

---------------------------------
INFORMATION on annotations of Gold Standard and Predictions .ann files

Number of annotations for Gold Standard Annotations: 1
Number of annotations for Predictions: 1
Entities for Gold Standard Annotations: {'SINTOMA'}
Entities for Predictions: {'SINTOMA'}
Total number of unique entities in Gold Standard: 1
Total number of unique entities in Predictions: 1

---------------------------------
METRICS SUMMARY:

Overall Metrics:
Exact Match: {'precision': 1.0, 'recall': 1.0, 'f1_score': 1.0}
Partial Match: {'precision': 1.0, 'recall': 1.0, 'f1_score': 1.0}

Micro-Averaged Metrics for Exact Match:
{'precision': 1.0, 'recall': 1.0, 'f1_score': 1.0}

Per-Entity Metrics for Exact Match:

Entity Type: SINTOMA
  True Positives: 1
  False Positives: 0
  False Negatives: 0
  Precision: 1.0000
  Recall: 1.0000
  F1 Score: 1.0000
---------------------------------
```

# ©️ LICENSE: 
Cite the source, License Apache 2.0.
