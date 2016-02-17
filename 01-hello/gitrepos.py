"""
Email git repo to: lebrun.matt@gmail.com
"""
import random

gitrepos = {
    'chey': 'https://github.com/cheyluna/python_021712016',
    'adrian': 'https://github.com/aososa/python_exercises',
    'ferdie': 'https://github.com/fcpendon/python',
    'erik': 'https://github.com/joeriksanjose/python_exercise',
    'darwin': 'https://github.com/darwinnavarro9/python_exer_20160217',
    'jeszy': 'https://github.com/jeszytanada/python_exercise_flask',
    'pamela': 'https://github.com/pamJasme/python_exercises',
    'renzo': 'https://github.com/renzosunico/python_exercises',
    'fatima': 'https://github.com/fatimaPHP/python',
}

def choose():
    pick = random.choice(list(gitrepos.items()))
    print(pick)


if __name__ == '__main__':
    choose()
