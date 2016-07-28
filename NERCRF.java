import edu.stanford.nlp.ie.crf.*;
import edu.stanford.nlp.ie.*; 
import edu.stanford.nlp.io.IOUtils;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.Annotator;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.sequences.DocumentReaderAndWriter;
import edu.stanford.nlp.util.StringUtils;
import edu.stanford.nlp.util.Triple;
import edu.stanford.nlp.sequences.SeqClassifierFlags;
import edu.stanford.nlp.ling.CoreLabel; 
import edu.stanford.nlp.util.CoreMap;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;


import com.aliasi.util.Arrays;


/**Program that takes the output of the Omniscience chunker and runs chained Stanford NER classifers for 4 class tagging**/

public class NERCRF{

	public static void main(String[] args) throws ClassCastException, ClassNotFoundException, IOException{

		//Create last CRF in chain from sample data:
		ArrayList<String> arguments = new ArrayList<String>();
		for(String s : args){arguments.add(s);}

		if(args.length>0){
			Properties chainprop = null;
			Properties prop = null;
			String trained = null;
			AbstractSequenceClassifier<CoreLabel> classifier=null;
			if(arguments.contains("-train")){
				//first load the properties file (contains link to data set)
				try{
					prop=StringUtils.propFileToProperties(arguments.get(arguments.indexOf("-train")+1));
				}catch (IllegalArgumentException ex){
					System.out.println("Invalid Properties File");
				}

				//create a new Sequence Classifier from the prop file, contains features from the prop file
				SeqClassifierFlags flags = new SeqClassifierFlags(prop);
				//Create CRF from the above classifier flags
				CRFClassifier<CoreLabel> crf = new CRFClassifier<CoreLabel>(flags);
				//Train the new CRF
				crf.train();
				//save newly trained classifier
				trained = "classifiers/model.ser.gz";
				//serialize to this file path
				crf.serializeClassifier(trained);
			}

			if(arguments.contains("-chain")){
				try{
					chainprop=StringUtils.propFileToProperties(arguments.get(arguments.indexOf("-chain")));
				}catch (IllegalArgumentException ex){
					System.out.println("Invalid Properties File");
				}		
				String modelNames = chainprop.getProperty("ner.model");
				assert modelNames != null & !(modelNames.isEmpty());
				String[] propmodels=modelNames.split(",");
				String[] models= new String[3];
				if(trained!=null){
					ArrayList<String> modellist = new ArrayList<String>();
					for(int x=0;x<2;x++){
						modellist.add(propmodels[x]);
					}
					modellist.add(trained);
					models=(String[]) modellist.toArray();

				}else{
					models=propmodels;
				}

				NERClassifierCombiner nerCombiner = new NERClassifierCombiner(false, false, chainprop, models);
				classifier = nerCombiner;
			}

			if(arguments.contains("classify")){

				String fileContents = IOUtils.slurpFile(arguments.get(arguments.indexOf("classify")+1));
				String nextString= IOUtils.slurpFile(arguments.get(arguments.indexOf("classify")+2));
				File nextStr = new File(nextString);


				if(nextStr.isFile()){
					classifier = CRFClassifier.getClassifier(nextString);
				}

				List<List<CoreLabel>> out = classifier.classify(fileContents);
				for (List<CoreLabel> sentence : out) {
					for (CoreLabel word : sentence) {
						System.out.print(word.word() + '/' + word.get(CoreAnnotations.AnswerAnnotation.class) + ' ');
					}
					System.out.println();
				}

			}
		}

	}
}