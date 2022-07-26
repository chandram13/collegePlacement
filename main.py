# Marvish Chandra
'''This program is intended to determine if a high school student is eligible to pursue a post-secondary program.'''

class collegePlacement:

def studentDemographic(name,age,identity,sexuality,nativeLang,parentIncome):
    name = input("Please enter your full name, including middle name.")
    age = input("Please enter your age.")
    typeStudent = input("Please indicate if you are College Preparatory or Advanced Placement.")
    identity = input("Does your identity describe you as a: woman, man, transgender, nonbinary, or different.")
    sexuality = input("Do you consider yourself to be: heterosexual or straight, gay or lesbian, or bisexual, or unlisted.")
    nativeLang = input("What is your native language (first language spoken)?")
    if nativeLang == "English":
        print("No other languages are required.")
    if nativeLang != "English":
        first_lang = input("What language did you first learn growing up?")
        print(first_lang)
    else: print("Give your native language as it is required to continue the application.")

def parentIncome(employed,highestEducation)
    employed = {"Employed": "Company"}
    highestEducation = {"Highest Education":"None","Some high school","High school graduate","Some college/University","Two-year college/University graduate","Postgraduate study"}
    


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