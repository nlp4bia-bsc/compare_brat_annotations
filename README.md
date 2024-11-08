# DESCRIPTION
This programme is designed to compare gold standard annotations in brat format with different predictions.

# HOW TO USE IT?
Clone the respository.
Use your Console and run the following once you are in the folder of the programme: \
&nbsp; $ python3 main.py "your/gold/annotations/folder/path" "your/predictions/annotations/folder/path"

# IMPORTANT NOTES
Input strings must be FOLDER paths with .ann files.
These files must keep the same name in both folders (gold and predictions) for the sake of comparison.
The programme will only compare .ann files, so you can have .conll, .txt and any extension files you want to. They will be ignored by programme.


📂 **Gold Standard Annotations Folder**  
&nbsp;&nbsp;&nbsp;&nbsp;├── file01.ann  
&nbsp;&nbsp;&nbsp;&nbsp;└── file01.txt  

📂 **Predicted Annotations Folder**  
&nbsp;&nbsp;&nbsp;&nbsp;├── file01.ann  
&nbsp;&nbsp;&nbsp;&nbsp;└── file01.txt  


# LICENSE: 
Cite the source, License Apache 2.0.
