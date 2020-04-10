from single_point import (parse, work_class_values, education_values, marital_status_values,
                          occupation_values, relationship_values, sex_values, race_values, native_country_values)

salary_values = ['<=50K', '>50K', '<=50K.', '>50K.']


# Here you need to implement the parser, don't forget to handle missing data...
def parse_data(data_file_full_path):
    """ This method parses the data into the final matrix [M x N] - called X matrix.
        and Nx1 vector of classifier results - Y vector.
    """
    f = open(data_file_full_path)
    final_x_matrix = list()
    final_y_vector = list()
    lines = f.readlines() #creates a list, each element in the list is a line in the data file
    for line in lines:
        #creates a list presentation of 'lines', with the relevant values for each attribute/feature
        line_list_presentation = line.replace(',', '').replace('\n', '').split(' ')
        try:
            #test whether it holds valid data and fix relevant attributes values if possible
            line_list_presentation = data_valid_fixer(line_list_presentation)
        except ValueError:
            continue
        x, y_value = parse(line_list_presentation)
        #append returned vector to x matrix, and return result to y vector
        final_x_matrix.append(x)
        final_y_vector.append(y_value)
    return final_x_matrix, final_y_vector


def data_valid_fixer(attributes):
    if not len(attributes) == 15:
        #if an object misses/holds extra attributes - we consider the object defective and ignore it.
        raise ValueError
    else:
        #for each attribute(=feature), we want to test if the attribute holds a valid value
            attributes[0] = int(attributes[0])
            work_class_values.index(attributes[1])
            attributes[2] = int(attributes[2])
            education_values.index(attributes[3])
            attributes[4] = int(attributes[4])
            marital_status_values.index(attributes[5])
            occupation_values.index(attributes[6])
            relationship_values.index(attributes[7])
            race_values.index(attributes[8])
            sex_values.index(attributes[9])
            attributes[10] = int(attributes[10])
            attributes[11] = int(attributes[11])
            attributes[12] = int(attributes[12])
            native_country_values.index(attributes[13])
            salary_values.index(attributes[14])
    return attributes


