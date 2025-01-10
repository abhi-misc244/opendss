import pandas as pd
import os

def add_elements_to_circuit(excel_file, sheet_name, function_name):
    """
    Converts an Excel file to a tab-separated text file with modified column values.

    Args:
        excel_file (str): Path to the Excel file.
        sheet_name (str): Name of the sheet within the Excel file.
        function_name (str): Name to replace 'Name=' in the text data.

    Returns:
        None
    """
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    for col in df.columns:
        df[col] = df[col].apply(lambda x: f"{col}={x}")
    text_data = df.to_csv(index=False, header=False, sep='\t')
    text_data = text_data.replace('Name=', function_name)

    # Specify the directory where you want to save the file
    save_path = 'CircuitData'
    os.makedirs(save_path, exist_ok=True)  # Create the directory if it doesn't exist

    txt_file = os.path.join(save_path, sheet_name + '.txt')
    with open(txt_file, 'w') as file:
        file.write(text_data)




def load_data_from_excel(excel_file):
    """
    Load data from the specified Excel file.

    Args:
        excel_file (str): Path to the Excel file.

    Returns:
        None  # You can modify this based on your requirements
    """

    sheet_functions = [
        ('Grid', 'New circuit.'),
        ('Loads', 'New load.'),
        ('Transformers', 'New transformer.'),
        ('Generators', 'New generator.'),
        ('Line', 'New Line.'),
        ('Monitors', 'New Monitor.')
    ]

    # Load data from each sheet
    for sheet_name, function_name in sheet_functions:
        add_elements_to_circuit(excel_file, sheet_name, function_name)

    return None






def test_function(excel_file, sheet_name, function_name):
    print(excel_file)
    print(sheet_name)
    print(function_name)
