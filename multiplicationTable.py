
def multipli_table(n,m):
    table = []
    for i in range(1,n+1):
        row = []
        table.append(row)
        for x in range(1,m+1):
            result = x * i 
            row.append(result)
    
    for row in table:
        print(row)
        
            
multipli_table(9,9)