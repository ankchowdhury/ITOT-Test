def generateTag(tableData,selectedType,selection,folderName,param1Name,param1,param2Name,param2):
	filterColumn = 'Type'
	filteredData = []
	
	# Check if tableData is not None and is a list of dictionaries
	if tableData:
	    # Loop through the rows in the table
	    for row in tableData:
	        # Ensure the row contains the filter column
	        if filterColumn in row:
	            # Check if the value in the specified column is in the selected values
	            if row[filterColumn] in selectedType:
	                # If it matches, add the row to the filteredData array
	                filteredData.append(row)
	
	for row in filteredData:
	    # Check if the "Tag" column exists in the row
	    if "Tag" in row:
	        tagName = row["Tag"]       
	        # Create the UDT instance
	        system.tag.addTag(parentPath=folderName, 
	                          name=tagName, 
	                          tagType="UDT_INST", 
	                          attributes={"UDTParentType": selection},
	                          parameters={param1Name : param1 , param2Name : param2})
	                          