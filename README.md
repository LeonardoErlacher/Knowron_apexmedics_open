# Welcome to Apexmedics
![Alt Text](Apexmedics.png)

## Get started 
Install the requierments.txt using 
```python
pip install -r requirements.txt
```
It's recommended to use Python 3.10.

In the confiq.json you find alle change able parameters. Please don't change the parameters if aren't sure you know what you are doing.
The gui should be the main interaction hub.
* RECORD_TIME how long the recording should run
* MAX_TOKENS the maximal result of ChatGPT 3.5 do not exceed 3000
* API_KEY the Api key for ChatGPT. This is present only for demonstration purpose you are not allowed to use it privat.
* FILENAME where the recorded audio file will be stored. If you want to use the sample files change the name to that, 
but keep in mind that you need to untick the new Record option in the Gui in order to not overwrite it. 

## GUI
![Alt Text](GUI Picture.png)

The gui has in the first line a button, this button displays Record if you start.<br>
If you untick the checkbox new Recording, the button displays Ask Ai.
* If you press Record it will display a red dot indication that recording is in Progress. Pls choose a recording time below 90 seconds.
* If you press Ask AI the programm will take the existing .wav file and proceed with that further.

<br> The dropdown under the checkbox specify what solution the AI should generate. 

* Bulletpoints
* A Protocol over the discussed medical examination
* A letter for the patient he can bring to the next doctor (Facharzt) or his health insurance.

The next field is the multi functional text field.
* You can enter names after the >>> that will be removed if they appear in the Dialog to insure privacy
* After the generation you can change the text. Maybe add things you thought but not said or correct things.

### The export
You can export the text field in three different ways. 
* copy it to the clipboard (you can insert it after that with crtl-v)
* export it via PDF format
* opens your mail programm and send it to the patient another doctor or the insurance.

Keep in mind you need to choose you option and that press the Export button.

## Notes
Make sure you have a microphone connected with one input channel (mono) if you want to record. If you don't have mono change this in file record.py line 10 channel=2 so you can record stereo.<br> 
Make sure you have an internet connection. 

