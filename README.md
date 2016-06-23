# Stanford-NER-for-Twitter
Understanding NER, attempting to improve accuracy for twitter applications

====FOLDERS OVERVIEW====

Stanford Ner: complete vanilla NER CRF in the folder
Scripts: includes helpful python scripts, including
twitter_streaming.py : streams twitter text to a JSON file
gettext.py: takes an existing JSON twitter file and parses it for the text
confmatrix.py: creates a confusion matrix and benchmark scores of an NER model 



=====TRAINING CRF=======

Document the process of training the NER CRF, ways that it can be 
improved, applications and limitations 

Creating Data: 
1. Get the raw data (I streamed twitter for about a minute into a text file via python). Twitter streams in JSON format, made sure to only stream the raw data (but other data, like user info, could also be used). 
Or, if using a file from Argus, write a quick python script to get just the "text" filed of the JSON file

2. Stanford NER contains an in box tokenizer, important to specify the currect CLASSPATH and include dependencies, run tokenizer on raw data file

java -cp "stanford-ner.jar:./lib/*" edu.stanford.nlp.process.PTBTokenizer twitter_streaming.txt > twitter_streaming.tok


3. Set all entries to O "Nothing", you can do this through various methods, I downloaded perl with 
brew install perl
and then used the following command
perl -ne 'chomp; print "$_\tO\n"' jane-austen-emma-ch1.tok > jane-austen-emma-ch1.tsv


4. Go through manually and change the named entities to their correct categorization

PERS LOC ORG MISC

You are going to need to do this for at least two sets, one to train, the other to test performance. 

5. Train the CRF on this data

6. Evaluate performance by running it on a (different!) pre-classified data set and comparing the output to the 
actual classifications using ConfMatrix.py

====Improving Performance?=====

Combining classifiers (the first with tag everything it can, the second with tag anything the first didnt, ect), Train specific classifers to catch those cases then combine 


