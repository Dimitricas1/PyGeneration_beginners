import os

from StepikAPI import StepikAPI

COURSE_ID = "78-58852" # ID курса, для которого нужно получить прогресс



sapi = StepikAPI(client_id = os.environ["STEPIK_CLIENT_ID"],
                 client_secret = os.environ["STEPIK_CLIENT_SECRET"])

print(sapi.get_progress(course_id = COURSE_ID))
