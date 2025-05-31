def levenshtein_distance(str1, str2):


    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1

    # Initialize a 2D matrix to store distances
    distance_matrix = [[0 for _ in range(len_str2)] for _ in range(len_str1)]

    # Initialize the first row and column of the matrix
    for i in range(len_str1):
        distance_matrix[i][0] = i
    for j in range(len_str2):
        distance_matrix[0][j] = j

    # Fill in the matrix based on the Levenshtein distance algorithm
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            distance_matrix[i][j] = min(
                distance_matrix[i - 1][j] + 1,           
                distance_matrix[i][j - 1] + 1,          
                distance_matrix[i - 1][j - 1] + cost    
            )

    # The bottom-right cell of the matrix contains the Levenshtein distance
    return distance_matrix[len_str1 - 1][len_str2 - 1]
