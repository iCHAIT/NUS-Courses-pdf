## NUS-Courses-pdf

This project scrapes all the relevant information for the courses offered for Master's in CS at NUS and dumps it into a PDF.

## Why?

There were number of web pages that needed to be traversed for going through all course information and stuff.
I wanted all this info at once place so that I don't have to navigate between multiple chrome tabs and more imortantly I can share the info with Shadab for discussion.


## Workflow

### Run `course_list.py`

* Requests desired page - `https://mysoc.nus.edu.sg/~postgd/LecturePreview.html` that contain master list of courses that'll be offered this sem.
* Parse html obtained from above and get intermediate IVLE links for each course -  
Eg. - `https://ivle.nus.edu.sg/lms/list_course.aspx?code=CS4211&acadyear=2017/2018`
* Store all these intermediate links in a file - `ivle_links.txt`


### Run `courses_desc.py`

* Read `ivle_links.txt` and extract final url for each course that contains all the information.
Eg. - `https://ivle.nus.edu.sg/Module/Student/default.aspx?CourseID=BE4CE92A-0E2C-4160-91BB-F26912239937&ClickFrom=StuViewBtn`
* Store all course final links to a new file - `final_links.txt`

### Run `download_info.py`

* Read all final links from `final_links.txt`
* Extract the most sane parent div tag and all its relevant content
* Dump div tags of all courses to a master html file


### Convert html to pdf using pandoc

Finally, convert master html file to pdf via pandoc -

```bash
$ pandoc NUS-SOC-Courses.html NUS-SOC-Courses.pdf
```


### TODO


* Not able to convert html to pdf via pandoc, issues with tex file :(
* Find a way to merge course information and respective slides - Should be doable..!!
* On the IVLE portal, information does not exist for some of the modules,check with seniors.
* If information for some course does not exist, fetch it from course catalogue? - Would be tough anyway.
* Merge course schedule with respective course - Tough!!
* Code Improvements

