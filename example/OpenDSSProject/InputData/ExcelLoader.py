import pandas as pd

class ExcelLoader:
    def __init__(self, excel_file_path):
        """
        Initialize the ExcelLoader with the path to the Excel file.

        Args:
            excel_file_path (str): Path to the Excel file.
        """
        self.excel_file_path = excel_file_path


    def load_data(self):
        """
        Load data from the specified Excel file and return it as a DataFrame.

        Returns:
            pd.DataFrame: The loaded data as a DataFrame.
        """
        try:
            df = pd.read_excel(self.excel_file_path)
            return df
        except FileNotFoundError:
            print(f"Error: File '{self.excel_file_path}' not found.")
            return None

    def add_elements_to_circuit(self, sheet_name, function_name):
        """
        Converts an Excel sheet to a tab-separated text file with modified column values.

        Args:
            sheet_name (str): Name of the sheet within the Excel file.
            function_name (str): Name to replace 'Name=' in the text data.

        Returns:
            None
        """
        df = self.load_data()
        if df is not None:
            for col in df.columns:
                df[col] = df[col].apply(lambda x: f"{col}={x}")
            text_data = df.to_csv(index=False, header=False, sep='\t')
            text_data = text_data.replace('Name=', function_name)
            txt_file = sheet_name + '.txt'  # Replace with your desired text file name
            with open(txt_file, 'w') as file:
                file.write(text_data)
                print(f"Text data saved to {txt_file}")
        else:
            print("Error loading data. Cannot create text file.")



# Example usage:
if __name__ == "__main__":
    excel_path = "./OpenDSSInputSheet.xlsx"  # Specify the path to your Excel file
    loader = ExcelLoader(excel_path)
    loader.add_elements_to_circuit(sheet_name="Grid", function_name="New circuit.")
    loader.add_elements_to_circuit(sheet_name="Loads", function_name="New load.")
    loader.add_elements_to_circuit(sheet_name="Transformers", function_name="New transformer.")
    loader.add_elements_to_circuit(sheet_name="Generators", function_name="New generator.")
    loader.add_elements_to_circuit(sheet_name="Line", function_name="New Line.")
    loader.add_elements_to_circuit(sheet_name="Monitors", function_name="New Monitor.")

