from single_point import (parse, work_class_values, education_values, marital_status_values,
                          occupation_values, relationship_values, sex_values, race_values, native_country_values)

# These possible salary values were added here and not under 'single_point' in order to leave 'single_point' the same
# way received (unchanged). Logically, this variable belongs there alongside the different features valid values.
salary_values = ['<=50K', '>50K', '<=50K.', '>50K.']

# Here you need to implement the parser, don't forget to handle missing data...
def parse_data(data_file_full_path):
    """ This method parses the data into the final matrix [M x N] - called X matrix.
        and Nx1 vector of classifier results - Y vector.
    """
    f = open(data_file_full_path)
    final_x_matrix = list()
    final_y_vector = list()
    lines = f.readlines() # Creates a list, each element in the list is a line in the data file
    data_size = len(lines) # Original data size (amount of objects provided)
    for line in lines:
        # creates a list presentation of 'lines', with the relevant values for each feature
        line_list_presentation = line.replace(',', '').replace('\n', '').split(' ')
        try:
            #test whether the object holds valid data and fix relevant features values if possible
            line_list_presentation = data_valid_fixer(line_list_presentation)
        except ValueError:
            #if one(or more) of the features holds non-valid value - it is ignored
            continue
        x, y_value = parse(line_list_presentation)
        #append parsed vector to x_matrix, and parsed label to y_vector
        final_x_matrix.append(x)
        final_y_vector.append(y_value)
    return data_size, len(final_y_vector), final_x_matrix, final_y_vector


# data_valid_fixer's responsibilities:
# 1- Make sure the features values held by the object is valid
# 2- Convert numeric values from str to int
def data_valid_fixer(features):
    if not len(features) == 15:
        #if an object misses/holds extra features - we consider the object defective and ignore it.
        raise ValueError
    else:
        #for each feature, we want to test if the feature holds a valid value
            features[0] = int(features[0])
            work_class_values.index(features[1])
            features[2] = int(features[2])
            education_values.index(features[3])
            features[4] = int(features[4])
            marital_status_values.index(features[5])
            occupation_values.index(features[6])
            relationship_values.index(features[7])
            race_values.index(features[8])
            sex_values.index(features[9])
            features[10] = int(features[10])
            features[11] = int(features[11])
            features[12] = int(features[12])
            native_country_values.index(features[13])
            salary_values.index(features[14])
    return features


