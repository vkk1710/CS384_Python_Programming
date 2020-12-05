import pandas as pd
import os

os.chdir('F:/Acads/5th sem/Python CS384/CS384_1801CE31/Projects/P1 Quiz_via_CSV')

class quiz:
    def __init__(self,roll):
        print('Which quiz do you want to attend?')
        self.quiz = input()
        self.quiz_df = pd.read_csv(f'quiz_wise_questions//q{self.quiz}.csv')
        self.time = self.quiz_df.columns[-1]
        print(self.time)
        self.quiz_df.drop(columns = self.time)
        self.roll = roll
        #print(self.quiz_df)
        print('*'*80)
        
        
    def get_data(self):
        self.l = {}
        question = self.quiz_df['question']
        choices = self.quiz_df[['option1','option2','option3','option4']]
        correct_opt = self.quiz_df['correct_option']
        marks_correct = self.quiz_df['marks_correct_ans']
        marks_wrong = self.quiz_df['marks_wrong_ans']
        compulsion = self.quiz_df['compulsory']
        ind = list(self.quiz_df.index)
        for i in ind:
            d = {}
            d['question'] = question[i]
            d['choices'] = list(choices.iloc[i])
            d['correct_option'] = correct_opt[i]
            d['marks_correct_ans'] = marks_correct[i]
            d['marks_wrong_ans'] = marks_wrong[i]
            d['compulsion'] = compulsion[i]
            self.l[i+1] = d
        print(self.l)   
    def main(self):
        self.ques_dict = self.l
        print(self.ques_dict)
        print('*'*80)
        self.num_ques = len(self.ques_dict)
        self.ques_attempted = []
        self.obtained_marks = 0
        self.total_marks = 0
        self.num_correct_ans = 0
        self.num_wrong_ans = 0
        self.num_unattempted = 0
        self.user_response_list = []
        for i in self.ques_dict:
            print('\tQuestion '+str(i)+') ',self.ques_dict[i]['question'])
            choices_list = self.ques_dict[i]['choices']
            for n in range(len(choices_list)):
                print(f'Option {n+1}) ',choices_list[n])
            print('\n')
            correct_marks = self.ques_dict[i]['marks_correct_ans']
            negative_marks = self.ques_dict[i]['marks_wrong_ans']
            compulsion = self.ques_dict[i]['compulsion']
            print(f'\tCredits if Correct Option: {correct_marks}')
            print(f'Negative Marking: {negative_marks}')
            print(f'Is compulsory: {compulsion}\n')
            if(compulsion == 'n'):
                print('\tEnter Choice: 1, 2, 3, 4, S : S is to skip question')
                ans_entered = input()
                while(ans_entered not in ['1','2','3','4','S']):
                    print('wrong choice made.....Please enter again:')
                    ans_entered = input()
                if(ans_entered != 'S'):
                    self.ques_attempted.append(i)
                    if(int(ans_entered) == self.ques_dict[i]['correct_option']):
                        self.num_correct_ans += 1
                        self.obtained_marks += self.ques_dict[i]['marks_correct_ans']
                    else:
                        self.num_wrong_ans += 1
                        self.obtained_marks += self.ques_dict[i]['marks_wrong_ans']
                else:
                   self.num_unattempted += 1 
            else:
                print('\tEnter Choice: 1, 2, 3, 4 :')
                ans_entered = input()
                while(ans_entered not in ['1','2','3','4']):
                    print('wrong choice made.....Please enter again:')
                    ans_entered = input()
                if(int(ans_entered) == self.ques_dict[i]['correct_option']):
                    self.num_correct_ans += 1
                    self.obtained_marks += self.ques_dict[i]['marks_correct_ans']
                else:
                    self.num_wrong_ans += 1
                    self.obtained_marks += self.ques_dict[i]['marks_wrong_ans']
                self.ques_attempted.append(i)
            self.user_response_list.append(ans_entered)
            self.total_marks += self.ques_dict[i]['marks_correct_ans']
            print('\n')
            print('choice made : ',ans_entered)
            print('*'*80)
        
        print(f'Total Quiz Questions: {self.num_ques}')
        print(f'Total Quiz Questions Attempted: {len(self.ques_attempted)}')
        print(f'Total Correct Question: {self.num_correct_ans}')
        print(f'Total Wrong Questions: {self.num_wrong_ans}')
        print(f'Total Marks: {self.obtained_marks/self.total_marks}')
        
        self.quiz_df['marked_choice'] = self.user_response_list
        self.quiz_df['Total'] = [self.num_correct_ans,self.num_wrong_ans,self.num_unattempted]
        self.quiz_df['Legend'] = ['Correct Choices','Wrong Choices','Unattempted']
        
        self.quiz_df.set_index('ques_no',inplace=True)
        # uploads the question wise response of student in csv file like q1_1701ME01.csv
        self.quiz_df.to_csv('individual_responses/'+f'q{self.quiz}_{self.roll}.csv')
        
# quiz_df = in the format of q1_1701ME01.csv ie this can be directly       
q = quiz('1801CE31')
q.get_data()
q.main()
print(q.quiz_df)

        