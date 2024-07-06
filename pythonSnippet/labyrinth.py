from itertools import combinations
import xlrd
spreadsheet = xlrd.open_workbook('Labyrinth Team Builder.xlsx')
sheet = spreadsheet.sheet_by_name('veryBigTable')

#given input, calculates score combination and returns highest one
def camp_score(comb_arr, char_dict, story_dict, story_arr):
    score_arr = []
    iter_comb = combinations(range(8), 2)
    story_comb_arr = [e for e in iter_comb]

    for story in story_comb_arr:
        score1 = 0
        score2 = 0

        char_id1 = story[0]//2
        char_id2 = story[1]//2
        story_id1 = story[0]%2
        story_id2 = story[1]%2
        
        char_story_id1 = char_dict[comb_arr[char_id1]][story_id1]
        char_story_id2 = char_dict[comb_arr[char_id2]][story_id2]

        for i in range(len(comb_arr)):
            if (i != char_id1):
                char_story_recept = char_dict[comb_arr[i]]
                score1 = score1 + char_story_recept[char_story_id1+2]
            if (i != char_id2):
                char_story_recept = char_dict[comb_arr[i]]
                score2 = score2 + char_story_recept[char_story_id2+2]
        score_arr.append([
            score1, comb_arr[char_id1], story_arr[char_story_id1], 
            score2, comb_arr[char_id2], story_arr[char_story_id2],
            #"char_id", char_id1, char_id2,
            #"char_story_id", char_story_id1, char_story_id2,
            #"story", story[0], story[1],
            #"story_id", story_id1, story_id2
        ])
    
    def sort_f2(elem):
        return elem[0]+elem[3]

    score_arr.sort(key=sort_f2)
    #for e in score_arr:
    #    print(e)
    return score_arr[len(score_arr)-1]

#create dictionary with stories as keys and id as values
story_dict = {}
story_arr = [0]*23
for i in range(0,22):
    story_arr[i] = sheet.cell(0, i+3).value
    story_dict[sheet.cell(0, i+3).value] = i

#create dictionary with char names as keys and array as values
#arrays are structured [story id1, story id2, reception story1, reception to story 2...]
#124 is last row in table
n = 1
char_dict = {}
while (n < 124):
    e = [sheet.cell(n, i).value for i in range(3,25)] 
    e.reverse()
    e.append(story_dict[sheet.cell(n,1).value])
    e.append(story_dict[sheet.cell(n,0).value])
    e.reverse()
    char_dict[sheet.cell(n,2).value] = e
    n = n + 1

print("This program is an assistance tool for Android Epic7's Labyrinth camping")
print("Give it at least 4 character names and it returns all combinations sorted by highest to lowest morale")
print("Enter 'd' to finish")
while (True):
    char_arr = []
    count = 0
    boolLoop = True
    boolLoopChar = True
    
    #prompt user input for characters
    #error message if character doesn't exist or you gave it less than 4 chars
    while (boolLoop):
        while (boolLoopChar):
            try:
                input_str = "Enter " + "character {0}".format(count + 1) + "'s name\n"
                char = input(input_str)
                if (char == 'd'):
                    if (count < 4):
                        raise NameError("error")
                    else:
                        boolLoop = False
                else:
                    e = char_dict[char]
                    char_arr.append(char)
                boolLoopChar = False
            except (KeyError) as e:
                print("That character doesn't exist")
            except (NameError) as e:
                print("You need to enter at least 4 characters")
        boolLoopChar = True
        count += 1
    
    #store combinations in array of string arrays with char names that has size 4
    def sort_f(elem):
        return elem[1][0] + elem[1][3]

    iter_comb = combinations([e for e in char_arr], 4)
    comb_arr = [e for e in iter_comb]
    comb_arr_score = [[e, camp_score(e, char_dict, story_dict, story_arr)] for e in comb_arr]
    comb_arr_score.sort(key=sort_f)
    comb_arr_score.reverse()

    #print top results, up to 60
    for e in range(min(len(comb_arr_score), 120)):
        print(comb_arr_score[e])