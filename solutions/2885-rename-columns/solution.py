import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """
    Renames specific columns of the students DataFrame according to the mapping specifications.
    """
    # Mapping old column names to new column names
    column_mapping = {
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }
    
    # rename() creates a view/copy with updated column metadata without copying underlying data blocks
    return students.rename(columns=column_mapping)
