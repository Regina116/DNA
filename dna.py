from sys import argv
from csv import reader, DictReader

if len(argv) != 3:
    print("Incorrect Input")
    exit(1)

with open(argv[1]) as csvfile:
    table = reader(csvfile)   #таблица csv

    header = next(table)[1:]  #список возможных srt

dictionary = {x: 1 for x in header}   #словарь: ключи - srt, значения - 1


with open(argv[2]) as dnafile:
    dna = reader(dnafile)

    for line in dna:
        dna = line[0]    #строка ДНК


for key in dictionary:

    l = len(key)  #длина srt
    temp = 0
    tempMax = 0

    for i in range(len(dna)-l):

        while temp > 0:
            temp = 0
            continue

        if dna[i:i+l] == key:

            while dna[i:i+l] == dna[i+l:i+2*l]:
                temp+=1
                i+=l

            if temp > tempMax:
                tempMax = temp


    dictionary[key] += tempMax

with open(argv[1]) as csvfile:
    people = DictReader(csvfile)

    for person in people:
        match = 0

        for srt in dictionary:
            if dictionary[srt] == int(person[srt]):
                match+=1

        if match == len(dictionary):
            print(person['name'])
            exit(1)

    print("No match")















