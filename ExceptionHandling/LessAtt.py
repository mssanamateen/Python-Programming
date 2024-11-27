
class LowAttendanceError(Exception):
    def __init__(self, attendance, required):
        super().__init__(f"Attendance is too low! Current: {attendance}%, Required: {required}%")

def check_attendance(attendance, required=75):
    if attendance < required:
        raise LowAttendanceError(attendance, required)
    else:
        print("Attendance is sufficient.")


try:
    student_attendance = 65 
    check_attendance(student_attendance)  
except LowAttendanceError as e:
    print(f"Error: {e}")
