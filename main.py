import createTable
import loadDimTable

if __name__ == "__main__":
    #create table
    createTable.execute()
    
    #load dim
    loadDimTable.execute()
    
    #load fact