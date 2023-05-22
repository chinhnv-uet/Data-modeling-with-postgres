import createTable
import loadDimTable
import loadFactTable

if __name__ == "__main__":
    #create table
    createTable.execute()
    
    #load dim
    loadDimTable.execute()
    
    #load fact
    loadFactTable.execute()