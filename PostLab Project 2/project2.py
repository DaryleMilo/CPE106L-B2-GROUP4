import random
x = random.randint(75,100)
class Student(object):
    """Represents a student."""


    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = [random.randint(75,100) ,random.randint(75,100),random.randint(75,100),random.randint(75,100),random.randint(75,100),random.randint(75,100),random.randint(75,100),random.randint(75,100),random.randint(75,100),random.randint(75,100)]
    
          

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
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __eq__(self,student):
        return self.name==student.name
    def __lt__(self,student):
        return self.name<student.name
    def __ge__(self,student):
        return self.name>=student.name
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Student Number: " + self.name  + "\nScores: " + " ".join(map(str, self.scores)) 

def main():
  
    list=[]

    for count in reversed(range(5)):
        s=Student("202011221"+str(count+1),10)
        list.append(s)

    print("Sorted list of the students: ")
    random.shuffle(list)

    list.sort()

    for obj in list:
        print(obj.__str__())




if __name__ == "__main__":
    main()