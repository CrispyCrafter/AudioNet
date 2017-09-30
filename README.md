# AudioNet
AudioNet is a collection of wav format audiosamples acquired from processing creative commons audio features freesound.org.

## Description
AudioNet aims to be a high quality training set for audio event detection. As of now the dataset is still under review, meaning misclassified audio files are still present. Files are arranged in folder main format, although plans to migrate to a WordNet style formatting is anticipated.

To help arrange and review each datalabel I have included a simple PyGame Python script which plays and prompts the validity of each audio sample. Ideally this could be run from a Jupyter Notebook for ease of navigation. To utilize SoundReview from Jupyter, navigate to the audio directory and initialise Run for each file in the current folder 

### Requirements:
* jupyter
* ipython3
* pygame

### Audio Format
* All files are between 1000 and 2000 ms of length
* All files are single channel little Endian format at 16000 Hz sampling rate
* Files were processed as follows using ffmpeg:
```
ffmpeg -i Foo.bar -c:a pcm_s16le -ar 16000 -ac 1 Foo.wav
```
### Audio Acquisition and Aknowledgements
*The scripts used to acquire and isolate the most relevant audio segments will be added soon.*
Dataset was partially populated by the [ESC-50 Dataset](https://github.com/karoldvl/ESC-50)
