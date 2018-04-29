# googleHomeProject
## Initiliazing
To start using the code, download the zip and extract it anywhere. Or you can use git!
	
`git clone https://github.com/gtairpline/googleHomeProject.git`
	
You will also need to download the dependencies using:
	
`pip install numpy matplotlib scipy sklearn hmmlearn simplejson eyed3 pydub `

	
_psst_ you can also use `pip install pyAudioAnalysis` but that doesn't always work that well :/
	
 ## Running
 By now, you should have the files some on your computer, probably the directory you downloaded the files in or invoked the `git clone` command in.
 There should be a folder with trainingData wav files. As you can see there are _categories_ and inside those you can find _files_! (woah).
 The _categories_ folder should be named respectively to what the files inside are for. Make sure you have atleast more than 2 samples in each _category_ folder. I recommend between 3-5 samples.
 
 Now, we can start working! Run this in the command line:
 
 `python buildModel.py *trainingDataFolder*`
 
 After building the model, you can go ahead and test it out by running 
 
 `python testModel.py *testFileDirectory*` Your test file directory should be something like this: 
 
 >folderName/file.wav
 
 ## Troubleshooting
 
 Nothing as of now. Check back later or contact me.
