import openpyxl

# Cargar el archivo y la hoja
wb = openpyxl.load_workbook("golf-dataset-categorical.xlsx")
ws = wb.active

# Obtener los encabezados (primera fila)
headers = [cell.value for cell in ws[1]]

# Crear lista de diccionarios para cada fila de datos
dic_list = []
for row in ws.iter_rows(min_row=2, values_only=True):
    dic = dict(zip(headers, row))
    dic_list.append(dic)

def split_data(data):
    half = (len(data)//2)+1
    return data[:half], data[half:]

def build_frequency_table(data, target):
    # Retrieves 
    features = [key for key in data[0] if key != target]
    target_values = set(row[target] for row in data)
    # print(f"Target values: {target_values}")

    freq_table = {}
    for feature in features:
        freq_table[feature] = {}
        feature_values = set(row[feature] for row in data)
        for value in feature_values:
            freq_table[feature][value] = {t_val: 0 for t_val in target_values}

    for row in data:
        for feature in features:
            value = row[feature]
            t_val = row[target]
            freq_table[feature][value][t_val] += 1
    print(f"Frecuency table: {freq_table}")
    return freq_table

def train_one_r(freq_table):
    # Train the OneR model using the frequency table

    # Initialize variables to track the best feature and its error
    best_feature = None
    best_probability = None
    best_rule = {}

    # Iterate over each feature in the frequency table
    for feature, values in freq_table.items():
        print(f"Feature: {feature}")
        sum_target_value = 0
        sum_target_per_feature = 0
        # Iterate over each value of the feature
        for value, counts in values.items():
            temp_target_value = None
            print(f"    Value: {value}, Counts: {counts}")
            # Iterate over each target value and its count
            for target_value, count in counts.items():
                # Retrieve the total count of the target values
                sum_target_value += count
                # Check if the current count is less than the temporary target value
                if temp_target_value == None:
                    temp_target_value = count
                elif count < temp_target_value:
                    temp_target_value = count
                # print(f"        Target value: {target_value}, Count: {count}")
                # print(f"        temp: {temp_target_value}")
            # Calculate the sum of target values for the feature    
            sum_target_per_feature += temp_target_value
        print(f"{feature} probability: {sum_target_per_feature}/{sum_target_value}")
        # Check if this is the first feature being evaluated
        if best_feature == None:
            best_feature = feature
            best_probability = sum_target_per_feature
        else:
            # Check if the current feature has a lower error than the best feature so far
            if sum_target_per_feature < best_probability:
                best_feature = feature
                # Update the best probability
                best_probability = sum_target_per_feature
    # Print the best feature and its error
    print(f"Best feature: {best_feature}")
    print(f"Best probability: {best_probability}")

    # Retrieve the best rule for the best feature
    for value, counts in freq_table[best_feature].items():
        best_target = min(counts, key=counts.get)
        best_rule[value] = best_target 
    print(f"Best rule: {best_rule}")
    
    # Return the best feature and its rule
    return best_feature, best_rule


def main():
    print(dic_list)
    train_data, test_data = split_data(dic_list)
    freq_table = build_frequency_table(train_data, 'Class')
    train_one_r(freq_table)

main()

