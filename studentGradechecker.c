#include<stdio.h>
//project 0: Student grade analyzer:
void PrintStudentResults(char name[],int score){
    if (score>=80){
        printf("%s excellent work for scoring %d.You have an A\n",name,score);
    }
    else if (score>=70 && score<80){
        printf("%s great effort on your %d. You have a B.\n",name,score);
    }
    else if (score>=60 && score<70){
        printf("%s good effort on your %d,but work harder. You have a C\n",name,score);
    }
    else if (score>=50 && score<60){
        printf("%s don't worry,better luck next time,you have a %d and your grade is D\n",name,score);
    }
    else{
        printf("%s don't lose hope,keep moving forward. You have scored %d and have a D\n",name,score);
    }
}

int main(void){
    //ask how many students are in the class
    float average =0;
    int total= 0;
    int number;
    int i;
    char name[50][101];
    int score[50];
    printf("\n CLASS OF 2025\n");
    printf("How many students are in the class this year: ");
    scanf("%d",&number);

    getchar();


    //ask for each student's name and score:
    for (i=0; i<number;i++){
        printf("What is your name %d: ",i+1);
        scanf("%[^\n]",name[i]);


        printf("what did you score %d: ",i+1);
        scanf("%d",&score[i]);

        getchar();
    }
    for (i=0;i<number;i++){
        PrintStudentResults(name[i],score[i]);
    }
    for (i=0;i<number;i++){
        total = total + score[i];
    }
        average = total/number;
        printf("Average: %.2f\n",average);
    return 0;
}
