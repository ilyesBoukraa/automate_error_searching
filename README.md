# automate_error_searching
As programmers, we often find ourselves facing bugs that we don't understand,
especially in low-level languages such as C. During my learning process, 
I thought of creating a tool to make our lives easier (my life actually). With this tool, 
you only need to copy the error message and then press Windows + R. Next,
type the batch file name (without .bat extension), and the program will open your default web browser,
navigate to Google, and search for the error message you copied!

# To get the program working, you'll need to make some changes. 
First, make sure you have __pyperclip__ installed by running the following command in your terminal or command prompt: <br><br>__pip install pyperclip__ <br><br>
Next, modify the batch file (search_google.bat) as follows (make sure to use pythonw.exe and not python.exe):
<br><br>![batch file](https://github.com/ilyesBoukraa/automate_error_searching/blob/master/batch_file.png)<br><br>
Replace <path_to_search_google.py> with the full path to the search_google.py Python script that you have created for this tool.

Finally, add the directory path where the batch file and the Python script exist into your system's PATH environment variable.
This step will allow you to run the batch file from any location in your terminal or command prompt.

Once you've completed these steps, you're ready to go! Now, when you encounter an error, simply copy the error message,
press Windows + R, type the name of the batch file (without the .bat extension aka type: search), 
<br><br>
![img_run](https://github.com/ilyesBoukraa/automate_error_searching/blob/master/Run.png)
<br><br>
and the program will automatically open your default web browser and perform a Google search for the error message.

<br><br>![batch file](https://github.com/ilyesBoukraa/automate_error_searching/blob/master/searched_an_error.png)<br><br>


# Please note that: 
this tool is a basic implementation, and you can further enhance it to suit your specific needs and preferences.
