import random
from pptx import Presentation
#import GUI as user_interface
study_sentences=[]
study_sentences_filled=[]
current_label=""
index=0
study_answer=[]
missed=[]
missed_filled=[]
valuesChecked=[]
study_sentences_filled_revised=[]
study_sentences_revised=[]
def convert_presentation(thisFile, thisBlankIntensity):
    global study_sentences_filled_revised
    global study_sentences_revised
    text_runs=[]#Instantiate the array that will store each sentence
    prs = Presentation(thisFile)#Load the presentation
    checkList=["the", "is", "a", "as", "of", "and", "or"]#Values in this list will not be converted into blanks
    file_split_string=""#will be used to join the words in the sentence back together
    for slide in prs.slides:#Go through each slide
        for shape in slide.shapes:#Go through each section
            if not shape.has_text_frame:#If it's not a text-frame
                continue#don't go through the rest of the program

            for paragraph in shape.text_frame.paragraphs:
                file_split=[]
                paragraph_text=""
                study_sentences_filled_text=""
                study_sentences_text=""
                for run in paragraph.runs:

                    text_runs.append(run.text)
                    study_sentences_filled_text+=(run.text.encode('ascii', 'ignore').decode('ascii'))         
                    file_split=run.text.split()
                    for a in range(len(file_split)-1):
                        for b in checkList:
                            if file_split[a]==b:
                                continue  
                        #if (random.randint(0, round(len(file_split[a])/int(thisBlankIntensity)))==0):
                        if (random.randint(0, round((10/len(file_split[a])))*int(thisBlankIntensity))==0):
                        
                            file_split[a]="____"
                    file_split_string=" ".join(file_split)
                    study_sentences_text+=file_split_string
                    paragraph_text+=file_split_string
                study_sentences.append(study_sentences_text)
                study_sentences_filled.append(study_sentences_filled_text)
                paragraph.text=paragraph_text
    print(study_sentences)
    study_sentences_revised=study_sentences
    study_sentences_filled_revised=study_sentences_filled
    newFileString=""
    for i in range(len(thisFile)-1):
        if (len(thisFile)-1)-i>4:
            newFileString+=thisFile[i]
    newFileString+="_blanks.pptx"
    print(newFileString)
    prs.save(str(newFileString))
'''def question_check(i):
    global index
    if i in valuesChecked:

        print("Index selected: " + str(i) + " valuesChecked: " + str(valuesChecked))
        print("This value has already occured")
        index=random.randint(0, len(study_sentences)-1)
        question_check(index)
        '''
def study_blanks():
    global current_label
    global study_answer
    global study_sentences
    global index
    global study_sentences_revised
    study_answer=[]
    current_label=""
    current_label_local=""
    if(len(study_sentences_revised)!=0):
        index=random.randint(0, len(study_sentences_revised)-1)
        print(index)
        '''print("******")
        print(index)
        print(valuesChecked)
        print("******")
        question_check(index)

        print(index)'''
        study_answer_split=study_sentences_filled_revised[index].split()

        #for i in study_sentences:
        index_split=study_sentences_revised[index].split()
        for a in range(0, len(index_split)-1):
            current_label_local+=index_split[a] + " "

            if index_split[a] =="____" and len(study_answer)<=3:
                study_answer.append(str(study_answer_split[a]))
        if(len(current_label)==0):
            current_label=study_sentences_revised[index]
            print(current_label_local)
            print(current_label)
            print(getCurrentLabel())
        print(study_answer)
        print(current_label)
def getCurrentLabel():
    print(current_label)
    return current_label

def getAnswer():
    return study_answer