import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    students_subjects = students.merge(subjects, how='cross')
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    return (
        students_subjects
        .merge(exam_counts, on=['student_id', 'subject_name'], how='left')
        .fillna({'attended_exams': 0})
        .astype({'attended_exams': 'Int64'})
        .sort_values(['student_id', 'subject_name'])
        .reset_index(drop=True)
    )