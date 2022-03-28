class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __eq__(self,student): #Test for Equality
        return self.name==student.name
    def __lt__(self,student): #Test for Less than
        return self.name<student.name
    def __ge__(self,student): #Test for Greater than
        return self.name>=student.name
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    print("First Student:")
    student1 = Student("Harold", 5)
    for i in range(1, 6):
        student1.setScore(i, 100) #Student 1 score would be 100,100,100,100,1000
    print(student1)

    print('\nSecond Student: ')
    student2=Student('Miguel',5)
    for i in range(1, 6):
        student2.setScore(i, 50) #Student 2 score would be 50,50,50,50,50
    print(student2)
    print("\nMETHOD TEST:")
    print('Do they have same score?') 
    print(student1 == student2)

    print('\nIs Student 2 greater than Student 1 base on the result of the final average?')
    print(student2>=student1)

    print('\nIs Student 2 less than Student 1 base on the result of the final average?')
    print(student2<student1)
    
    print('\n')

if __name__ == "__main__":
    main()