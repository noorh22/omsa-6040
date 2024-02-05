# NOTEBOOK 1 - PYTHON BASICS
# PART 0
def strcat_ba(a, b):
    assert type(a) is str, f"Input argument `a` has `type(a)` is {type(a)} rather than `str`"
    assert type(b) is str, f"Input argument `b` has `type(b)` is {type(b)} rather than `str`"
    return b + a


def strcat_list(L):
    assert type(L) is list
    R = ''.join(reversed(L.copy()))
    return R


def is_number(x):
    from numbers import Number
    return isinstance(x, Number)


def floor_fraction(a, b):
    assert is_number(a) and a >= 0
    assert is_number(b) and b > 0
    return int(a // b)


def ceiling_fraction(a, b):
    assert is_number(a) and a >= 0
    assert is_number(b) and b > 0
    return int(a // b + 1)


def report_exam_avg(a, b, c):
    avg = (a + b + c) / 3
    return 'Your average score: ' + str(round(avg, 1))


def count_word_lengths(s):
    assert all([x.isalpha() or x == ' ' for x in s])
    assert type(s) is str
    res = [len(x) for x in s.split()]
    return res


# PART 1

def minmax(L):
    assert hasattr(L, "__iter__")
    return min(L), max(L)


def remove_all(L, x):
    assert type(L) is list and x is not None
    remove_list = [i for i in L if i != x]
    return remove_list


def compress_vector(x):
    assert type(x) is list
    d = {'inds': [j for j in range(len(x)) if x[j] != 0], 'vals': [i for i in x if i != 0]}
    print(d)
    return d


def decompress_vector(d, n=None):
    # Checks the input
    assert type(d) is dict and 'inds' in d and 'vals' in d, "Not a dictionary or missing keys"
    assert type(d['inds']) is list and type(d['vals']) is list, "Not a list"
    assert len(d['inds']) == len(d['vals']), "Length mismatch"

    # Determine length of the full vector
    i_max = max(d['inds']) if d['inds'] else -1
    if n is None:
        n = i_max + 1
    else:
        assert n > i_max, "Bad value for full vector length"

    x = []
    for l in range(n):
        index_array = [j for j in range(len(d['inds'])) if d['inds'][j] == l]
        value_array = [d['vals'][q] for q in index_array]
        x.append(sum(value_array))

    return x


def find_common_inds(d1, d2):
    assert type(d1) is dict and 'inds' in d1 and 'vals' in d1
    assert type(d2) is dict and 'inds' in d2 and 'vals' in d2
    d1_set = set(d1['inds'])
    d2_set = set(d2['inds'])
    array = []
    for i in d1_set:
        for j in d2_set:
            if j == i:
                array.append(j)
                break

    return array


# PART 2
def get_students(grades):
    names_list = [grades[i][0] for i in range(1, len(grades))]
    return names_list


def get_assignments(grades):
    assignments_list = [grades[0][i] for i in range(1, len(grades[0]))]
    return assignments_list


# Create a dict mapping names to lists of grades.
def build_grade_lists(grades):
    dict = {}
    for i in range(1, len(grades)):
        dict[grades[i][0]] = [int(grades[i][j]) for j in range(1, len(grades[i]))]
    return dict


def build_grade_dicts(grades):
    grades_dict = {grades[i][0]: {grades[0][j]: int(grades[i][j]) for j in range(1, len(grades[i]))} for i in
                   range(1, len(grades))}
    return grades_dict


# Create a dict mapping names to grade averages.


def build_avg_by_student(grades):
    avg_dict = {grades[i][0]: statistics.mean(int(j) for j in grades[i][1:]) for i in range(1, len(grades))}
    return avg_dict


def build_grade_by_asn(grades):
    asn_dict = {grades[0][i]: [int(grades[j][i]) for j in range(1, len(grades))] for i in range(1, len(grades[0]))}
    return asn_dict


# Create a dict mapping items to average for that item across all students.
import statistics


def build_avg_by_asn(grades):
    asn_avg_dict = {grades[0][i]: statistics.mean([int(grades[j][i]) for j in range(1, len(grades))]) for i in
                    range(1, len(grades[0]))}
    return asn_avg_dict


def get_ranked_students(grades):
    names = [grades[i][0] for i in range(1, len(grades))]
    avg_scores = [statistics.mean(int(j) for j in grades[i][1:]) for i in range(1, len(grades))]
    names_list = [j[1] for j in sorted(zip(avg_scores, names), reverse=True)]
    return names_list
