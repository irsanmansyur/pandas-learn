import pandas as pd

df = pd.read_csv("./data/Mutation.csv")


# Menampilkan jumlah nomor yang transaksi di atas satu juta
def get_count_number_if():
  # filter if balance lebih besar dari 1 juta"
  df_if = df[df.balance >=  1000000];

  # Group by number of mutations and reset count
  print_this = df_if.groupby(["number"]).size().reset_index(name="jumlah_nomor")
  print(print_this)

get_count_number_if()


# sorting by balance descending and show top 10
def get_top_10_balance():
  print(df.sort_values(by=["balance"], ascending=False).head(10))

# get_top_10_balance() 