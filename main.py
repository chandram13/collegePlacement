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
    print("Currently, my parent is unemployed for" + unemployedStatus + "./n")


def studentSAT(ebrwScore,mathScore,composite):
    ebrwScore = input("Please enter your total reading and writing score you received on the SAT.")
    print(askReadingScore)
    if ebrwScore 300 > 200:
        print("Your performance is in the negative quartile of -1.")
    if ebrwScore 400 > 300:
        print("Your performance is in the quartile range of 1 to 11.")
    if ebrwScore 500 > 420:
        print("Your performance is in the quartile range of 11 to 41.")
    if ebrwScore 600 > 520:
        print("Your performance is in the quartile range of 48 to 73.")
    if ebrwScore 700 > 620:
        print("Your performance is in the quartile range of 78 to 94.")
    if ebrwScore 800 > 720:
        print("Your performance is in the quartile range of 96 to 99 and above.")
    else: print("Please enter a valid input for your reading and writing score.")

    mathScore = input("Please enter your total math score you received on the SAT.")
    print(mathScore)
    if mathScore 300 > 200:
        print("Your performance is in the negative quartile of -1.")
    if mathScore 400 > 300:
        print("Your performance is in the quartile range of 1 to 16.")
    if mathScore 500 > 420:
        print("Your performance is in the quartile range of 20 to 43.")
    if mathScore 600 > 520:
        print("Your performance is in the quartile range of 50 to 75.")
    if mathScore 700 > 620:
        print("Your performance is in the quartile range of 75 to 91.")
    if mathScore 800 > 720:
        print("Your performance is in the quartile range of 93 to 99 & above.")
    else: print("Please enter a valid input for your math score.")

# Calculated composite score then evaluates quartile range
    composite = ebrwScore + mathScore
    yourComposite = "Your total composite score is" + str(composite) + "./n"
    print(yourComposite)

    if composite 600 > 400:
        print("Your performance is in the negative quartile of -1.")
    if composite 800 > 600:
        print("Your performance is in the quartile range of -1 to 19.")
    if composite 1000 > 800:
        print("Your performance is in the quartile range of 19 to 42.")
    if composite 1200 > 1000:
        print("Your performance is in the quartile range of 42 to 74.")
    if composite 1400 > 1200:
        print("Your performance is in the quartile range of 74 to 93. ")
    if composite 1600 > 1400:
        print("Your performance is in the quartile range of 93 to 99 & above.")
    else: print("Please enter a valid input for your composite score.")

def studentACT(englishScore,mathScore,readingScore,scienceScore,composite):
        englishScore = input("Please enter your total english score.")
        print(englishScore)
        if englishScore 10 > 1:
            print("Your english score percentile is between 1 to 7.")
        if englishScore 20 > 11:
            print("Your english score percentile is between 11 to 55.")
        if englishScore 30 > 21:
            print("Your english score percentile is between 60 to 89.")
        if englishScore 36 > 31:
            print("Your english score percentile is between 91 to 100.")
        else: print("Please enter a valid input for your english score.")

        mathScore = input("Please enter your total math score.")
        print(mathScore)
        if mathScore 10 > 1:
            print("Your math score percentile is between 1 to 3.")
        if mathScore 20 > 11:
            print("Your math score percentile is between 1 and 58.")
        if mathScore 30 > 21:
            print("Your math score percentile is between 61 and 94.")
        if mathScore 36 > 31:
            print("Your math score percentile is between 96 and 100.")
        else: print("Please enter a valid input for your math score.")

        readingScore = input("Please enter your total reading score.")
        print(readingScore)
        if readingScore 10 > 1:
            print("Your reading score percentile is between 1 to 3.")
        if readingScore 20 > 11:
            print("Your reading score percentile is between 5 to 50.")
        if readingScore 30 > 21:
            print("Your reading score percentile is between 55 to 86.")
        if readingScore 36 > 31:
            print("Your reading score percentile is between 89 to 100.")
        else: print("Please enter a valid input for your reading score.")

        # Calculated composite score based on the three scores: English, Math, and Reading
        composite = englishScore + mathScore + readingScore
        yourComposite = "Your total composite score" + str(composite) +"./n"
        print(yourComposite)

        if composite 10 > 1:
            print("Your total composite score is in quartile 1.")
        if composite 20 > 11:
            print("Your total composite score's quartile is between 2 and 53.")
        if composite 30 > 21:
            print("Your total composite score's quartile is between 59 to 93.")
        if composite 36 > 31:
            print("Your total composite score's quartile is between 95 and 100.")
        elif composite == 0:
            print("Please enter a valid input above 1 for your composite score, as your score is invalid.")
        else: print("Please enter a valid input for your composite score.")

def personalStatements(score):
            if score > 50:
                print("The student has written a personal statement that qualifies failing.")
            if score > 60:
                print("The student has written a personal statement that qualifies as unsatisfactory.")
            if score > 70:
                print("The student has written a personal statement that qualifies as satisfactory.")
            if score > 80:
                print("The student has written a personal statement that qualifies as good.")
            if score > 90:
                print("The student has written a personal statement that qualifies as excellent.")
            else: print("The student has submitted a personal statement that was either incomplete or not submitted at all.")


def studentGrades(GPA):
    GPA = input("Please enter a valid unweighted GPA value between 1.0 and 4.0.")
    if GPA > 1.0:
        print("You are currently failing high school. Increase your grades as much as you can and consider pursuing an adult school.")
    if GPA > 2.0:
        print("You have a low GPA. To increase your chances at a good post-secondary program, increase your grades and do well on the standardized exams.")
    if GPA > 3.0:
        print("You have a decent chance to enter a good post-secondary program.")
    if GPA 4.0 > 3.5:
        print("You have a high chance to enter an excellent post-secondary program.")
    else: print("Please enter a valid GPA to determine your performance in high school.")

