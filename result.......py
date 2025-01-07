fullmarks = 800
obt_marks = 0
for x in range(8):
  marks = int(input("Enter your obtained marks"))
  totalobt_marks = obt_marks + marks
percent = (totalobt_marks/fullmarks)*100
if percent >= 90:
  print("Grade A")
elif percent < 90 and percent >= 80:
  print("Grade B")
elif percent < 80 and percent >= 70:
  print("Grade C")
elif percent < 70 and percent >= 60:
  print("Grade D")

