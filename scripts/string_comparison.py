from numpy import eye, empty, nditer, append
from difflib import SequenceMatcher


# %% Filtering similarity, so we can easily see which quotes are simular to each other
def check_for_string_similarity(string_list):
    difference_matrix = eye(len(string_list))
    pivot = 0
    for qi1 in range(len(string_list)):
        for qi2 in range(pivot, len(string_list)):
            difference_matrix[qi1, qi2] = SequenceMatcher(None, string_list[qi1], string_list[qi2]).ratio()
        pivot += 1
        # in general, we use the pivot to help us reduce calculation time, we don't need
        # to create a whole diff. matrix, we only need one (triangular) half of it :)
    return difference_matrix


def filter_by_similarity(string_list, tolerance=0.7, upper_bound_ignore=1.1):
    diff_matrix = check_for_string_similarity(string_list)
    simular_quotes = empty([0, 3], dtype=float)
    with nditer(diff_matrix, flags=["multi_index"]) as it:
        for similarity_measure in it:
            if (len(set(it.multi_index)) != 1
                    and (similarity_measure >= tolerance)
                    and (similarity_measure < upper_bound_ignore)):
                simular_quotes = append(
                    simular_quotes,
                    [[it.multi_index[0] + 1, it.multi_index[1] + 1, similarity_measure]],
                    axis=0)
    return simular_quotes
