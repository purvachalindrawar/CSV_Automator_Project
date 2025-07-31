import pandas as pd

def load_csv(file_name):
    try:
        df = pd.read_csv(file_name)
        print("✅ CSV Loaded Successfully!")
        return df
    except FileNotFoundError:
        print("❌ File not found. Please check the file name.")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def show_columns(df):
    print("\n🧾 Columns in the CSV:")
    print(df.columns.tolist())

def show_head(df):
    print("\n📄 First 5 rows of the CSV:")
    print(df.head())

def count_rows(df):
    print(f"\n🔢 Total Rows: {len(df)}")

def search_value(df, column, value):
    if column not in df.columns:
        print("❌ Column not found.")
        return
    result = df[df[column].astype(str).str.contains(value, case=False)]
    print(f"\n🔍 Search results for '{value}' in column '{column}':")
    print(result)

def main():
    file_name = input("📂 Enter CSV file name (e.g., language.csv): ")
    df = load_csv(file_name)
    if df is None:
        return

    while True:
        print("\n📋 Choose an operation:")
        print("1. Show column names")
        print("2. Show first 5 rows")
        print("3. Count rows")
        print("4. Search value in column")
        print("5. Exit")

        choice = input("👉 Enter your choice (1-5): ")

        if choice == '1':
            show_columns(df)
        elif choice == '2':
            show_head(df)
        elif choice == '3':
            count_rows(df)
        elif choice == '4':
            column = input("Enter column name: ")
            value = input("Enter value to search: ")
            search_value(df, column, value)
        elif choice == '5':
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
