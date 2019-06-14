def tuple_tables(*args):

    #Turn however many excel ranges "tables" supplied. Into tuples
    
    newTables = []
    for table in args:
        newRows = []
        for row in table:
            newCells = []
            for cell in row:
                newCells.append(cell.value)
            if all(i != None for i in newCells):
                newCellsTuple = tuple(newCells)
                newRows.append(newCellsTuple)
            else:
                print("zero tuple")
        newRowsTuple = tuple(newRows)
        newTables.append(newRowsTuple)
    newTablesTuple = tuple(newTables)

    return newTablesTuple 

def differences_between_tuples(two_tupled_tables):

    #Calculate the symmetric difference between two tables supplied. Does not work with more than two tables

    items_not_in_tuple = set(two_tupled_tables[0]).symmetric_difference(two_tupled_tables[1])

    return items_not_in_tuple

def intersection_between_tuples(two_tupled_tables):

    #Calculate the intersection between two tables supplied. Does not work with more than two tables

    items_in_both_tuples = set(two_tupled_tables[0]).intersection(two_tupled_tables[1])

    return items_in_both_tuples

def inverse_intersection_between_tuples(two_tupled_tables):

    #Calculate the intersection between two tables supplied. Does not work with more than two tables
    #Reverses the intersection

    items_in_both_tuples_reverse = set(two_tupled_tables[1]).intersection(two_tupled_tables[0])

    return items_in_both_tuples_reverse


    