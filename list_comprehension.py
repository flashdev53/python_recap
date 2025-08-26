server_ids=[1,2,3,4,5,6]
even_servers=[sid for sid in server_ids if sid % 2==0]
print("Even Servers:", even_servers)