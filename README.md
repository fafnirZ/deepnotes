# deepnotes
indexes and clusters semantically similar markdown files


# POC requirements
- assumes markdown files / txt files
- assumes for each file a model will output a set of keywords, this will be stubbed and can be changed according to model the user wants to use.
- keywords will be preprocessed, i.e. lower-cased
- generate an UndirectedGraph by clustering all files with same words using some algorithm to appropriately construct distances from one file to another.
- display graph on a webpage or something (visualise)


## POST POC
- easily search within graph
- incremental builds? 


