import pandas as pd

df_bids = pd.read_csv('bids.csv')
df_train = pd.read_csv('train.csv')

lst_humen = (df_train[df_train['outcome'] == 0.0]['bidder_id'].unique()).tolist()
lst_robots = (df_train[df_train['outcome'] == 1.0]['bidder_id'].unique()).tolist()

def label_bids(bidder_id):
	label = 2	# unknown
	if bidder_id in lst_humen:
		label = 0
	elif bidder_id in lst_robots:
		label = 1
	return label

df_bids['outcome'] = df_bids.apply(lambda row: label_bids(row['bidder_id']), axis=1)

print df_bids.head()
df_bids.to_csv('bids_labeled.csv', index=False)