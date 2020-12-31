import os
import easygui as g

total_lines = 0

def search_files(address, target):
    os.chdir(address)
    all_files = os.walk(address)
    coding_files = []
    list1 = list(all_files)
    count_each_file = 0
    for each_file in list1:
        for each_item in each_file:
            for every in each_item:
                file_t = every.split('.')[-1]
                for each_one in target:
                    if (('.' + file_t) == each_one) and (len(file_t) <=4) and len(every) >= 4:
                            #print(file_t)
                            # print(len(file_t))
                            coding_files.append(list1[count_each_file][0] + '/' + every)
                            #coding_files.append(every)
        count_each_file += 1
    print(coding_files)
    get_file_length(coding_files)

def get_file_length(coding_files):
    global total_lines
    for each_file in coding_files:
        with open(each_file) as f:
            try:
                for each_line in f:
                    total_lines += 1
            except UnicodeDecodeError:
                pass
    percentage_counting(total_lines)

def percentage_counting(total_lines):
    percentage = (total_lines / 100000) * 100
    g.msgbox(msg = 'total attribute: ' + str(total_lines) + ' and the percentage is: ' + str(percentage) + ' %')

address = input('enter the files address:\n')
target = ['.c','.py','.java','.sql','.css','.js','.html']
search_files(address, target)
