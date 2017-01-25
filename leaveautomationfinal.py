# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:10:37 2016

@author: saisugeethkamineni
"""
# Leave Automation Project #
'''
start
'''
import time
import math
from sys import exit as close
import numpy as np
import matplotlib.pyplot as plt

database = open('leave automation.csv', 'r')
readDatabase = database.read()
# print('\n', readDatabase)
rows = readDatabase.split('\n')
# print (rows)
employee_rows = []
for i in range(len(rows)):
    employee_rows.append(rows[i])
    
# print (employee_rows)
employees = []
i = 0
for j in employee_rows:
    employees.append(j.split(','))
    del(employees[i][(len(employees[i])-1)])
    i += 1
# print (employees)
employees_data = []
for k in employees:
    employees_cells = []
    for l in k:
        employees_cells.append([l])
    employees_data.append(employees_cells)
# print('\n', employees_data)
for a in employees_data:
    for b in a:
        if b[0] == '':
            b.clear()
# print('\n', employees_data)
for a in employees_data:
    b = a[4][0]
    e = b[:2]
    c = b[3:5]
    d = b[6:]
    if int(e) > 31 or int(c) > 12 or int(d) > 16 or (int(e) > 29 and int(c) == 2) or (
            int(e) == 31 and (int(c) == (4 or 6 or 9 or 11))):
        print ("\nIncorrect joining date.")
        close()
    if int(d) + 30 != int(time.time() / (60 * 60 * 24 * 365)):
        a[5].append(8)
        a[18].append(24)
        a[6][0] = int(a[6][0])
        a[7].append(a[5][0] - a[6][0])
        a[19][0] = int(a[19][0])
        a[20].append(a[18][0] - a[19][0])
        a[9][0] = int(a[9][0])
        a[14][0] = int(a[14][0])
        if int(e) < 15:
            l = (((13 - int(c)) / 12.0) * 10.0)
            if l >= int(l) + 0.5:
                m = math.ceil(l)
            else:
                m = math.floor(l)
        else:
            l = (((12 - int(c)) / 12.0) * 10.0)
            if l >= int(l) + 0.5:
                m = math.ceil(l)
            else:
                m = math.floor(l)
        if int(d) == 15:
            a[14][0] = int(a[14][0])
            a[11][0] = int(a[11][0])
            a[15][0] = int(a[15][0])
            a[10][0] = int(a[10][0])
            a[16][0] = int(a[16][0])
            a[8].append((m - a[10][0] + 10))
            a[12].append(a[8][0] - a[9][0])
            if int(c) <= 6:
                if (time.time() / (60 * 60 * 24 * 365.0)) - (int(time.time() / (60 * 60 * 24 * 365.0))) <= 0.5:
                    a[13].append(30 - a[15][0] + 15)
                if (time.time() / (60 * 60 * 24 * 365.0)) - (int(time.time() / (60 * 60 * 24 * 365.0))) > 0.5:
                    a[13].append(30 - a[15][0] + 30)
            if int(c) > 7:
                if (time.time() / (60 * 60 * 24 * 365.0)) - (int(time.time() / (60 * 60 * 24 * 365.0))) <= 0.5:
                    a[13].append(15 - a[15][0] + 15)
                if (time.time() / (60 * 60 * 24 * 365.0)) - (int(time.time() / (60 * 60 * 24 * 365.0))) > 0.5:
                    a[13].append(15 - a[15][0] + 30)
            a[17].append(a[13][0] - a[14][0])
        if int(d) == 14:
            a[14][0] = int(a[14][0])
            a[15][0] = int(a[15][0])
            a[10][0] = int(a[10][0])
            a[11][0] = int(a[11][0])
            a[16][0] = int(a[16][0])
            a[8].append(m - a[11][0] + 10 - a[10][0] + 10)
            a[12].append(a[8][0] - a[9][0])
            a[16][0] = int(a[16][0])
            if int(c) <= 6:
                if (time.time() / (60 * 60 * 24 * 365.0)) - (int(time.time() / (60 * 60 * 24 * 365.0))) <= 0.5:
                    a[13].append(30 - a[16][0] + 30 - a[15][0] + 15)
                if (time.time() / (60 * 60 * 24 * 365.0)) - (int(time.time() / (60 * 60 * 24 * 365.0))) > 0.5:
                    a[13].append(30 - a[16][0] + 30 - a[15][0] + 30)
            if int(c) > 7:
                if (time.time() / (60 * 60 * 24 * 365.0)) - (int(time.time() / (60 * 60 * 24 * 365.0))) <= 0.5:
                    a[13].append(15 - a[16][0] + 30 - a[15][0] + 15)
                if (time.time() / (60 * 60 * 24 * 365.0)) - (int(time.time() / (60 * 60 * 24 * 365.0))) > 0.5:
                    a[13].append(15 - a[16][0] + 30 - a[15][0] + 30)
            a[17].append(a[13][0] - a[14][0])
    else:
        a[10][0] = int(a[10][0])
        a[11][0] = int(a[11][0])
        a[14][0] = int(a[14][0])
        a[15][0] = int(a[15][0])
        a[16][0] = int(a[16][0])
        if int(c) <= 6:
            if (time.time() / (60 * 60 * 24 * 365.0)) - (int(time.time() / (60 * 60 * 24 * 365.0))) <= 0.5:
                a[13].append(15)
            else:
                a[13].append(30)
            a[17].append(a[13][0] - a[14][0])
        if int(c) > 7:
            a[13].append(15)
            a[17].append(a[13][0] - a[14][0])
        if int(e) < 15:
            f = (((13 - int(c)) / 12.0) * 8.0)
            if f >= int(f) + 0.5:
                h = math.ceil(f)
            else:
                h = math.floor(f)
            g = (((13 - int(c)) / 12.0) * 24.0)
            if g >= int(f) + 0.5:
                i = math.ceil(g)
            else:
                i = math.floor(g)
            l = (((13 - int(c)) / 12.0) * 10.0)
            if l >= int(l) + 0.5:
                m = math.ceil(l)
            else:
                m = math.floor(l)
            a[5].append(h)
            a[18].append(i)
            a[8].append(m)
            a[6][0] = int(a[6][0])
            a[7].append(a[5][0] - a[6][0])
            a[19][0] = int(a[19][0])
            a[20].append(a[18][0] - a[19][0])
            a[9][0] = int(a[9][0])
            a[12].append(a[8][0] - a[9][0])
        else:
            f = (((12 - int(c)) / 12.0) * 8.0)
            if f >= int(f) + 0.5:
                j = math.ceil(f)
            else:
                j = math.floor(f)
            g = (((12 - int(c)) / 12.0) * 24.0)
            if g >= int(f) + 0.5:
                k = math.ceil(g)
            else:
                k = math.floor(g)
            l = (((12 - int(c)) / 12.0) * 10.0)
            if l >= int(l) + 0.5:
                m = math.ceil(l)
            else:
                m = math.floor(l)
            a[5].append(j)
            a[18].append(k)
            a[8].append(m)
            a[6][0] = int(a[6][0])
            a[7].append(a[5][0] - a[6][0])
            a[19][0] = int(a[19][0])
            a[20].append(a[18][0] - a[19][0])
            a[9][0] = int(a[9][0])
            a[12].append(a[8][0] - a[9][0])
# print('\n', employees_data)
for x in employees_data:
    x[30][0] = int(x[30][0])
    if x[30][0] == 0:
        x[22][0] = int(x[22][0])
        x[25][0] = int(x[25][0])
        x[28][0] = int(x[28][0])
        x[21].append(0)
        x[23].append(0)
        x[24].append(0)
        x[26].append(0)
        x[27].append(0)
        x[29].append(0)
    if (x[30][0]) == 1 or (x[30][0]) == 2:
        if (x[3][0]).lower() == 'male':
            x[21].append(32)
            x[22][0] = int(x[22][0])
            x[23].append(x[21][0] - x[22][0])
            x[24].append(0)
            x[25][0] = int(x[25][0])
            x[26].append(0)
            x[27].append(0)
            x[28][0] = int(x[28][0])
            x[29].append(0)
        else:
            x[24].append(90)
            x[27].append(30)
            x[25][0] = int(x[25][0])
            x[26].append(x[24][0] - x[25][0])
            x[28][0] = int(x[28][0])
            x[29].append(x[27][0] - x[28][0])
            x[21].append(0)
            x[22][0] = int(x[22][0])
            x[23].append(0)
# print('\n', employees_data)


#
##if __name__ == '__main__':
##    print('\n', employees_data)
# '''
# done
# '''

empid = input("Enter Employee ID: ")
for a in employees_data:
    q = a[1][0]
    if (empid == q):
        if (a[3][0] == "Male"):
            print("\nWelcome Mr." + a[2][0])
        else:
            print("\nWelcome Miss / Mrs." + a[2][0])
print('\n1. Query mode \n2. Update Mode')
choice = int(input("Enter '1' for query mode and '2' for update mode: "))
if choice == 1:
    for employee in employees_data:
        if empid == employee[1][0]:
            a = employee
            break
    n_groups = 7
#    print (a)
    used = [a[6][0], a[9][0], a[14][0], a[19][0], a[22][0], a[25][0], a[28][0]]
    balance = [a[7][0], a[12][0], a[17][0], a[20][0], a[23][0], a[26][0], a[29][0]]

    # create plot 
    ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 1

    rects1 = plt.bar(index + 0.2, balance, bar_width, color='g', label='Available')

    rects2 = plt.bar(index + bar_width - 0.1, used, bar_width, color='r', label='Used')

    plt.xlabel('Type of leaves')
    plt.ylabel('No. of leaves')
    plt.title('QUERY MODE')
    plt.xticks(index + bar_width + 0.05, ('CL', 'SL', 'EL', 'PDL', 'PL', 'ML', 'CC'))
    plt.legend(loc = "upper left")
    plt.tight_layout()
    plt.show()
    print("---------------------------------------------")
    print("|  CL    |          CASUAL LEAVES           |")
    print("|  SL    |           SICK LEAVES            |")
    print("|  EL    |          EARNED LEAVES           |")
    print("|  PDL   | PROFESSIONAL DEVELOPMENT LEAVES  |")
    print("|  PL    |         PARENTING LEAVE          |")
    print("|  ML    |         MATERNITY LEAVE          |")
    print("|  CC    |     CHILD CARETAKING LEAVE       |")
    print("---------------------------------------------")
    ch = input('Would you like to go thorugh the update mode? (y/n): ')
    if ch.lower() == 'y':
        for a in employees_data:
            if empid == a[1][0]:
                t = a
                break
                #     print (a)
        typ = input('Enter the type of leave(CL/SL/EL/PDL/PL/ML/CC): ')
        typ = typ.upper()
        num = int(input('Enter the number of leaves required:'))
        if (typ == 'CL' and num > a[7][0]) or (typ == 'SL' and num > a[12][0]) or (typ == 'EL' and num > a[17][0]) or (
                typ == 'PDL' and num > a[20][0]) or (typ == "PL" and num > a[23][0]) or (
                typ == 'ML' and num > a[26][0]) or (typ == 'CC' and num > a[29][0]):
            print('\nNumber of leaves applied for is either exceeding the balance in the respective category or is not applicable.')
        else:
#            print (t)
            u = 0
            if typ == 'CL':
                if num <= 2:
                    t[6][0] += (num)
                    print('\nThe leave is granted and the database has been updated.')
                    u=1
                else:
                    print('\nMaximum 2 at a time.')
            elif typ == 'SL':
                if num <= 3:
                    t[9][0] += (num)
                    print('\nThe leave is granted and the database has been updated.')
                    u=1
                else:
                    print('\nTaking more than 3 leaves requires a medical certificate.')
                    mc = input('Do you have a medical certificate?\n')
                    if mc.lower() == 'yes':
                        t[9][0] += num
                        print('\nThe leave is granted and the database has been updated.')
                        u=1
                    else:
                        print('\nSorry, leave cannot be granted.')
            elif typ == 'EL':
                t[14][0] += (num)
                print('\nThe leave is granted and the database has been updated.')
                u=1
            elif typ == 'PDL':
                t[19][0] += (num)
                print('\nThe leave is granted and the database has been updated.')
                u=1
            elif typ == 'PL':
                if t[3][0] == 'Male':
                    t[22][0] += (num)
                    print('\nThe leave is granted and the database has been updated.')
                    u=1
                else:
                    print('\nNot applicable.')
            elif typ == 'ML':
                if t[3][0] == 'Female':
                    t[25][0] += (num)
                    print('\nThe leave is granted and the database has been updated.')
                    u=1
                else:
                    print('\nNot applicable.')
            elif typ == 'CC':
                if t[3][0] == 'Female':
                    t[28][0] += (num)
                    print('\nThe leave is granted and the database has been updated.')
                    u = 1
                else:
                    print('\nNot applicable.')
            #         print (t)
            if u==1:
                for employee in employees_data:
                    for cell in range(len(employee)):
                        if cell == (5):
                            (employee[cell]).clear()
                        if cell == (7):
                            (employee[cell]).clear()
                        if cell == (8):
                            (employee[cell]).clear()
                        if cell == (12):
                            (employee[cell]).clear()
                        if cell == (13):
                            (employee[cell]).clear()
                        if cell == (17):
                            (employee[cell]).clear()
                        if cell == (18):
                            (employee[cell]).clear()
                        if cell == (20):
                            (employee[cell]).clear()
                        if cell == (21):
                            (employee[cell]).clear()
                        if cell == (23):
                            (employee[cell]).clear()
                        if cell == (24):
                            (employee[cell]).clear()
                        if cell == (26):
                            (employee[cell]).clear()
                        if cell == (27):
                            (employee[cell]).clear()
                        if cell == (29):
                            (employee[cell]).clear()
#                print (employees_data)
                file = ''
                n = 1
                for employee in employees_data:
                    if n == 1:
                        n = 2
                    else:
                        file += '\n'
        
                    for c in employee:
                        if c == []:
                            file += ('' + ',')
                        else:
                            file += (str(c[0]) + ',')
#                print (file)
                database.close()
                database = open('leave automation.csv', 'w+')
                database.write(file)
#                o = (database.read())
#                print (o)
    #        print (database.read())
            database.close()
    else:
        database.close()
        print('\nThe program has been terminated. Thank you!')
if choice == 2:
    for a in employees_data:
            if empid == a[1][0]:
                t = a
                break
                #     print (a)
    typ = input('Enter the type of leave(CL/SL/EL/PDL/PL/ML/CC): ')
    typ = typ.upper()
    num = int(input('Enter the number of leaves required:'))
    if (typ == 'CL' and num > a[7][0]) or (typ == 'SL' and num > a[12][0]) or (typ == 'EL' and num > a[17][0]) or (
            typ == 'PDL' and num > a[20][0]) or (typ == "PL" and num > a[23][0]) or (
            typ == 'ML' and num > a[26][0]) or (typ == 'CC' and num > a[29][0]):
        print('\nNumber of leaves applied for is either exceeding the balance in the respective category or is not applicable.')
    else:
        #         print (t)
        u = 0
        if typ == 'CL':
            if num <= 2:
                t[6][0] += (num)
                print('\nThe leave is granted and the database has been updated.')
                u=1
            else:
                print('\nMaximum 2 at a time.')
        elif typ == 'SL':
            if num <= 3:
                t[9][0] += (num)
                print('\nThe leave is granted and the database has been updated.')
                u=1
            else:
                print('\nTaking more than 3 leaves requires a medical certificate.')
                mc = input('Do you have a medical certificate?\n')
                if mc.lower() == 'yes':
                    t[9][0] += num
                    print('\nThe leave is granted and the database has been updated.')
                    u=1
                else:
                    print('\nSorry, leave cannot be granted.')
        elif typ == 'EL':
            t[14][0] += (num)
            print('\nThe leave is granted and the database has been updated.')
            u=1
        elif typ == 'PDL':
            t[19][0] += (num)
            print('\nThe leave is granted and the database has been updated.')
            u=1
        elif typ == 'PL':
            if t[3][0] == 'Male':
                t[22][0] += (num)
                print('\nThe leave is granted and the database has been updated.')
                u=1
            else:
                print('\nNot applicable.')
        elif typ == 'ML':
            if t[3][0] == 'Female':
                t[25][0] += (num)
                print('\nThe leave is granted and the database has been updated.')
                u=1
            else:
                print('\nNot applicable.')
        elif typ == 'CC':
            if t[3][0] == 'Female':
                t[28][0] += (num)
                print('\nThe leave is granted and the database has been updated.')
                u = 1
            else:
                print('\nNot applicable.')
        #         print (t)
        if u==1:
            for employee in employees_data:
                for cell in range(len(employee)):
                    if cell == (5):
                        (employee[cell]).clear()
                    if cell == (7):
                        (employee[cell]).clear()
                    if cell == (8):
                        (employee[cell]).clear()
                    if cell == (12):
                        (employee[cell]).clear()
                    if cell == (13):
                        (employee[cell]).clear()
                    if cell == (17):
                        (employee[cell]).clear()
                    if cell == (18):
                        (employee[cell]).clear()
                    if cell == (20):
                        (employee[cell]).clear()
                    if cell == (21):
                        (employee[cell]).clear()
                    if cell == (23):
                        (employee[cell]).clear()
                    if cell == (24):
                        (employee[cell]).clear()
                    if cell == (26):
                        (employee[cell]).clear()
                    if cell == (27):
                        (employee[cell]).clear()
                    if cell == (29):
                        (employee[cell]).clear()
#                print (employees_data)
            file = ''
            n = 1
            for employee in employees_data:
                if n == 1:
                    n = 2
                else:
                    file += '\n'
    
                for c in employee:
                    if c == []:
                        file += ('' + ',')
                    else:
                        file += (str(c[0]) + ',')
#                print (file)
            database.close()
            database = open('leave automation.csv', 'w+')
            database.write(file)
#            o = (database.read())
#            print (o)
#        print (database.read())
        database.close()
