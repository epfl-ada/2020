# ADA Final Exam

This repository contains the final exam for Applied Data Analysis (CS-401).

The questions and the data will be made available to you at 8:15 A.M. on January 12th, 2021 via the the Jupyter Notebook named "exam.ipynb" and the folder named `data`, respectively.

All the logistical details, rules, and guidelines pertaining to exam are stated below. For the mock exam, please see the [mock exam instructions](#Mock-Exam-Instructions) section at the bottom of this document.

## Conda Environment
We have prepared a conda environment, named `adaexam`, with all the Python packages that you might need for the exam. You can install it with the following command:   
`conda env create -f adaexam_crossplatform.yml`   

Once installed, to activate the environment, please use `conda activate adaexam`. To use it in Jupyter, please initiate Jupyter from a terminal with `adaexam` as the active conda environment. Alternatively, you can add the conda environment as a custom kernel by using the following command:   
`ipython kernel install --user --name=adaexam`

*Note: You are of course welcome to install any additional package to the aforementioned conda environment.*

## Timeline
**Exam date:** Tuesday, January 12th, 2021   
**Exam start:** 8:15 A.M. (CET/UTC+1h)   
**Exam end:** 11:15 A.M. (CET/UTC+1h)   
We allow a grace period of 5 minutes for you to submit your solved IPython notebooks. The strict deadline is at 11:20 A.M. **Later submissions will not be accepted!**

## Communication Guidelines
* The following states how we (the teaching staff) will communicate with you (the students):   
   * Please watch the "Announcements" section at the bottom of [this Google document](https://docs.google.com/document/d/186AHQGZ6LnON42ZqWHS6Y_ljcxfcBFqWKFRh-HX01lA/edit?usp=sharing) for updates from our side.

* The following states how we expect you to communicate with us:   
   * If you encounter any problems or have any questions, please contact us via ada-core-assistants-2020@groupes.epfl.ch.    
   * The use of any messaging program (including Zulip) during the exam (with the exception of emails to us) is **strictly forbidden**! Additionally, let us remind you that we will monitor all traffic on Zulip between 8:00 A.M. and 11:30 A.M.
   * For prolonged Internet outages, we have prepared the following phone numbers:
      * +41-779876871
      * +41-783260888   
   You need to have a **reasonable justification** for calling us on phone. For instance, no Internet connectivity for more than 15 minutes qualifies as a reasonable justification.
   * If you are unable to work on the exam, you need to contact us immediately.

## High-level Guidelines and Rules
1. You have to open “exam.ipynb” in Jupyter, edit it, and submit it with your solutions.
2. You have *3 hours* (8:15 -- 11:15) to solve the exam and upload your solved iPython (.ipynb) notebook.
3. We have prepared a conda environment with all the necessary Python packages. If not done already, you can install it with the following command:
`conda env create -f adaexam_crossplatform.yml`
4. You are allowed to use any built-in Python library that comes with Anaconda.
5. You are allowed to use [Google Colab](https://colab.research.google.com/) or [EPFL Noto](https://noto.epfl.ch), however, it's your responsibility to ensure that the required Python packages (see the section [Conda environment](#Conda-environment) for details) are accessbile in the execution environment and platform of choice.
6. There are **three tasks:** A, B, and C, which are further split into several subtasks.
7. The three tasks are **independent** of each other, and you can solve any combination of them.
8. The exam is designed for *more than 3 hours*, so don't worry if you don't manage to solve everything; you can still score a 6!
9. For questions containing the **/Discuss:/** prefix, answer not with code, but with a textual explanation (in markdown).
10. Don't forget to add a textual description of your thought process, the assumptions you made, and your results!
11. Please write all your comments in English, and use meaningful variable names in your code.
12. As we have seen during the semester, data science is all about multiple iterations on the same dataset. We suggest that you not obsess over small details in the beginning, and try to complete as many tasks as possible during the first 2 hours. Then, go back to the obtained results, write meaningful comments, and debug your code if you have found any glaring mistake.
13. Fully read the instructions for each question before starting to solve it to avoid misunderstandings, and remember to save your notebook often!
14. We will **not run your notebook for you**! Rather, we will grade it as is, which means that only the results contained in your evaluated code cells will be considered, and we will not see the results in unevaluated code cells. Thus, be sure to hand in a **fully-run and evaluated notebook**.
15. In continuation to the previous point, interactive plots, such as those generated using `plotly`, should be **strictly avoided**!
16. You can use all the online resources you want except for communication tools (emails, web chats, forums, phone, etc.). 
17. Remember, this is not a homework assignment -- no teamwork allowed!

## Submission
* You will have until 11:20 (strict deadline) to turn in your submission. **Late submissions will not be accepted.**
* For students **with** an EPFL email address:
    * Your file has to be named as "YourSCIPERNumber.ipynb". For example, if your SCIPER number is '123456', please name your file as '123456.ipynb'.   
    **Note-1: We won't grade your exam if the file is not properly named, thus, be extra careful in this regard.**   
    *Note-2: The Google form upload utility might automatically append the name on your EPFL account to the filename provided by you, thus, don't be alarmed if this happens. For instance, if your name on the EPFL account is 'Abc Xyz' and you upload the file '123456.ipynb', it might be renamed to '123456 - Abc Xyz.ipynb*   
    * Upload your Jupyter Notebook (1 file) to [this Google form](https://forms.gle/rDxQYyXQFhFe5X5d7) at the end of the exam, with all the cells already evaluated. You need to **sign in to Google** using your **EPFL credentials** in order to access the form. Please see [this EPFL Wiki](https://wiki.epfl.ch/help-gdrive-en) for more details on how to use Google services via your EPFL credentials.   
    *Note-1: If you get a *'You need permission'* message, then it means you are trying to access the Google form via a non-EPFL account. This can be fixed by opening the submission link in a *private/incognito* window and signing in using your EPFL credentials.*   
    *Note-2: You can correct 'typos' in your name using the "edit response" option, however, the uploaded 'ipynb' file cannot be modified. Make sure to submit the correct 'ipynb' file **only once** you have completely solved the exam.*   
    * In case of problems with the form, send your Jupyter Notebook via email to ada-core-assistants-2020@groupes.epfl.ch. This is reserved only for those who encounter problems with the submission - you need to have a **reasonable justification** for using this backup.
* For students **without** an EPFL email address:
    * Your file has to be named (in *titlecase*) as "YourFirstName_YourLastName.ipynb". For example, if your first name is 'Abc', and last name is 'Xyz', please name your file as 'Abc_Xyz.ipynb'.   
    **Note: We won't grade your exam if the file is not properly named, thus, be extra careful in this regard.**   
    * Send your Jupyter Notebook (1 file) via email to ada-core-assistants-2020@groupes.epfl.ch.

## Mock Exam Instructions
1. Carefully read and familiarize yourself with all the aforementioned rules and instructions.
2. Set up the [conda environment](#Conda-Environment) and make sure you can use it.   
   **Test:** Running `exam.ipynb` in Jupyter should print *'Package import test successful!'* without throwing any errors!
3. Make sure you can access the [Google document](https://docs.google.com/document/d/186AHQGZ6LnON42ZqWHS6Y_ljcxfcBFqWKFRh-HX01lA/edit?usp=sharing) containing the *"Announcements"* section.
4. **[Only for students with an EPFL email address]** Test the [submission](#Submission) utility by submitting your 'ipynb' file using [the Google form](https://forms.gle/rDxQYyXQFhFe5X5d7). On successful submission, you should receive an acknowledgement email from forms-receipts-noreply@google.com.

*Note: If you face any problems in carrying out the aforementioned steps or have any doubts regarding the rules, please reach out to us via Zulip by posting your questions (use meaningful topic categorizations) in the public stream named **#Final exam**.*