#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0

  for line in textFile:
    lineCount += 1
    words = line.split()
    

    for word in words:
      wordCount += 1
      words = line.split()

      for letter in word:
        print(letter)

  print("Lines:", lineCount)
  print("Words:", wordCount)
  

if __name__ == '__main__':
  main()
