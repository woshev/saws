my_dict = {
    "task": [
        "17-1",
        "17-2",
        "17-5",
        "17-24",
        "17-29"
    ],
    "Белов Максим": {
        "17-2": {
            "task_path_name": "17-2.py",
            "done": True,
            "auto_check": None,
            "teacher_check": None,
            "teacher_comment": None,
            "grade": None,
            "check_date": None
        },
        "17-5": {
            "task_path_name": "17-5.py",
            "done": True,
            "auto_check": None,
            "teacher_check": None,
            "teacher_comment": None,
            "grade": None,
            "check_date": None
        },
        "17-24": {
            "task_path_name": "17-24.py",
            "done": True,
            "auto_check": None,
            "teacher_check": None,
            "teacher_comment": None,
            "grade": None,
            "check_date": None
        },
        "17-29": {
            "task_path_name": "17-29.py",
            "done": True,
            "auto_check": None,
            "teacher_check": None,
            "teacher_comment": None,
            "grade": None,
            "check_date": None
        }
    }
}

for key,value in my_dict.items():
    if key == "task":
        print(*value)
    print(value)
