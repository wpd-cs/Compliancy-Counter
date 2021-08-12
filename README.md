# Compliancy Counter
Keeps count of vaccinated patients using CMS and PNC data.

*Last Updated: 08/12/2021*

## File Naming
***Make sure these files are in the same directory as the executable***
- CSV export from PNC must be named: ***compliance.txt***
- Employee extract from Central IT folder must be named: ***employee.txt***
- Student extract from Central IT folder must be named: ***student.txt***
- Non-state extract from Central It folder must be named: ***nonstate.txt***

## To Make the Executable...
1. Make sure Python is installed on your computer
<ol>- Link to the Python Download Page: https://www.python.org/downloads/</ol>

2. Make sure pyinstaller is installed on your computer (can only be downloaded after Python is installed)
<ol>- Link to instructions on installing Pyinstaller: https://pyinstaller.readthedocs.io/en/stable/installation.html</ol>

3. Navigate to the file directory of ***main.py*** and copy the address

4. In Command Prompt, type ***cd [file address]*** then press Enter

5. Once in the correct directory, type ***pyinstaller --onefile main.py*** then press Enter
<ol>- If unsuccessful at first, repeat step 5 until it is successful</ol>

6. Move the executable file out of the ***dist*** folder into the directory that holds ***dist***

7. Remake the executable file if Windows Antivirus keeps removing the executable
