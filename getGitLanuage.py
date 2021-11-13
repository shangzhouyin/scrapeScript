import os
from re import UNICODE
from statistics import median

path = "/Users/yinshangzhou/Desktop/scirpt/github_test" 
os.chdir(path)

def get_lines_of_code(path):
    file = open(path, "r", encoding='utf8') 
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    return line_count


def get_lines_stats(paths_list):
    lines = []
    for file in paths_list:
        lines.append(get_lines_of_code(file))
        total = sum(lines)
        median_value = median(lines)
    return total, median_value


listOfFiles = []
for (root, dirs, files) in os.walk(path):
    listOfFiles += [os.path.join(root, file) for file in files]

py = [fi for fi in listOfFiles if fi.endswith(".py")]
r = [fi for fi in listOfFiles if fi.endswith(".R")]
ts = [fi for fi in listOfFiles if fi.endswith(".ts")]
cpp = [fi for fi in listOfFiles if fi.endswith(".cc")]
C_sharp = [fi for fi in listOfFiles if fi.endswith(".cs")]
Ruby = [fi for fi in listOfFiles if fi.endswith(".rb")]
Julia = [fi for fi in listOfFiles if fi.endswith(".jl")]
php_ = [fi for fi in listOfFiles if fi.endswith(".php")]


py_total = get_lines_stats(py)[0]
py_median = get_lines_stats(py)[1]
print("Number of source code lines in Python: ", str(py_total))
print("Median number of source code lines in Python: ", str(py_median))
R_total = get_lines_stats(r)[0]
R_median = get_lines_stats(r)[1]
print("Number of source code lines in R: ", str(R_total))
print("Median number of source code lines in R: ", str(R_median))
ts_total = get_lines_stats(ts)[0]
ts_median = get_lines_stats(ts)[1]
print("Number of source code lines in Typescript", str(ts_total))
print("Median number of source code lines in Typescript", str(ts_median))
cpp_total = get_lines_stats(cpp)[0]
cpp_median = get_lines_stats(cpp)[1]
print("Number of source code lines in c++", str(cpp_total))
print("Median number of source code lines in c++", str(cpp_median))
c_total = get_lines_stats(C_sharp)[0]
c_median = get_lines_stats(C_sharp)[1]
print("Number of source code lines in c#", str(c_total) )
print("Median number of source code lines in c#", str(c_median))
ruby_total = get_lines_stats(Ruby)[0]
ruby_median = get_lines_stats(Ruby)[1]
print("Number of source code lines in ruby", str(ruby_total))
print("Median number of source code lines in ruby", str(ruby_median))
julia_total = get_lines_stats(Julia)[0]
julia_median = get_lines_stats(Julia)[1]
print("Number of source code lines in Julia", str(julia_total))
print("Median number of source code lines in Julia", str(julia_median))



