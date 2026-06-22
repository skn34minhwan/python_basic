from work_management import task_tracking, reporting

task_name = "코드 리뷰"
print(task_tracking.start_task(task_name))
print(task_tracking.end_task(task_name))
print(reporting.generate_report(task_name))
