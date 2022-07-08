# CTTF

Recursively looks for flac files within the current working directory  
Extracts and saves cover.jpg  
Transcodes to mp3 320kbps  
Saves files according to the specified format string  
Keeps original files in "processed"  

## Usage
Create new venv and install dependencies
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Place music in `./music` or run the script within a directory that already holds music  
run cttf.py 
```
$ ./cttf.py
```

