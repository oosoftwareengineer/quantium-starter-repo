import csv
import pandas as pd
from pathlib import Path


def csv_content_reader(file_path, search_criteria):
	'''Reads the content of csv and filter based on search criteria on a column name'''
	try:
		df = pd.read_csv(file_path)
		df = df[df["product"] == search_criteria]
		df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
		df["sales"] = df["price"] * df["quantity"]
		df_new_list = df[["sales", "date", "region"]]
	except AttributeError:
		print(f"File {file_path.name} does not have one of the attributes processed. Consider manual processing...")
	except Exception as e:
		print(f"An error occurred: {e}")
	else:
		return df[["date", "sales", "region"]]


def load_csv_content(search_criteria):
	path = Path()
	data_path = path / "data"

	df_list = []

	for file_path in data_path.rglob(f"*{'.csv'}"):
		df = csv_content_reader(file_path, search_criteria)
		df_list.append(df)

	merge_df = pd.concat(df_list, ignore_index = True)
	df_list.clear()
	print(merge_df)

	merge_df.to_csv(data_path / 'sales_data.csv', index = False)


if __name__ == "__main__":
	search_criteria = "pink morsel"
	load_csv_content(search_criteria)