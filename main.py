# Marvish Chandra
'''This program is intended to determine if a high school student is eligible to pursue a post-secondary program.'''

class collegePlacement:

def studentDemographic(name,age,typeStudent,identity,sexuality,nativeLang):
    name = input("Please enter your full name, including middle name.")
    age = input("Please enter your age.")
    typeStudent = input("Please indicate if you are College Preparatory or Advanced Placement.")
    identity = input("Does your identity describe you as a: woman, man, transgender, non-binary, or different.")
    sexuality = input("Do you consider yourself to be: heterosexual or straight, gay or lesbian, or bisexual, or unlisted.")
    nativeLang = input("What is your native language (first language spoken)?")
    if nativeLang == "English":
        print("No other languages are required.")
    if nativeLang != "English":
        first_lang = input("What language did you first learn growing up?")
        print("My first language is: " + first_lang + ".")
    else: print("Give your native language as it is required to continue the application.")

#Example function call
studentDemographic("Blank",18,"AP","non-binary","unlisted","English")


def parentIncome(askEmployed,current_employed,unemployedStatus,askhighestEducation)
    askEmployed = input("Does your single or dual parent work currently?")
    statusEmployed = {"Employed": "Company"}
    if employed: current_employed = input("Where do you work?")
    print(current_employed)
    else: unemployed = input("How many years have you been unemployed or a stay at home parent?")
    unemployedStatus = unemployed == current_employed
    print(unemployedStatus)
    educationLevels = {"Highest Education":"None","Some high school", "High school graduate", "Some college/University", "Two-year college/University graduate", "Postgraduate study"}
    askhighestEducation = input("What educational qualifications do you have?")
    # enter ask highest edu input
    print("My parent does" + askEmployed + "./n" + "My parent is currently employed at" + current_employed + "./n"" My parent has received this level of education" + askhighestEducation + "./n")
    print("Currently, my parent is unemployed for" + unemployedStatus + ".")


def studentSAT(readingScore,mathScore,writingScore,composite):


    def studentACT(englishScore,mathScore,scienceScore,composite)


        def personalStatements(score):
            if score > 50:
                print("The student has written a personal statement that qualifies failing. ")
            if score > 60:
                print("The student has written a personal statement that qualifies unsatisfactory.")
            if score > 70:
                print("The student has written a personal statement that qualifies as satisfactory.")
            if score > 80:
                print("The student has written a personal statement that qualifies as good.")
            if score > 90:
                print("The student has written a personal statement that qualifies as excellent.")
            else: print("The student has submitted a personal statement that was either incomplete or not submitted at all.")


    def studentGrades(grades)

    def